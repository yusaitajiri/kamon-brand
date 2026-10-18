# Working on kamon-brand

This repository is the kamon brand itself: the tokens, the logos and icons, and the rules for every platform. No app installs it. Each platform kit (`kamon-react`, later `kamon-flutter`) pins a tagged version of it, copies what it needs and generates its own files, and apps install a kit. `docs/direction-platform-kits.md` explains the split.

The rules are in `rules/brand.md`. Read it before changing anything visible, a token or a rule.

## Changing the base

- Kits pin a version, so a change reaches a kit only when it syncs, and an app only when it upgrades its kit. Every change to what the kits copy (`tokens/tokens.json`, `logo/`, `icons/`, `rules/brand.md`) gets an entry under *Unreleased* in `CHANGELOG.md` that says what changed and what a kit, and the apps on it, have to do.
- Versions follow semver. Major: an app that follows the rules would look or behave differently, or a token, file or app id a kit uses is renamed or removed. Minor: something is added, such as a token, an app color, an app or a logo. Patch: a fix that doesn't change how a correct app looks.
- To release: move *Unreleased* under the new version with the date, commit, and tag that commit `vX.Y.Z`. Never move or delete a released tag, because the kits record which one they were built from. Then sync each kit to the new tag (its `AGENTS.md` says how) and release the kit.
- Each rule is written twice: in `rules/brand.md` for agents and in `README.md` for people. Change both.
- Logos and icons come out of `tools/build_logo.py` and the colors in `tokens/tokens.json`: `uv run tools/build_logo.py`. Edit those and rebuild, never the outputs.
- After changing `tokens/tokens.json`, regenerate the readable table: `uv run tools/build_tokens_doc.py`. Never edit `tokens/tokens.md` by hand.
- Nothing here is for one platform. CSS, TypeScript, Dart and components belong in the kits.
- `docs/direction-*.md` say why the brand is the way it is, as it stands now. When a decision changes, rewrite its page to the new decision; how it got there stays in the git history. Keep studies, candidates and screenshots out of the repository.
