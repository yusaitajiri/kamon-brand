# Changelog

The platform kits (`kamon-react`, later `kamon-flutter`) pin a tagged version of the base and copy from it, so a change here reaches a kit when it syncs, and an app when it upgrades its kit. Each version says what changed and what a kit has to do to take it.

Versions follow semver. A major version changes how an app that follows the rules looks or behaves, or renames or removes a token, file or app id a kit uses. A minor version adds something. A patch fixes something without changing how a correct app looks.

Versions 1.0.0 and 1.0.1 were releases of `@yusai/brand`, the single web package this repository used to be.

## Unreleased

## 2.0.0 — 2026-10-18

The repository is now `kamon-brand`, the platform-neutral brand, and no app installs it any more. The web side moved to `kamon-react` (`@yusai/kamon-react`). Nothing an app shows changes: the tokens, logos, icons and rules have the same values. `docs/direction-platform-kits.md` has the reasoning.

- **Removed, now in `kamon-react`:** `package.json` and the `@yusai/brand` package, `tokens/tokens.css`, `tokens/tokens.ts`, `ui/` (`ui.css`, the sample pages and their screenshots) and `scripts/brand-sync.mjs`. `kamon-react` generates the token files from `tokens/tokens.json`.
- **The rules moved** from `skills/brand-ui/SKILL.md` to `rules/brand.md` and no longer name web files, classes or React Native functions. Each kit builds its `brand-ui` skill from them and adds its platform's part.
- **Added `tokens/tokens.md`,** every token as tables to read, generated from `tokens/tokens.json` by `tools/build_tokens_doc.py`.
- **The brand has no name of its own.** It was called Yusai Tajiri; now it's unnamed, and "the kamon brand" where a label is needed. Its own logo and icons moved from `logo/yusai-tajiri*.svg` and `icons/yusai-tajiri/` to `logo/brand*.svg` and `icons/brand/`, and its app id from `yusai-tajiri` to `brand`. The drawings are unchanged; the SVG titles now say "Brand logo". A kit renames its references to the id and the files.
- **The docs keep only the decisions that stand.** The studies, candidate sheets and the pages about the retired notch and frame candidates are removed; `docs/direction-kamon.md` gives the reasoning for the 木瓜 frame and its double line in one place. They stay in the git history and under `v1.0.1`.
- **`tools/build_logo.py` runs with `uv run tools/build_logo.py`;** it declares its own dependencies. Its output is unchanged.

To move an app from `@yusai/brand` to `kamon-react`, follow `kamon-react`'s changelog for 1.0.0. An app can also stay on `@yusai/brand` 1.0.1, which keeps working as long as its tag can be fetched.

## 1.0.1 — 2026-10-18

Nothing an app shows changes. To upgrade, change the tag to `#v1.0.1` and install.

- **The kit is public.** The tokens, `ui.css`, the brand-ui skill and the scripts are under the MIT License. The logos, icons and names stay reserved (`LICENSE`, `TRADEMARKS.md`). Installing no longer needs a GitHub login or a CI token.
- **The README installs the kit as a dev dependency.** Nothing from it runs in the shipped app. Apps already on `dependencies` can move it over with nothing else to change.

## 1.0.0 — 2026-10-18

The first versioned release. It contains:

- **Tokens:** `tokens/tokens.json`, `tokens.css` and `tokens.ts`. They cover the warm-gray surfaces and ink, and five app colors (moss, shu, ai, budo and tetsu) with dark-mode values. They also cover type set in Zen Kaku Gothic New and IBM Plex Mono, 4px spacing, radii and `shadow-float`.
- **UI elements:** `ui/ui.css`. Button, text box, select, checkbox, switch, card, list, tag and empty state, plus the kamon's double line: the primary button's inner line, `.frame` and `.rule`.
- **Logos and icons:** `logo/` and `icons/`. Every app shares the 木瓜 frame with its own motif inside: 狐 for the brand, 千鳥 for Kikitori and 入れ子枡 for Explorer.
- **The brand-ui skill:** `skills/brand-ui/SKILL.md`. These are the brand rules for coding agents, including the recommended density (one rule, one frame, one primary per view) and the naming convention. Apps get it through `brand-sync`.

### Upgrading from a copied `brand/` folder

1. Add the kit as a dependency pinned to this version: `"@yusai/brand": "git+https://github.com/yusaitajiri/my-brand.git#v1.0.0"`. Then add `"postinstall": "brand-sync"` to the app's scripts and install.
2. Point imports at the package instead of the folder:
   - `brand/tokens/tokens.css` → `@yusai/brand/tokens/tokens.css`
   - `./brand/tokens/tokens` → `@yusai/brand/tokens/tokens`
3. Replace `@brand/AGENTS.md` in the app's `CLAUDE.md` with the line from the README that points Claude Code at the brand-ui skill.
4. Delete the copied `brand/` folder.
5. Check the app's UI against the skill. Copies made before 2026-10-18 had the notched primary button rather than the inner line, and no frame or rule.
