# Changelog

Apps install the kit pinned to a `react-vX.Y.Z` tag of the kamon-brand repository (see *Using it in an app* in `react/README.md`), so a change here reaches an app only when the app upgrades. Each version says what changed, including changes to the brand itself, and what an app has to do to upgrade.

Versions follow semver. A major version changes how an app that follows the rules looks or behaves, or renames or removes something an app uses. A minor version adds something. A patch fixes something without changing how a correct app looks.

## Unreleased

## 2.0.0 — 2026-10-18

Kikitori is renamed Chidori, and the fonts move out of `tokens.css`.

- **App id:** `kikitori` is now `chidori`: `data-app="chidori"`, `<Logo app="chidori">`, `<EmptyState app="chidori">`, `appColors("chidori", …)`, `logo/chidori*.svg` and `icons/chidori/`. The drawings and the color, 朱 shu, are unchanged.
- **Fonts:** `tokens.css` no longer imports Google Fonts. The import is in `@yusai/kamon-react/tokens/fonts.css`, so an app that must stay offline can bundle the fonts instead.
- **Docs:** the repository's `README.md` starts with how to set up an app, and the upgrade example in `react/README.md` uses the `react-v…` tags.

### Upgrading from 1.0.0

1. Change the tag to `#react-v2.0.0` and run a plain install.
2. Web apps: import `@yusai/kamon-react/tokens/fonts.css` before `tokens.css`. Apps that must not reach the network, such as Tauri apps, bundle Zen Kaku Gothic New (400, 500) and IBM Plex Mono (400) instead, for example from `@fontsource/zen-kaku-gothic-new` and `@fontsource/ibm-plex-mono`.
3. Kikitori only: replace `kikitori` with `chidori` in `data-app`, the `app` prop of `Logo` and `EmptyState`, `appColors` and any path into `logo/` or `icons/`, and regenerate the app icons from `icons/chidori/`.

## 1.0.0 — 2026-10-18

The first version of the React kit, tagged `react-v1.0.0`. It takes over the web side of `@yusai/brand` 1.0.1, which is retired, and adds React components. Nothing an app shows changes: `tokens.css` and `ui.css` have the same values and rules, and the demo pages match the old sample pages pixel for pixel.

- **Tokens:** `@yusai/kamon-react/tokens/tokens.css` and `@yusai/kamon-react/tokens` (formerly `tokens/tokens.ts`), now generated from the brand's `tokens/tokens.json`.
- **UI elements:** `@yusai/kamon-react/ui/ui.css`, unchanged apart from a `.logo` rule for the `Logo` component.
- **Components:** `Button`, `Field`, `Input`, `Select`, `Checkbox`, `Switch`, `Card`, `List`, `ListRow`, `Tag`, `EmptyState`, `Rule` and `Logo`.
- **Logos and icons:** `logo/` and `icons/`, the brand's own, shipped from the repository root. The brand's own logo is now `brand` (`logo/brand.svg`, `icons/brand/`, `<Logo app="brand">`), formerly `yusai-tajiri`.
- **The brand-ui skill:** the brand's rules followed by how to apply them in React. `brand-sync` copies it into the app as before.
- **Demo pages:** `react/demo/`, the old `elements.html`, `sample.html` and `dashboard.html` rebuilt from the components (`npm run demo`).

### Upgrading from `@yusai/brand` 1.0.x

1. Replace the dependency: remove `"@yusai/brand"` and add `"@yusai/kamon-react": "git+https://github.com/yusaitajiri/kamon-brand.git#react-v1.0.0"` under `dependencies`. Keep `"postinstall": "brand-sync"` and run a plain install.
2. Point imports at the new package:
   - `@yusai/brand/tokens/tokens.css` → `@yusai/kamon-react/tokens/tokens.css`
   - `@yusai/brand/ui/ui.css` → `@yusai/kamon-react/ui/ui.css`
   - `@yusai/brand/tokens/tokens` → `@yusai/kamon-react/tokens`
   - `node_modules/@yusai/brand/icons/` and `logo/` → `node_modules/@yusai/kamon-react/icons/` and `logo/`
3. Optionally replace markup written with the `ui.css` classes by the components (`<button class="button button-primary">` → `<Button variant="primary">`). The classes keep working, so this can happen screen by screen.
4. Replace `yusai-tajiri` with `brand` wherever the app uses the brand's own logo or icons: `logo/brand.svg`, `icons/brand/`.
5. The app's `.gitignore` entry for `.claude/skills/brand-ui/` stays as it is.
