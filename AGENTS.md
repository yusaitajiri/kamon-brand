# Working on kamon-brand

This repository is the kamon brand and its platform kits. The root holds the brand, the same on every platform: `tokens/tokens.json`, the logos and icons, and the rules (`rules/brand.md`). Each platform's kit lives in its own folder and is what apps install: `react/` is `@yusai/kamon-react`, and `flutter/` comes later. `docs/direction-platform-kits.md` explains the layout.

The rules are in `rules/brand.md`. Read them before changing anything visible, a token or a rule, and follow them for UI in this repository too.

## What comes from where

- **The brand, edited here:** `tokens/tokens.json`, the shapes in `tools/build_logo.py`, `rules/brand.md`, `README.md` and `docs/`.
- **Generated, never edited by hand:**
  - `logo/` and `icons/`: `uv run tools/build_logo.py`
  - `tokens/tokens.md`: `uv run tools/build_tokens_doc.py`
  - `react/tokens/tokens.css`, `react/src/tokens.ts`, `react/src/logos.ts` and `react/skills/brand-ui/SKILL.md`: `npm run generate`
  - `react/dist/`: `npm run build`
- **The React kit, edited here:** the components in `react/src/components/`, `react/ui/ui.css`, `react/skill/react.md`, the demo in `react/demo/`, and the root `package.json`, which is the React package's manifest. It has to be at the root because npm installs git dependencies only from a repository's root.

## Changing the brand

- After changing `tokens/tokens.json`, run `uv run tools/build_tokens_doc.py`, and `uv run tools/build_logo.py` if an app color changed. Then regenerate every kit (`npm run generate && npm run build` for React) in the same commit.
- Each rule is written twice: in `rules/brand.md` for agents and in `README.md` for people. Change both.
- Nothing at the root is for one platform. CSS, TypeScript, Dart and components belong in a kit's folder.
- `docs/direction-*.md` say why the brand is the way it is, as it stands now. When a decision changes, rewrite its page to the new decision; how it got there stays in the git history. Keep studies, candidates and screenshots out of the repository.

## Changing a kit

- Generated outputs and `react/dist/` are committed, so a git install builds nothing. `npm run check` regenerates and rebuilds and fails if a committed output was out of date. Run it before committing.
- A React component renders an element of `react/ui/ui.css` and adds no look of its own. A new look starts in `ui.css`, from the tokens.
- How to apply the rules in React is written twice: in `react/skill/react.md` for agents and in `react/README.md` for people. Change both.
- After changing anything visible, retake the screenshots in `react/ui/screens/` in light and dark from `npm run demo`, at the sizes of the ones there now.

## Releasing

- Each kit is released on its own. Apps pin a kit's tag, so a change reaches an app only when it upgrades. Every change to what a kit ships (for React, the `files` list in `package.json`, which includes the root `tokens/tokens.json`, `logo/` and `icons/`) gets an entry under *Unreleased* in that kit's changelog (`react/CHANGELOG.md`) that says what changed and what an app has to do when it upgrades. A brand change gets an entry in every kit that ships it.
- Versions follow semver, per kit. Major: an app that follows the rules would look or behave differently, or a file, class, component, prop, token or app id it uses is renamed or removed. Minor: something is added, such as a component, a prop, a token, an app color or a logo. Patch: a fix that doesn't change how a correct app looks.
- To release React: set `version` in `package.json`, move *Unreleased* in `react/CHANGELOG.md` under that version with the date, run `npm run check`, commit, and tag the commit `react-vX.Y.Z`. Flutter will use `flutter-vX.Y.Z`. Never move or delete a released tag, because apps' lockfiles point at it. The tags `v1.0.0` and `v1.0.1` are releases of `@yusai/brand`, the package this repository used to be.
