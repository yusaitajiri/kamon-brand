# Working on kamon-react

This repository is the kamon brand's kit for React on the web and in Tauri, which apps install as `@yusai/kamon-react`, pinned to a version. It's built from a pinned version of `kamon-brand` (recorded in `base.json`), which holds the brand itself. Follow the brand's rules for UI in this repository too:

@skills/brand-ui/SKILL.md

## What comes from where

- **Copied from `kamon-brand`, never edited here:** `tokens/tokens.json`, `logo/`, `icons/` and `rules/brand.md`. To change a color, a logo or a rule, change `kamon-brand`, release it, and sync.
- **Generated, never edited by hand:** `tokens/tokens.css`, `src/tokens.ts`, `src/logos.ts` and `skills/brand-ui/SKILL.md` come from `scripts/generate.mjs`; `dist/` from `npm run build`.
- **Written here:** the components in `src/components/`, `ui/ui.css`, `skill/react.md`, the demo pages in `demo/` and the docs.

## Changing the kit

- **Sync to a new base:** `npm run sync-base -- ../kamon-brand --ref vX.Y.Z`, then `npm run build`. It reads the files from that tag, records it in `base.json` and regenerates. Without `--ref` it reads the checkout as it is, to try an unreleased base change; never release the kit that way.
- After editing `skill/react.md`, run `npm run generate`. After editing a component, run `npm run build`. Both outputs are committed: apps install from git tags, and `dist/` means they build nothing.
- `npm run check` regenerates and rebuilds and fails if a committed output was out of date. Run it before committing.
- Apps pin a version, so a change reaches an app only when it upgrades. Every change to a shipped file (the `files` list in `package.json`) gets an entry under *Unreleased* in `CHANGELOG.md` that says what changed and what an app has to do when it upgrades. A base sync gets one too, naming the base version and passing on what its changelog asks of apps.
- Versions follow semver. Major: an app that follows the rules would look or behave differently, or a file, class, component, prop, token or app id it uses is renamed or removed. Minor: something is added, such as a component, a prop, a token, an app color or a logo. Patch: a fix that doesn't change how a correct app looks.
- To release: set `version` in `package.json`, move *Unreleased* under that version with the date, check that `base.json` names a tag, and once it's on `main`, tag that commit `vX.Y.Z` and push the tag. Never move or delete a released tag, because apps' lockfiles point at it.
- How to apply the rules in React is written twice: in `skill/react.md` for agents and in `README.md` for people. Change both. The brand's rules themselves are in `kamon-brand`.
- A component renders an element of `ui/ui.css` and adds no look of its own. A new look starts in `ui.css`, from the tokens.
- After changing anything visible, retake the screenshots in `ui/screens/` in light and dark from `npm run demo`, at the sizes of the ones there now.
