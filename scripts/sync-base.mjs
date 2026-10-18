#!/usr/bin/env node
// Copies the brand from a kamon-brand checkout into this kit, records which version it came from in
// base.json, and regenerates the kit's own files from it (scripts/generate.mjs).
//
//   npm run sync-base -- ../kamon-brand --ref v2.0.0
//
// With --ref the files are read from that tag through git, so the kit is built from a released base.
// Without it they're read from the checkout as it is, to try an unreleased base change; base.json then
// says so, and the kit isn't released until it's synced to a tag.

import { execFileSync } from "node:child_process";
import { cpSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// What the kit takes from the base. Never edit these in the kit; change them in the base and sync.
export const FROM_BASE = ["tokens/tokens.json", "rules/brand.md", "logo", "icons"];

const kit = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
const refAt = args.indexOf("--ref");
const ref = refAt >= 0 ? args[refAt + 1] : null;
const base = resolve(args.find((a, i) => !a.startsWith("--") && i !== refAt + 1) ?? join(kit, "..", "kamon-brand"));

const git = (...a) => execFileSync("git", ["-C", base, ...a], { maxBuffer: 1 << 28 });
const text = (...a) => git(...a).toString().trim();

for (const path of FROM_BASE) rmSync(join(kit, path), { recursive: true, force: true });

if (ref) {
  for (const file of text("ls-tree", "-r", "--name-only", ref, "--", ...FROM_BASE).split("\n")) {
    mkdirSync(dirname(join(kit, file)), { recursive: true });
    writeFileSync(join(kit, file), git("show", `${ref}:${file}`));
  }
} else {
  for (const path of FROM_BASE) cpSync(join(base, path), join(kit, path), { recursive: true });
}

const record = ref
  ? { version: ref.replace(/^v/, ""), ref, commit: text("rev-list", "-n", "1", ref) }
  : {
      version: null,
      ref: null,
      commit: text("rev-parse", "HEAD"),
      uncommitted: text("status", "--porcelain", "--", ...FROM_BASE) !== "",
      note: "Synced from a kamon-brand checkout, not a tag. Sync to a tag before releasing the kit.",
    };
writeFileSync(join(kit, "base.json"), JSON.stringify(record, null, 2) + "\n");
console.log(`sync-base: copied ${FROM_BASE.join(", ")} from ${ref ? `kamon-brand ${ref}` : `the checkout at ${base}`}`);

await import("./generate.mjs");
