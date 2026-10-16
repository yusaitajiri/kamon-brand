# Kudagitsune

The personal brand for every app Yusai Tajiri makes. A calm, warm-gray interface, signed with a hanko and kept company by a tiny fox that lives in a bamboo tube. Each app wears its own 家紋 (mon, a family crest) in its own color, so a row of them reads as one family and each one is easy to find.

The 管狐 (kudagitsune) is a fox spirit from Japanese folklore, small enough to live inside a bamboo tube and carried around by its owner as a helper. That is the idea of the brand: the apps are ordinary, well-made tools, and each one has a little spirit living at its edges.

<p>
  <img src="marks/hanko-square.svg" height="120" alt="Square hanko: a fox in a bamboo tube beside the kanji 管狐">
  &nbsp;&nbsp;
  <img src="marks/hanko-round.svg" height="120" alt="Round hanko: a fox in a bamboo tube">
  &nbsp;&nbsp;
  <img src="mascot/fox-pixel@4x.png" height="120" alt="Pixel kudagitsune, standard pose">
  <img src="mascot/fox-pixel-shy@4x.png" height="120" alt="Pixel kudagitsune, shy peek">
  <img src="mascot/fox-pixel-sleeping@4x.png" height="120" alt="Pixel kudagitsune, sleeping">
</p>

<p>
  <img src="mon/kudagitsune.svg" height="96" alt="Kudagitsune mon: in a ring, the fox looking out of its bamboo tube, in moss">
  &nbsp;&nbsp;
  <img src="mon/kikitori.svg" height="96" alt="Kikitori mon: in a ring, a plover over a wave, in vermilion">
  &nbsp;&nbsp;
  <img src="mon/explorer.svg" height="96" alt="File manager mon: in a ring, nested measuring boxes, in indigo">
</p>

## Principles

1. **Calm first.** Generous spacing, a warm gray ground, plain words. Nothing in the UI competes for attention.
2. **One color per app, used with intent.** Moss is the brand's own color. Each app brings one color of its own and uses it the way the brand uses moss: to mark what you can act on and what is selected — not decoration. Everything else is shared.
3. **Personality lives at the edges.** The working UI stays normal and native. The fox and the hanko appear in empty states, loading, success moments and the about page, and the mon is the app icon — never in the middle of a task.
4. **Made, not copied.** No imitation paper, wood, glass or metal. Surfaces are flat; depth comes from borders and spacing.

What this brand is **not**: neon or glow, neumorphic soft-3D, "light show" effects (animated gradients, blur, sparkle), brutalism (raw borders, clashing color, shouting type), or skeuomorphic objects. It also skips the stock web defaults: italic accent words in headlines, numbered "01 / 02 / 03" section labels, monospace eyebrow labels and pill-shaped buttons. If a choice leans toward any of these, pick the quieter option.

## Color

- Ground is `surface` (warm gray `#F3F1EC`), never pure white or cream. Cards use `surface-raised` with a `border` hairline.
- Text is `ink`; supporting text `ink-muted`; captions `ink-subtle`. All pass 4.5:1 on `surface` and `surface-raised` in both themes.
- UI is built with `accent`, the app's own color (see *App colors* below). `accent` fills at most one primary control per view; text on it is `on-accent`. Links and focus rings are `accent`.
- Selected rows, tags and active nav use `accent-tint` with `accent-deep` text.
- `moss` itself is the brand's color: the hanko ink, the 管狐 mon and Kudagitsune's own pages. In Kudagitsune, and in any app without a color of its own, `accent` is moss.
- `sage` and `blush` are illustration colors only (the tube, the fox's cheeks, pixel trim). Never use them for text or status.
- Success is `moss` in every app. Errors are a muted brick (`danger`), warnings a dry ochre (`warning`). No pure red, yellow or bright green anywhere.
- Dark mode is a warm, slightly green near-black (`surface` `#1C1E1B`) with a lighter moss (`#8FB08F`). It should feel like the same room at night, not a different app. Every app color has a lighter dark-mode value too.

### App colors

Each app takes one color from this palette. The colors are traditional Japanese ones, matched in depth so no app is louder than another, and every one passes 4.5:1 for text on it and for links on `surface`, in both themes.

| Color | Light | Dark | App |
| --- | --- | --- | --- |
| 苔 `moss` | `#4E6B4F` | `#8FB08F` | Kudagitsune itself |
| 朱 `shu` | `#B0501F` | `#EBA57E` | Kikitori |
| 藍 `ai` | `#3B5878` | `#93AACB` | The file manager (working name *Explorer*) |
| 葡萄 `budo` | `#6E4C6E` | `#C29FC2` | Free for the next app |
| 鉄 `tetsu` | `#2F6265` | `#86B7B5` | Free for the next app |

- Each color has the same five tokens as moss: `shu`, `shu-hover`, `shu-deep`, `shu-tint`, `on-shu` and so on. Apps don't use them by name; they point `accent` at their color.
- One color per app, never two in one app. A new color must keep the same depth, pass the same contrast checks and stay clearly apart from `danger` (brick) and `warning` (ochre).
- 朱 sits between `danger` and `warning`. In a 朱 app an error is never shown by color alone: it always says what went wrong in words, as the voice rules already ask.

## Type

- **Zen Kaku Gothic New** for everything in the UI, Japanese and English. It is warm, slightly rounded and has no trendy serif signal. Weights 400 and 500 only; 700 belongs to the hanko lettering and never appears in UI text.
- **IBM Plex Mono** for numbers that should line up, versions and code.
- **Zen Old Mincho** only inside hanko-style marks. Never for UI copy.
- Body text is 16px with a 27px line height. Do not tighten it — the air is part of the brand.
- Sentence case everywhere. Japanese-first apps write Japanese UI; English labels are not mixed in for style.

## Space and shape

- 4px base: `space-1` (4) through `space-16` (64). Phone gutters are `space-4`; card padding `space-6`; sections `space-8`. When unsure, add space.
- Corners: `radius-md` (8px) for controls, `radius-lg` (12px) for cards, `radius-seal` (14px) only for the square hanko.
- No shadows except `shadow-float` on menus that float over content. Borders are 1px `border`.
- Motion is short (150–200ms) and functional: things fade or slide because they changed. No looping or decorative animation.

## The marks

| Mark | File | Use it for | Minimum size |
| --- | --- | --- | --- |
| Square hanko (primary) | `marks/hanko-square.svg` | About pages, READMEs, store screenshots, the "made by" signature | 32px tall |
| Round hanko (compact) | `marks/hanko-round.svg` | Favicons, profile pictures, footers, small corners | 20px |

- The hanko is a **single-ink stamp**. The cut-out parts are transparent, so it works on any background. Use the `moss` ink on light grounds and the `marks/*-on-dark` files (lighter moss) on dark grounds.
- Keep clear space of at least a quarter of the mark's width on every side.
- Don't recolor it to anything but the two moss inks, don't rotate, stretch or outline it, don't add shadows, glow or texture, and don't put it on a busy photo.
- The kanji 管狐 are drawn as shapes inside the square hanko; never retype them in another font.

## The mon (app icons)

Every app has a 家紋, a mon: one shape in one color inside the shared ring, the way a Japanese family crest is drawn. The ring and the drawing style make the apps one family; the shape and the color tell them apart. Mons have no letters or kanji, so they read the same in any language.

| App | Mon | Color | Files |
| --- | --- | --- | --- |
| Kudagitsune | 丸に管狐 — the fox looking out of its bamboo tube, as on the hanko | 苔 moss | `mon/kudagitsune*.svg`, `icons/kudagitsune/` |
| Kikitori | 丸に波に千鳥 — a plover over a wave; the wave is Kikitori's recording line | 朱 shu | `mon/kikitori*.svg`, `icons/kikitori/` |
| File manager (working name *Explorer*) | 丸に入れ子枡 — measuring boxes inside each other, as folders inside folders | 藍 ai | `mon/explorer*.svg`, `icons/explorer/` |

- **Files.** `mon/<app>.svg` is the mon in the app's color, `-on-dark` in its dark-mode color and `-ink` in ink for print and one-color uses. Cut-outs are transparent. Below 32px use the `-small` files: the same outline with a heavier ring and without the cut-outs too fine to see.
- **App icons.** `icons/<app>/` holds the mon on a paper disc, so it reads on light and dark taskbars alike: `icon.svg`, PNGs from 16 to 1024px (24px and down use the small drawing), a Windows `icon.ico` with every size drawn for its size, and `app-icon-1024.png`, an opaque square on the warm ground for stores and iOS.
- **Tray and menu bar.** Use `mon/<app>-small-ink.svg` on light taskbars and `-small-on-dark.svg` on dark ones.
- **One color, flat.** Never two colors, gradients, outlines, shadows or texture. Don't rotate or stretch a mon, and don't take it out of its ring except at small sizes.
- **Black-and-white test.** Every mon must be recognisable in solid black at 16px and must not be confused with any other app's mon. Check this before adding one.
- **A new app's mon** is a traditional motif, or the app's own idea drawn the same way: filled shapes, cut-outs instead of lines, about 70% of the ring's width. No letters. Add it to `tools/build_mon.py`, run it, and add the app to `tokens/tokens.json` → `apps`.
- `tools/build_mon.py` draws every mon file and icon; change shapes or colors there and rebuild, never edit the outputs by hand.

## The fox (mascot)

The pixel kudagitsune is the character that lives inside the apps. It always sits in its tube.

| Pose | File | When |
| --- | --- | --- |
| Standard | `mascot/fox-pixel.svg` | Empty states, success, the about page |
| Shy peek | `mascot/fox-pixel-shy.svg` | Loading, waiting, "nothing here yet" |
| Sleeping | `mascot/fox-pixel-sleeping.svg` | Offline, idle, nothing to do, night |

- Scale only in **whole-pixel multiples** (the art is 14 × 22 pixels: show it at 28 × 44, 42 × 66, 56 × 88…) and render with `image-rendering: pixelated` so edges stay crisp.
- One fox per screen, at most. It sits at an edge or above an empty-state message, never over content or controls.
- The fox uses only brand colors. New poses must reuse the same 14-pixel-wide head, the same palette and the tube.
- The fox never speaks in speech bubbles and never blocks a task. If removing it would make the screen unclear, the screen needs better words, not a bigger fox.

## Voice

Plain, calm and brief, like a considerate friend. Say what happened and what to do next. No exclamation marks in system messages, no "successfully", no jokes in error messages. Empty states may have a little warmth (the fox is there), but stay one sentence.

- Good: 「まだ記録がありません。最初の一行を書いてみましょう。」 / "No entries yet. Write your first line."
- Avoid: "Oops!! Nothing here 😢 Let's get started!!!"

`AGENTS.md` has more examples, for saving, errors, going offline and confirming a delete.

## Using this on each platform

The brand lives in the accent color, the mon, type, empty states and words. Native controls stay native: on iOS use system navigation and sheets tinted with the app's `accent`; on Windows use standard window chrome; on the web build with these tokens directly. Never fight the platform to look "on brand".

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

All three are free (SIL Open Font License) on Google Fonts:

- [Zen Kaku Gothic New](https://fonts.google.com/specimen/Zen+Kaku+Gothic+New) — weights 400, 500
- [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) — weight 400
- [Zen Old Mincho](https://fonts.google.com/specimen/Zen+Old+Mincho) — weight 700, hanko text only

`tokens/tokens.css` already imports them. In native apps, bundle the font files from Google Fonts.

## Files in this kit

| Folder | What's inside |
| --- | --- |
| `marks/` | Both hanko as SVG (use these whenever you can) and PNG at 64, 256 and 1024px tall, in moss ink and the `-on-dark` lighter ink. Cut-outs are transparent. |
| `mascot/` | The pixel fox in three poses as SVG, plus crisp PNGs at 2×, 3×, 4× and 8×. |
| `mon/` | Each app's mon as SVG: in its color, `-on-dark` and `-ink`, each also as `-small` for 24px and down. Cut-outs are transparent. |
| `icons/` | One folder per app with its app icon: SVG, PNGs from 16 to 1024px, a Windows `.ico` and a store icon. At the top, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon-180.png` and `app-icon-1024.png` are the 管狐 mon for the brand's own pages. |
| `tools/build_mon.py` | Draws every file in `mon/` and `icons/` from one set of shapes (`pip install resvg-py pillow`, then `python tools/build_mon.py`). |
| `tokens/tokens.css` | CSS custom properties for web projects. Light by default, dark via the system setting or `data-theme="dark"`. |
| `tokens/tokens.ts` | The same values as a plain object for React, React Native and Expo. |
| `tokens/tokens.json` | The source of truth, with a usage note on every token. |
| `AGENTS.md` | The rules from this guide, condensed for coding agents, with more voice examples and a check to run before finishing UI work. |

## Using it in a project

Copy this folder into a repo as `brand/`. Then:

- **Web:** `@import "brand/tokens/tokens.css";`, put the app's id on the root element (`<html data-app="kikitori">`) and build with `var(--accent)`, `var(--space-6)` and so on. Kudagitsune itself needs no `data-app`; its accent is moss.
- **React Native / Expo:** `import { appColors } from "./brand/tokens/tokens";` and use `appColors("kikitori", "light")` (or `"dark"`, from the system color scheme). It returns every color with `accent` set to the app's own.
- **App icon:** take `icons/<app>/` as the app's icon set; for Tauri, point `tauri icon` at `icons/<app>/icon-1024.png` and replace the `.ico` it writes with `icons/<app>/icon.ico`, which draws the small sizes properly.
- **Coding agents:** put the line `@brand/AGENTS.md` in the app's root `CLAUDE.md` so Claude Code loads the rules at the start of every session. Asking an agent in words to read a file only works if it decides to open it, and a file inside `brand/` is never loaded on its own. For other agents, add "Before touching UI, read `brand/AGENTS.md`." to their instruction file. If you change a rule, change it in both this README and `AGENTS.md`.
