# Yusai Tajiri brand rules for coding agents

Follow these rules for any UI in an app that carries the Yusai Tajiri brand. Paths are relative to this folder, which apps keep at `brand/`. Take every value from the tokens instead of copying numbers: `tokens/tokens.json` is the source of truth (with a usage note on each token), `tokens/tokens.css` is for the web and `tokens/tokens.ts` for React and React Native. `README.md` is the guide for people, with the background behind these rules.

The brand is calm and warm gray. Each app has one accent color of its own and a logo: a kamon (家紋), the same four-lobed 木瓜 frame in every app with the app's own motif inside, an animal or an object. The brand's own color is moss and its own logo is the frame with a fox's head. Its personality lives at the edges of an app and never in the middle of a task.

## Color

- The page background is `surface`; cards are `surface-raised` with a 1px `border`. Never pure white, cream or a gradient.
- Text is `ink`, supporting text `ink-muted`, captions and placeholders `ink-subtle`.
- Build UI with `accent`, the app's own color, never with `moss`, `shu`, `ai` or another palette color by name. On the web set `data-app="<app id>"` on `<html>` (none for the brand's own pages); in React Native use `appColors(app, theme)` from `tokens/tokens.ts`. The app ids are in `tokens/tokens.json` → `apps`.
- `accent` fills at most one primary control per view, with `on-accent` text. Links and focus rings are `accent`. The accent marks what can be acted on or is selected, so using it as decoration weakens that signal.
- Selected rows, tags and active nav use an `accent-tint` background with `accent-deep` text.
- One app, one color: never use a second app's color in an app.
- Success is `moss` in every app, errors `danger` (on `danger-tint`), warnings `warning` (on `warning-tint`). No pure red, yellow or bright green. In an app whose accent is `shu`, never show an error by color alone; say it in words.
- `sage` and `blush` are illustration colors only. Never use them for text or status.
- Dark mode comes from the tokens (the system setting, or `data-theme="dark"` on the web). Don't pick dark colors by hand.

## Type

- `font-sans` (Zen Kaku Gothic New) for all UI text, Japanese and English, at weights 400 and 500 only.
- `font-mono` (IBM Plex Mono) only for numbers that should line up, versions and code.
- Body text is 16px with a 27px line height. Don't tighten it.
- Sentence case everywhere. Japanese-first apps write Japanese UI and don't mix in English labels for style.

## Space, shape and motion

- Spacing uses the `space-*` tokens (4px base): phone gutter `space-4`, card padding `space-6`, between sections `space-8`, around empty states `space-12`. When unsure, take the larger step.
- Corners: `radius-md` for buttons and inputs, `radius-lg` for cards and dialogs, `radius-sm` for chips and tags. `radius-full` is only for avatars.
- No shadows except `shadow-float` on menus and popovers that float over content. Depth comes from borders and spacing.
- Motion is 150–200ms, a fade or slide because something changed. No looping or decorative animation.

## Generic defaults to avoid

Without direction, models fall back on a few stock web styles that don't belong here. Don't use any of these:

- italic accent words in headlines
- numbered "01 / 02 / 03" section labels
- monospace or all-caps eyebrow labels above headings
- pill-shaped buttons
- white or cream page backgrounds
- gradients, glow, blur, glass effects or soft neumorphic shadows
- textures imitating paper, wood or metal

Use the plain, token-based choice from the sections above instead.

## Logos

- Logo: the app's icon and its symbol, in `logo/<app>.svg` (`-on-dark` on dark grounds, `-ink` for one-color use). Below 32px use the `-small` files. Never recolor a logo to another app's color, add a second color, outline, shadow or texture, rotate, mirror or stretch it, or redraw the frame for one app or put it in a circle. The brand's own pages use `logo/yusai-tajiri.svg`. App icons, `.ico` included, are ready-made in `icons/<app>/`; tray icons are `logo/<app>-small-ink.svg` on light taskbars and `-small-on-dark.svg` on dark ones. `tools/build_logo.py` makes all of these from the shapes in it and the colors in `tokens/tokens.json`; edit those and rebuild, never the outputs.

## Platforms

Native controls stay native: iOS system navigation and sheets tinted with the app's `accent`, standard Windows window chrome, and on the web plain HTML built on `tokens/tokens.css`. In React Native or Expo, use `appColors(app, "light" | "dark")` from `tokens/tokens.ts` to match the system color scheme.

## Voice

Plain, calm and brief. Say what happened and what to do next. No exclamation marks in system messages, no "successfully" (成功しました), and no jokes in error messages. Empty states may have a little warmth, in one sentence.

<examples>
Empty: 「まだ記録がありません。最初の一行を書いてみましょう。」 / "No entries yet. Write your first line."
Saved: 「保存しました。」 / "Saved."
Error: 「保存できませんでした。接続を確認して、もう一度お試しください。」 / "Couldn't save. Check your connection and try again."
Offline: 「オフラインです。接続が戻ると自動で同期します。」 / "You're offline. Changes will sync when you reconnect."
Confirm: 「この記録を削除しますか。元に戻せません。」 / "Delete this entry? This can't be undone."
Avoid: "Oops!! Nothing here 😢 Let's get started!!!" and "Successfully saved!"
</examples>

## Before you finish UI work

Check each item and say in your report what you checked:

1. Search the files you changed for color literals (`#` hex values, `rgb(`, `hsl(`). Every color should come from a token; only `tokens/` holds raw values.
2. Colors come through `accent`, not a palette color by name, and each view has at most one `accent`-filled control.
3. Spacing, corner radii and font sizes come from tokens, and body text is 16px / 27px.
4. Nothing from "Generic defaults to avoid" slipped in.
5. Any logo is the file from `logo/` or `icons/`, unchanged: the app's own, in its own color, `-small` below 32px.
6. Copy follows the voice rules above.
7. If you can run the app, screenshot the changed screens in light and dark mode and compare them with these rules.
