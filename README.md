# Yusai Tajiri

The personal brand for every app Yusai Tajiri makes: a calm, warm-gray interface and a family of logos. Every logo is a kamon (家紋), a Japanese family crest: the same four-lobed 木瓜 frame in every app, with a different motif inside for each one, an animal or an object that says what the app is for. Each app's logo is in its own color, so a row of them reads as one family and each one is easy to find.

That is the idea of the brand: the apps are ordinary, well-made tools that share one frame, and each one shows its own face.

<p>
  <img src="logo/yusai-tajiri.svg" height="96" alt="Brand logo: a fox's head inside a four-lobed crest frame, in moss">
  &nbsp;&nbsp;
  <img src="logo/kikitori.svg" height="96" alt="Kikitori logo: a plover inside the same frame, in vermilion">
  &nbsp;&nbsp;
  <img src="logo/explorer.svg" height="96" alt="File manager logo: nested measuring boxes inside the same frame, in indigo">
</p>

## Principles

1. **Calm first.** Generous spacing, a warm gray ground, plain words. Nothing in the UI competes for attention.
2. **One color per app, used with intent.** Moss is the brand's own color. Each app brings one color of its own and uses it the way the brand uses moss: to mark what you can act on and what is selected — not decoration. Everything else is shared.
3. **Personality lives at the edges.** The working UI stays normal and native. The logo is the app icon and belongs on the about page and the brand's own pages — never in the middle of a task.
4. **Made, not copied.** No imitation paper, wood, glass or metal. Surfaces are flat; depth comes from borders and spacing.

What this brand is **not**: neon or glow, neumorphic soft-3D, "light show" effects (animated gradients, blur, sparkle), brutalism (raw borders, clashing color, shouting type), or skeuomorphic objects. It also skips the stock web defaults: italic accent words in headlines, numbered "01 / 02 / 03" section labels, monospace eyebrow labels and pill-shaped buttons. If a choice leans toward any of these, pick the quieter option.

## Color

- Ground is `surface` (warm gray `#F3F1EC`), never pure white or cream. Cards use `surface-raised` with a `border` hairline.
- Text is `ink`; supporting text `ink-muted`; captions `ink-subtle`. All pass 4.5:1 on `surface` and `surface-raised` in both themes.
- UI is built with `accent`, the app's own color (see *App colors* below). `accent` fills at most one primary control per view; text on it is `on-accent`. Links and focus rings are `accent`.
- Selected rows, tags and active nav use `accent-tint` with `accent-deep` text.
- `moss` itself is the brand's color: the brand logo and the brand's own pages. On those pages, and in any app without a color of its own, `accent` is moss.
- `sage` and `blush` are illustration colors only. Never use them for text or status.
- Success is `moss` in every app. Errors are a muted brick (`danger`), warnings a dry ochre (`warning`). No pure red, yellow or bright green anywhere.
- Dark mode is a warm, slightly green near-black (`surface` `#1C1E1B`) with a lighter moss (`#8FB08F`). It should feel like the same room at night, not a different app. Every app color has a lighter dark-mode value too.

### App colors

Each app takes one color from this palette. The colors are traditional Japanese ones, matched in depth so no app is louder than another, and every one passes 4.5:1 for text on it and for links on `surface`, in both themes.

| Color | Light | Dark | App |
| --- | --- | --- | --- |
| 苔 `moss` | `#4E6B4F` | `#8FB08F` | The brand itself |
| 朱 `shu` | `#B0501F` | `#EBA57E` | Kikitori |
| 藍 `ai` | `#3B5878` | `#93AACB` | The file manager (working name *Explorer*) |
| 葡萄 `budo` | `#6E4C6E` | `#C29FC2` | Free for the next app |
| 鉄 `tetsu` | `#2F6265` | `#86B7B5` | Free for the next app |

- Each color has the same five tokens as moss: `shu`, `shu-hover`, `shu-deep`, `shu-tint`, `on-shu` and so on. Apps don't use them by name; they point `accent` at their color.
- One color per app, never two in one app. A new color must keep the same depth, pass the same contrast checks and stay clearly apart from `danger` (brick) and `warning` (ochre).
- 朱 sits between `danger` and `warning`. In a 朱 app an error is never shown by color alone: it always says what went wrong in words, as the voice rules already ask.

## Type

- **Zen Kaku Gothic New** for everything in the UI, Japanese and English. It is warm, slightly rounded and has no trendy serif signal. Weights 400 and 500 only.
- **IBM Plex Mono** for numbers that should line up, versions and code.
- Body text is 16px with a 27px line height. Do not tighten it — the air is part of the brand.
- Sentence case everywhere. Japanese-first apps write Japanese UI; English labels are not mixed in for style.

## Space and shape

- 4px base: `space-1` (4) through `space-16` (64). Phone gutters are `space-4`; card padding `space-6`; sections `space-8`. When unsure, add space.
- Corners: `radius-md` (8px) for controls, `radius-lg` (12px) for cards, `radius-sm` (6px) for chips and tags. `radius-full` only for avatars.
- No shadows except `shadow-float` on menus that float over content. Borders are 1px `border`.
- Motion is short (150–200ms) and functional: things fade or slide because they changed. No looping or decorative animation.

## The logos (app icons)

Every app has a logo drawn in one flat color, built like a kamon (家紋): a simple motif inside a frame. The frame is the same in every app: 木瓜, four lobes a little wider than tall, drawn as a band with a thin line inside it, the double outline of the classic crest. Only the motif inside changes from app to app, an animal or an object reduced to a few simple shapes. The shared frame makes the apps one family; the motif and the color tell them apart. The logos have no letters or kanji, so they read the same in any language.

| App | Motif | Color | Files |
| --- | --- | --- | --- |
| The brand itself | 狐 — a fox's head, for the brand's own pages and anything without an app of its own | 苔 moss | `logo/yusai-tajiri*.svg`, `icons/yusai-tajiri/` |
| Kikitori | 千鳥 — the plover of 波に千鳥 | 朱 shu | `logo/kikitori*.svg`, `icons/kikitori/` |
| File manager (working name *Explorer*) | 入れ子枡 — measuring boxes inside each other, as folders inside folders | 藍 ai | `logo/explorer*.svg`, `icons/explorer/` |

- **Files.** `logo/<app>.svg` is the logo in the app's color, `-on-dark` in its dark-mode color and `-ink` in ink for print and one-color uses. Each is one filled path and its cut-outs are transparent. Below 32px use the `-small` files: the same logo with one heavier band instead of the band and inner line, a wider gap and the motif without the cut-outs too fine to see.
- **App icons.** `icons/<app>/` holds the logo with its frame filled with paper, so it reads on light and dark taskbars alike and keeps the frame's own outline: `icon.svg`, PNGs from 16 to 1024px (24px and down use the small drawing), a Windows `icon.ico` with every size drawn for its size, and `app-icon-1024.png`, an opaque square on the warm ground for stores and iOS.
- **Tray and menu bar.** Use `logo/<app>-small-ink.svg` on light taskbars and `-small-on-dark.svg` on dark ones.
- **One color, flat.** Never two colors, gradients, outlines, shadows or texture. Don't rotate, mirror or stretch a logo, and don't redraw the frame for one app or put it in a circle (丸に木瓜): every app shares it as it is. On iOS and Android the system masks the icon to a rounded square or circle; the store icon already sits the frame inside that on the warm ground.
- **Black-and-white test.** Every logo must be recognisable in solid black at 16px and must not be confused with any other app's logo. Check this before adding one.
- **A new app's logo** is a new motif in the same frame: an animal or an object, from a traditional crest or the app's own idea, as 3–5 simple filled shapes with rounded corners and cut-outs instead of thin lines. No letters. Add it to `MOTIFS` in `tools/build_logo.py`, which sizes it to fill the frame, run it, and add the app to `tokens/tokens.json` → `apps`.
- `tools/build_logo.py` draws every logo file and icon, taking the colors from `tokens/tokens.json`. Change shapes there and colors in the tokens, then rebuild; never edit the outputs by hand.

## Voice

Plain, calm and brief, like a considerate friend. Say what happened and what to do next. No exclamation marks in system messages, no "successfully", no jokes in error messages. Empty states may have a little warmth, but stay one sentence.

- Good: 「まだ記録がありません。最初の一行を書いてみましょう。」 / "No entries yet. Write your first line."
- Avoid: "Oops!! Nothing here 😢 Let's get started!!!"

`AGENTS.md` has more examples, for saving, errors, going offline and confirming a delete.

## Using this on each platform

The brand lives in the accent color, the logo, type, empty states and words. Native controls stay native: on iOS use system navigation and sheets tinted with the app's `accent`; on Windows use standard window chrome; on the web build with these tokens directly. Never fight the platform to look "on brand".

## Colors at a glance

| Token | Light | Dark |
| --- | --- | --- |
| `surface` | `#F3F1EC` | `#1C1E1B` |
| `surface-raised` | `#FBFAF7` | `#252824` |
| `ink` | `#2A2826` | `#ECE9E2` |
| `ink-muted` | `#5E5A53` | `#B0ABA1` |
| `moss` | `#4E6B4F` | `#8FB08F` |
| `moss-tint` | `#DDE5D9` | `#2C382C` |
| `accent` | the app's color | the app's color |
| `sage` | `#C3CFBF` | `#4C5C4A` |
| `blush` | `#E3B7A6` | `#C99A8A` |

The full list, with a usage note for every token, is in `tokens/tokens.json`.

## Fonts

Both are free (SIL Open Font License) on Google Fonts:

- [Zen Kaku Gothic New](https://fonts.google.com/specimen/Zen+Kaku+Gothic+New) — weights 400, 500
- [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) — weight 400

`tokens/tokens.css` already imports them. In native apps, bundle the font files from Google Fonts.

## Files in this kit

| Folder | What's inside |
| --- | --- |
| `logo/` | Each app's logo as SVG: in its color, `-on-dark` and `-ink`, each also as `-small` for 24px and down. Each is one filled path; cut-outs are transparent. |
| `icons/` | One folder per app with its app icon: SVG, PNGs from 16 to 1024px, a Windows `.ico` and a store icon. At the top, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon-180.png` and `app-icon-1024.png` are the brand logo for the brand's own pages. |
| `tools/` | `build_logo.py` draws every file in `logo/` and `icons/` from one set of shapes, with the geometry in `logokit.py` (`pip install skia-pathops resvg-py pillow`, then `python tools/build_logo.py`). |
| `tokens/tokens.css` | CSS custom properties for web projects. Light by default, dark via the system setting or `data-theme="dark"`. |
| `tokens/tokens.ts` | The same values as a plain object for React, React Native and Expo. |
| `tokens/tokens.json` | The source of truth, with a usage note on every token. |
| `AGENTS.md` | The rules from this guide, condensed for coding agents, with more voice examples and a check to run before finishing UI work. |

## Using it in a project

Copy this folder into a repo as `brand/`. Then:

- **Web:** `@import "brand/tokens/tokens.css";`, put the app's id on the root element (`<html data-app="kikitori">`) and build with `var(--accent)`, `var(--space-6)` and so on. The brand's own pages need no `data-app`; their accent is moss.
- **React Native / Expo:** `import { appColors } from "./brand/tokens/tokens";` and use `appColors("kikitori", "light")` (or `"dark"`, from the system color scheme). It returns every color with `accent` set to the app's own.
- **App icon:** take `icons/<app>/` as the app's icon set; for Tauri, point `tauri icon` at `icons/<app>/icon-1024.png` and replace the `.ico` it writes with `icons/<app>/icon.ico`, which draws the small sizes properly.
- **Coding agents:** put the line `@brand/AGENTS.md` in the app's root `CLAUDE.md` so Claude Code loads the rules at the start of every session. Asking an agent in words to read a file only works if it decides to open it, and a file inside `brand/` is never loaded on its own. For other agents, add "Before touching UI, read `brand/AGENTS.md`." to their instruction file. If you change a rule, change it in both this README and `AGENTS.md`.
