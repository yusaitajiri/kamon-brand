# Direction: one repository, a kit per platform

Status: adopted 2026-10-18, with `@yusai/kamon-react` 1.0.0. Before this the repository was `my-brand`, one package (`@yusai/brand`) that held the tokens as CSS and TypeScript, `ui.css`, the logos and the skill, and that apps installed directly.

## The problem

`@yusai/brand` was a web package with a brand inside it. `tokens.css` and `ui.css` were the brand's web form, `tokens.ts` its React form, and the rules pointed at both. A Flutter app could use none of it, and React components built on it would have needed a package of their own.

## The layout

```
kamon-brand/
├── tokens/  logo/  icons/  rules/  tools/  docs/   the brand, the same on every platform
├── react/                                          the React kit
├── flutter/                                        the Flutter kit, later
└── package.json                                    the React kit's manifest
```

- **The root holds the brand:** `tokens/tokens.json` as the source of truth, `tokens/tokens.md` generated from it for people, the logos and icons with the tool that draws them, the rules for every platform (`rules/brand.md`), `README.md` and these records. None of it is for one platform.
- **Each kit has a folder** and is what apps install. It generates its token files from `tokens/tokens.json` and builds its `brand-ui` skill from `rules/brand.md` with a part for its platform. A brand change regenerates every kit in the same commit.
- **Each kit is released on its own**, with its own version, changelog and prefixed tags (`react-v1.0.0`, `flutter-v1.0.0`). An app pins one kit's tag.

## Choices along the way

- **The tokens stay JSON, not markdown.** Markdown is easier to read but would have to be copied into each platform by hand, and the platforms would drift. JSON is free of any one platform, carries a usage note on every token and is read by `build_logo.py` and the generators. `tokens.md` is generated from it for reading.
- **One repository instead of a base repository and a repository per kit.** With separate repositories each kit copied the brand files from a tagged base and recorded the version, so every brand change took a base release, a sync and a kit release. In one repository the kits read the brand files directly, the logos exist once, and a brand change is one commit. The same person maintains both sides, so the separation bought nothing.
- **The React manifest sits at the root.** Apps install from git tags without a package registry, and npm installs a git dependency only from the repository's root. So `package.json` is at the root and its `files` list ships `react/` with the root's `tokens/tokens.json`, `logo/` and `icons/`. Pub can install from a subfolder of a git repository, so the Flutter kit keeps its `pubspec.yaml` in `flutter/`.
- **Built files are committed.** `react/dist/` and the generated token files are in the repository, so installing from git builds nothing. `npm run check` keeps them up to date.
- **The history continues here.** The tags `v1.0.0` and `v1.0.1` are releases of `@yusai/brand` and still check out the old web package. The original GitHub repository, `my-brand`, is retired.
