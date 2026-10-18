## In React: @yusai/kamon-react

This app applies the rules above with `@yusai/kamon-react`, the kit for React on the web and in Tauri. The kit is installed at `node_modules/@yusai/kamon-react/`, so `tokens/tokens.json` above means `node_modules/@yusai/kamon-react/tokens/tokens.json`, and the same for `logo/` and `icons/`. Its own files are in the package's `react/` folder: before writing UI, read `node_modules/@yusai/kamon-react/react/tokens/tokens.css` and `node_modules/@yusai/kamon-react/react/ui/ui.css`. The app pins a version of the kit, and this skill matches that version, so follow it even if the kit has moved on.

### Setup, once per app

- Import `@yusai/kamon-react/tokens/tokens.css` and then `@yusai/kamon-react/ui/ui.css` once, at the app's entry.
- Put the app's id on the root element, `<html data-app="kikitori">`, and `class="ui"` on `<body>`. The brand's own pages leave `data-app` out; their accent is moss.
- Dark mode follows the system. `data-theme="light"` or `"dark"` on `<html>` overrides it, for an app with its own theme setting.

### Use the components

Build with the kit's components before writing markup of your own. Each renders the matching class in `ui.css`:

| Component | Renders | Notes |
| --- | --- | --- |
| `Button` | `.button` | `variant="primary"` is the one accent-filled action per view, with the inner line; `"quiet"` for toolbars and rows. `type` defaults to `"button"`. |
| `Field` with `Input` or `Select` | `.field`, `.input`, `.select` | `label`, `help` and `error` (in words) on the Field; it sets `aria-invalid` and `aria-describedby` on the control. |
| `Checkbox`, `Switch` | `.check`, `.switch` | The label is the children. `className` goes on the label. |
| `Card` | `.card` | `frame` adds the kamon's frame: only on the one container being worked in. |
| `List`, `ListRow` | `.list`, `.list-row` | `selected` and `meta` (mono text at the end) on the row. |
| `Tag` | `.tag` | `pressed` for a selected filter. |
| `EmptyState` | `.empty` | `app` shows that app's logo at 48px above the one sentence. |
| `Rule` | `.rule` | Once, under the app bar. |
| `Logo` | inline SVG | `app` and `size`; the `-small` drawing below 32px, the dark color in dark mode. Pass `title` only when no name is written beside it. |

- Lay out pages with plain elements and CSS that takes every value from the tokens: `var(--space-6)`, `var(--radius-lg)`, `font: var(--text-heading)`, `color: var(--ink-muted)`. Never write a hex value, a px size for spacing, radius or type, or a font name.
- A container that has no component, such as a dialog, an editor or an edit panel, takes the frame as `className="frame"` next to its own classes. A dialog also takes `box-shadow: var(--shadow-float)`, `background: var(--surface-raised)` and `border-radius: var(--radius-lg)`.
- When values are needed in code, such as a canvas or a chart, import `brand` or `appColors(app, theme)` from `@yusai/kamon-react/tokens`.
- For the app icon in Tauri, point `tauri icon` at `node_modules/@yusai/kamon-react/icons/<app>/icon-1024.png`, then replace the `.ico` it writes with the kit's `icon.ico`, which draws the small sizes properly.

### React checks before you finish

1. No `style={{ color: "#…" }}`, hex values or px sizes for spacing, radius or type in the files you changed; CSS uses the `var(--…)` tokens.
2. Each view has at most one `<Button variant="primary">`, at most one `frame`, and `<Rule />` only under the app bar.
3. Logos come from `<Logo>` or the files in the kit's `logo/` and `icons/`, never a copied or redrawn SVG.
4. If the app runs, screenshot the changed screens with `prefers-color-scheme` light and dark.
