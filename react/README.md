# @yusai/kamon-react

The kamon brand for React apps on the web and in Tauri: the tokens as CSS and TypeScript, the UI elements in `ui/ui.css`, React components built on them, the logos and app icons, and the `brand-ui` skill that teaches coding agents the brand's rules.

This kit lives in the `react/` folder of the kamon-brand repository. The brand itself, its tokens, logos and rules, is at the repository's root, and its `README.md` explains the ideas behind it. The kit generates its files from those, and apps install the kit.

<p>
  <img src="ui/screens/sample-light.png" width="260" alt="A Kikitori screen built from the kit's components in light mode">
  &nbsp;
  <img src="ui/screens/sample-dark.png" width="260" alt="The same screen in dark mode">
</p>

## Using it in an app

Apps install the kit pinned to a version tag, so the kit can move on without changing any app until that app upgrades.

1. **Install it, pinned.** In the app's `package.json`:

   ```json
   "dependencies": { "@yusai/kamon-react": "git+https://github.com/yusaitajiri/kamon-brand.git#react-v1.0.0" },
   "scripts": { "postinstall": "brand-sync" }
   ```

   Then run a plain `npm install` or `pnpm install`. Installing with a package name (`npm install @yusai/kamon-react`) skips the app's own `postinstall`, so run the plain install once after adding the line. The built components are committed in `dist/`, so installing builds nothing.
2. **`brand-sync` runs after every install.** It copies the `brand-ui` skill into `.claude/skills/brand-ui/` and adds that folder to `.gitignore`. Claude Code doesn't look for skills inside `node_modules`, so this copy is what makes the skill visible. Redoing it on every install keeps it on the pinned version.
3. **Point Claude Code at the skill.** Add this line to the app's `CLAUDE.md` (or `AGENTS.md`):

   ```text
   For any UI work, use the brand-ui skill: it has the kamon brand rules for this app.
   ```

   Other coding agents don't read Claude Code skills, so point them at `.claude/skills/brand-ui/SKILL.md` in their own instruction file.
4. **Set up the page once.** Import the styles at the app's entry, and put the app's id on `<html>`:

   ```tsx
   import "@yusai/kamon-react/tokens/tokens.css";
   import "@yusai/kamon-react/ui/ui.css";
   ```

   ```html
   <html lang="ja" data-app="kikitori">
     <body class="ui">
   ```

   The brand's own pages need no `data-app`; their accent is moss. Dark mode follows the system; `data-theme="light"` or `"dark"` on `<html>` overrides it.
5. **Build with the components.**

   ```tsx
   import { Button, Card, Field, Input, Rule } from "@yusai/kamon-react";

   <Rule />
   <Card frame>
     <Field label="タイトル" error={error}>
       <Input value={title} onChange={(e) => setTitle(e.target.value)} />
     </Field>
     <Button variant="primary" type="submit">保存</Button>
   </Card>
   ```

6. **App icon.** For Tauri, point `tauri icon` at `node_modules/@yusai/kamon-react/icons/<app>/icon-1024.png`, then replace the `.ico` it writes with the kit's `icon.ico`, which draws the small sizes properly. Icons generated into the app are part of its build, so commit those.
7. **Upgrade on purpose.** Change the tag (`#react-v1.1.0`) and install again. `react/CHANGELOG.md` says what changed between the two versions and what the app needs to do. An agent can carry it out: "Upgrade @yusai/kamon-react from v1.0.0 to v1.1.0, following its CHANGELOG."

## The components

Each component renders the matching element of `ui.css`, so a page built from them looks exactly like one written with the classes, and the classes stay available for anything the components don't cover.

| Component | What it is |
| --- | --- |
| `Button` | Secondary by default. `variant="primary"` is the one accent-filled action per view, with the thin inner line that comes from the 木瓜 frame's double outline; `"quiet"` stays out of the way in toolbars and rows. |
| `Field`, `Input`, `Select` | A label over a text box or select, with help or an error under it. An error is always in words, and the Field marks the control invalid for screen readers. |
| `Checkbox`, `Switch` | With their labels. The switch's track is squared, not a pill. |
| `Card` | A raised card with a hairline border. `frame` gives it the kamon's frame, for the one container you're working in. |
| `List`, `ListRow` | Rows with an optional mono value at the end, and a selected state in the app's tint. |
| `Tag` | A small label or filter, with a pressed state. |
| `EmptyState` | One sentence, optionally under the app's logo. |
| `Rule` | 子持ち罫, the thick-over-thin line, once under the app bar. |
| `Logo` | The app's logo from `logo/`, in its color and its dark-mode color, with the small drawing below 32px. |

Values for code, such as a canvas or a chart, come from `@yusai/kamon-react/tokens`: `brand` holds every value and `appColors("kikitori", "dark")` returns the colors with `accent` set to the app's own.

The demo pages show every component and two sample screens: in the repository, `npm install`, then `npm run demo` and open the address it prints. `react/ui/screens/` has them in light and dark.

## Files in this kit

Paths are from the repository's root. The React package's manifest, `package.json`, is at the root because npm installs git dependencies only from there.

| File or folder | What's inside |
| --- | --- |
| `react/src/` | The components, and `tokens.ts` and `logos.ts`, which are generated. |
| `react/dist/` | The components built for apps, committed so a git install needs no build. |
| `react/tokens/tokens.css` | CSS custom properties generated from `tokens/tokens.json`. Light by default, dark through the system setting or `data-theme="dark"`, and `data-app` picks the accent. Apps import it as `@yusai/kamon-react/tokens/tokens.css`. |
| `react/ui/ui.css` | The UI elements built on the tokens, with the kamon's double line: the primary button's inner line, `.frame` and `.rule`. Apps import it as `@yusai/kamon-react/ui/ui.css`. `react/ui/screens/` has the demo pages in light and dark. |
| `react/skill/react.md` | How to apply the rules in React. |
| `react/skills/brand-ui/SKILL.md` | The skill apps get: `rules/brand.md` followed by `react/skill/react.md`, generated. |
| `react/scripts/` | `generate.mjs` writes the generated files from the brand at the root. `brand-sync.mjs` copies the skill into an app. |
| `react/demo/` | The demo pages, built from the components with Vite. |
| `react/CHANGELOG.md` | What changed in each version and what an app has to do to upgrade. |
| `tokens/tokens.json`, `logo/`, `icons/` | The brand's tokens, logos and app icons, shipped with the package from the root. |

## Changing the kit

The repository's `AGENTS.md` has the steps. A change to the brand itself, a color, a logo or a rule, is made at the root, and the kit is regenerated in the same commit with `npm run generate` and `npm run build`. Changes to how React applies the brand, the components, `ui.css` or `skill/react.md`, are made in `react/`. Releases are tagged `react-vX.Y.Z`.

## License

The style is open and the identity is reserved. The tokens, `ui.css`, the components, the skill, the scripts and the text of these docs are under the MIT License. The logos, the app icons and the apps' names, such as Kikitori, are all rights reserved. The repository's `LICENSE` has the terms, and `TRADEMARKS.md` says how to refer to the names and logos.
