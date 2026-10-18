# Working on the Yusai Tajiri brand kit

This repository is the brand kit that apps install as `@yusai/brand`, pinned to a version. The brand's rules are the `brand-ui` skill in `skills/brand-ui/SKILL.md`, which `brand-sync` copies into each app. Follow them for UI in this repository too:

@skills/brand-ui/SKILL.md

## Changing the kit

- Apps pin a version, so a change reaches an app only when it upgrades. Every change to a shipped file (the `files` list in `package.json`) gets an entry under *Unreleased* in `CHANGELOG.md` that says what changed and what an app has to do when it upgrades.
- Versions follow semver. Major: an app that follows the rules would look or behave differently, or a file, class, token or app id it uses is renamed or removed. Minor: something is added, such as a token, an app color, an element or a logo. Patch: a fix that doesn't change how a correct app looks.
- To release: set `version` in `package.json`, move *Unreleased* under that version with the date, and once it's on `main`, tag that commit `vX.Y.Z` and push the tag. Never move or delete a released tag, because apps' lockfiles point at it.
- Each rule is written twice: in `skills/brand-ui/SKILL.md` for agents and in `README.md` for people. Change both.
- Logos and icons come out of `tools/build_logo.py` and the colors in `tokens/tokens.json`. Edit those and rebuild, never the outputs.
- After changing anything visible, retake the screenshots in `ui/screens/` in light and dark.
- `docs/direction-*.md` record past decisions. Start a new one for a new direction rather than rewriting an old one.
