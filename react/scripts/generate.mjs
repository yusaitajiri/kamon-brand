#!/usr/bin/env node
// Generates the kit's files from what it copied from kamon-brand (see sync-base.mjs):
//   tokens/tokens.json  → tokens/tokens.css, src/tokens.ts
//   logo/*.svg          → src/logos.ts, the path data the Logo component draws
//   rules/brand.md + skill/react.md → skills/brand-ui/SKILL.md
// Run it after editing skill/react.md; sync-base runs it after every sync. Never edit the outputs.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const kit = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(kit, path), "utf8");
const write = (path, content) => {
  mkdirSync(dirname(join(kit, path)), { recursive: true });
  writeFileSync(join(kit, path), content);
};

const tokens = JSON.parse(read("tokens/tokens.json"));
const base = JSON.parse(read("base.json"));
const baseLabel = base.ref ? `kamon-brand ${base.ref}` : `an unreleased kamon-brand (${base.commit.slice(0, 7)})`;

const colors = tokens.color.tokens;
const byName = Object.fromEntries(colors.map((c) => [c.name, c]));
const refOf = (value) => value.match(/^\{(.+)\}$/)?.[1];
const resolveColor = (value, theme) => (refOf(value) ? resolveColor(byName[refOf(value)].value[theme], theme) : value);
const apps = tokens.apps.list;
const defaultColor = refOf(byName.accent.value.light);
const accentSet = (k) => ({
  accent: k,
  "accent-hover": `${k}-hover`,
  "accent-deep": `${k}-deep`,
  "accent-tint": `${k}-tint`,
  "on-accent": `on-${k}`,
});
const shadow = tokens.shadow.tokens;
const typeStyles = tokens.type.groups.flatMap((g) => g.styles.map((s) => ({ ...s, family: g.family })));
const firstFamily = (stack) => stack.split(",")[0].trim().replace(/^"|"$/g, "");

// ---------------------------------------------------------------- tokens.css

function cssThemeBlock(theme) {
  const lines = [];
  for (const c of colors) {
    const value = c.value[theme];
    if (theme === "dark" && refOf(value)) continue; // a reference resolves to the dark value by itself
    lines.push(`  --${c.name}: ${refOf(value) ? `var(--${refOf(value)})` : value};`);
  }
  for (const s of shadow) lines.push(`  --${s.name}: ${s.value[theme]};`);
  return lines;
}

const fontImport = `@import url('https://fonts.googleapis.com/css2?family=${firstFamily(tokens.type.families.sans).replace(/ /g, "+")}:wght@400;500&family=${firstFamily(tokens.type.families.mono).replace(/ /g, "+")}:wght@400&display=swap');`;

const css = [
  `/* Kamon brand tokens, generated from tokens.json (${baseLabel}) by scripts/generate.mjs. Don't edit.`,
  `   Light is default; dark follows the system or [data-theme="dark"]. Build with --accent; an app brings its`,
  `   own color with data-app on <html> (the brand's own pages stay moss). */`,
  fontImport,
  "",
  ":root {",
  ...cssThemeBlock("light"),
  ...tokens.spacing.tokens.map((s) => `  --${s.name}: ${s.value};`),
  ...tokens.radius.tokens.map((r) => `  --${r.name}: ${r.value};`),
  ...Object.entries(tokens.type.families).map(([k, v]) => `  --font-${k}: ${v};`),
  "  /* Type styles for the font shorthand: font: var(--text-body). */",
  ...typeStyles.map((s) => `  --text-${s.name}: ${s.fontWeight} ${s.fontSize}/${s.lineHeight} var(--font-${s.family});`),
  "  color-scheme: light;",
  "}",
  "",
  "@media (prefers-color-scheme: dark) {",
  ':root:not([data-theme="light"]) {',
  ...cssThemeBlock("dark"),
  "  color-scheme: dark;",
  "}",
  "}",
  "",
  ':root[data-theme="dark"] {',
  ...cssThemeBlock("dark"),
  "  color-scheme: dark;",
  "}",
  ...apps
    .filter((a) => a.color !== defaultColor)
    .flatMap((a) => [
      "",
      `[data-app="${a.id}"] {`,
      ...Object.entries(accentSet(a.color)).map(([k, v]) => `  --${k}: var(--${v});`),
      "}",
    ]),
  "",
].join("\n");

write("tokens/tokens.css", css);

// ---------------------------------------------------------------- tokens.ts

const px = (v) => Number.parseFloat(v);
const brand = {
  color: Object.fromEntries(
    ["light", "dark"].map((theme) => [theme, Object.fromEntries(colors.map((c) => [c.name, resolveColor(c.value[theme], theme)]))]),
  ),
  space: Object.fromEntries(tokens.spacing.tokens.map((s) => [s.name.replace("space-", ""), px(s.value)])),
  radius: Object.fromEntries(tokens.radius.tokens.map((r) => [r.name.replace("radius-", ""), px(r.value)])),
  apps: Object.fromEntries(apps.map((a) => [a.id, { color: a.color, logo: a.logo }])),
  type: Object.fromEntries(
    typeStyles.map((s) => [s.name, { size: px(s.fontSize), lineHeight: px(s.lineHeight), weight: s.fontWeight }]),
  ),
  font: Object.fromEntries(Object.entries(tokens.type.families).map(([k, v]) => [k, firstFamily(v)])),
};

const ts = `// Kamon brand tokens as plain values, generated from tokens.json (${baseLabel}) by
// scripts/generate.mjs. Don't edit. Numbers are px. On the web prefer the CSS custom properties in
// tokens/tokens.css; use these where a value is needed in code, such as a canvas or a chart.
export const brand = ${JSON.stringify(brand, null, 2)} as const;

export type ThemeName = keyof typeof brand.color;
export type AppName = keyof typeof brand.apps;

/** The theme's colors with accent set to the app's own color. */
export function appColors(app: AppName, theme: ThemeName) {
  const c = brand.color[theme];
  const k = brand.apps[app].color;
  return {
    ...c,
    accent: c[k],
    "accent-hover": c[\`\${k}-hover\`],
    "accent-deep": c[\`\${k}-deep\`],
    "accent-tint": c[\`\${k}-tint\`],
    "on-accent": c[\`on-\${k}\`],
  };
}
`;

write("src/tokens.ts", ts);

// ---------------------------------------------------------------- logos.ts
// The Logo component draws the logo files' own paths and fills them with the app's color token, which
// switches to the -on-dark color in dark mode, data-theme included. Check that the token values are the
// files' colors, so the drawn logo is exactly the file.

const pathOf = (svg) => svg.match(/<path fill="([^"]+)" d="([^"]+)"/).slice(1);
const logos = {};
for (const a of apps) {
  const [light, full] = pathOf(read(`logo/${a.id}.svg`));
  const [dark] = pathOf(read(`logo/${a.id}-on-dark.svg`));
  const [, small] = pathOf(read(`logo/${a.id}-small.svg`));
  const token = byName[a.color].value;
  if (light.toUpperCase() !== token.light.toUpperCase() || dark.toUpperCase() !== token.dark.toUpperCase()) {
    throw new Error(`logo/${a.id}.svg is ${light} / ${dark} but ${a.color} is ${token.light} / ${token.dark}. Rebuild the logos in kamon-brand.`);
  }
  logos[a.id] = { color: a.color, name: a.name, full, small };
}

write(
  "src/logos.ts",
  `// Path data of every logo in logo/, generated from those files (${baseLabel}) by scripts/generate.mjs.
// Don't edit. \`full\` is logo/<app>.svg and \`small\` logo/<app>-small.svg, both on a 140 x 140 grid.
export const logos = ${JSON.stringify(logos, null, 2)} as const;
`,
);

// ---------------------------------------------------------------- the brand-ui skill

const frontmatter = `---
name: brand-ui
description: Kamon brand rules for UI, with the React kit (@yusai/kamon-react) that applies them. Use for any UI work in an app that carries the kamon brand — building or changing screens, components, styles, colors, type, spacing, icons and logos, UI copy such as empty states and error messages, and app names. Covers the tokens, the app's accent color, the kamon's double line (primary button, frame, rule), the kit's components, voice, naming and a check before finishing.
---

<!-- Generated by scripts/generate.mjs from rules/brand.md (${baseLabel}) and skill/react.md. Don't edit. -->
`;

write("skills/brand-ui/SKILL.md", `${frontmatter}\n${read("rules/brand.md").trim()}\n\n${read("skill/react.md").trim()}\n`);

console.log(`generate: wrote tokens/tokens.css, src/tokens.ts, src/logos.ts and skills/brand-ui/SKILL.md from ${baseLabel}`);
