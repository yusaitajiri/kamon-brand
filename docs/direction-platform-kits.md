# Direction: a platform-neutral base and one kit per platform

Status: adopted 2026-10-18, in base 2.0.0 and `kamon-react` 1.0.0. Before this the repository was `my-brand`, one package (`@yusai/brand`) that apps installed directly and that held the tokens as CSS and TypeScript, `ui.css`, the logos and the skill.

## The problem

`@yusai/brand` was a web package with a brand inside it. `tokens.css` and `ui.css` were the brand's web form, `tokens.ts` its React form, and the rules pointed at both. A Flutter app could use none of it, and a React component library built on it would have made apps import two packages that had to agree on a version.

## The split

- **kamon-brand** (this repository) is the brand itself and is never installed by an app: `tokens/tokens.json` as the source of truth, `tokens/tokens.md` generated from it for people, the logos and icons with the tool that draws them, the rules for every platform (`rules/brand.md`), `README.md` and these records.
- **A platform kit** per platform is what apps install: `kamon-react` for React on the web, Tauri included, and later `kamon-flutter`. A kit pins a tagged version of the base, copies `tokens.json`, the logos, the icons and `rules/brand.md` from it, and generates its own token files. Its `brand-ui` skill is the base rules plus a part for its platform. Each kit has its own semver and changelog, and records the base version it was built from.
- **An app** pins one kit and never the base.

```
kamon-brand  ──tag vX.Y.Z──►  kamon-react    ──tag──►  Tauri and web apps
            ──tag vX.Y.Z──►  kamon-flutter  ──tag──►  Flutter apps
```

A change to the brand is released in the base first, then picked up by each kit when it syncs, and reaches an app when the app upgrades its kit. The kits don't have to move together.

## Choices along the way

- **The tokens stay JSON, not markdown.** Markdown is easier to read but would have to be copied into each platform by hand, and the platforms would drift. JSON is already free of any one platform, carries a usage note on every token and is read by `build_logo.py`. `tokens.md` is generated from it for reading.
- **Separate repositories, not a monorepo.** Apps install from git tags, and npm can't install a package from a subfolder of a git repository, so a monorepo would need a package registry and its logins. The toolchains differ too: Python for the base, Node and TypeScript for React, the Flutter SDK later. The release paces differ as well, since components change more often than the brand.
- **The kits copy files from the base instead of depending on it.** A Dart package can't depend on an npm package and the other way round. A copied file with the base version recorded next to it works the same way for every platform, and an app's dependency tree holds one brand package.
- **The base's history continues here.** It was `my-brand`, which is why its tags start at v1.0.0. Those tags were releases of `@yusai/brand` and still check out the old web package. The original GitHub repository is retired.
