# Changelog

Apps install the kit pinned to a version tag (see *Using it in a project* in `README.md`), so a change here reaches an app only when the app upgrades. Each version says what changed and what an app has to do to upgrade.

Versions follow semver. A major version changes how an app that follows the rules looks or behaves, or renames or removes something an app uses. A minor version adds something. A patch fixes something without changing how a correct app looks.

## Unreleased

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
