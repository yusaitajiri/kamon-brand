#!/usr/bin/env node
// Copies the brand-ui skill from the installed kit into the app's .claude/skills/, where Claude Code
// finds it (it doesn't look inside node_modules), and keeps that copy out of git. Apps run it on
// postinstall, so the copy always matches the kit version the app pins.

import { appendFileSync, cpSync, existsSync, mkdirSync, readFileSync, rmSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const kit = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const app = process.cwd();
const { version } = JSON.parse(readFileSync(join(kit, "package.json"), "utf8"));

if (resolve(app) === kit) {
  console.log("brand-sync: running inside the kit itself, nothing to copy.");
  process.exit(0);
}

const relative = ".claude/skills/brand-ui";
const source = join(kit, "skills", "brand-ui");
const target = join(app, relative);

rmSync(target, { recursive: true, force: true });
mkdirSync(dirname(target), { recursive: true });
cpSync(source, target, { recursive: true });
console.log(`brand-sync: copied the brand-ui skill from @yusai/brand ${version} to ${relative}/`);

// The copy is generated, like node_modules: ignore it so a kit upgrade never shows up as a hand edit.
const gitignore = join(app, ".gitignore");
const entry = `${relative}/`;
const lines = existsSync(gitignore) ? readFileSync(gitignore, "utf8").split(/\r?\n/) : [];
if (!lines.some((line) => line.trim() === entry || line.trim() === relative)) {
  const lead = lines.length && lines[lines.length - 1] !== "" ? "\n" : "";
  appendFileSync(gitignore, `${lead}\n# Copied from @yusai/brand by brand-sync on install\n${entry}\n`);
  console.log(`brand-sync: added ${entry} to .gitignore`);
}
