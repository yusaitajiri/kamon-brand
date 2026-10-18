# Changelog

Each kit has its own changelog, versions and tags:

- `@yusai/kamon-react`: `react/CHANGELOG.md`, tags `react-vX.Y.Z`
- the Flutter kit, later: `flutter/CHANGELOG.md`, tags `flutter-vX.Y.Z`

A brand change, such as a token, a logo or a rule, is recorded in the changelog of every kit that ships it.

Below is the history of `@yusai/brand`, the single web package this repository used to be. Its tags, `v1.0.0` and `v1.0.1`, still install it. An app on it moves to `@yusai/kamon-react` by following `react/CHANGELOG.md` for 1.0.0.

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
