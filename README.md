# Kudagitsune

The personal brand for every app Yusai Tajiri makes. A calm, warm-gray interface tinted with one moss green, signed with a hanko, and kept company by a tiny fox that lives in a bamboo tube.

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

## Principles

1. **Calm first.** Generous spacing, a warm gray ground, plain words. Nothing in the UI competes for attention.
2. **One color, used with intent.** Moss is the only brand hue. It marks what you can act on and what is selected — not decoration.
3. **Personality lives at the edges.** The working UI stays normal and native. The fox and the hanko appear in empty states, loading, success moments, the about page and the app icon — never in the middle of a task.
4. **Made, not copied.** No imitation paper, wood, glass or metal. Surfaces are flat; depth comes from borders and spacing.

What this brand is **not**: neon or glow, neumorphic soft-3D, "light show" effects (animated gradients, blur, sparkle), brutalism (raw borders, clashing color, shouting type), or skeuomorphic objects. If a choice leans toward any of these, pick the quieter option.

## Color

- Ground is `surface` (warm gray `#F3F1EC`), never pure white or cream. Cards use `surface-raised` with a `border` hairline.
- Text is `ink`; supporting text `ink-muted`; captions `ink-subtle`. All pass 4.5:1 on `surface` and `surface-raised` in both themes.
- `moss` fills at most one primary control per view; text on it is `on-moss`. Links and focus rings are `moss`.
- Selected rows, tags and active nav use `moss-tint` with `moss-deep` text.
- `sage` and `blush` are illustration colors only (the tube, the fox's cheeks, pixel trim). Never use them for text or status.
- Success is `moss`. Errors are a muted brick (`danger`), warnings a dry ochre (`warning`). No pure red, yellow or bright green anywhere.
- Dark mode is a warm, slightly green near-black (`surface` `#1C1E1B`) with a lighter moss (`#8FB08F`). It should feel like the same room at night, not a different app.

## Type

- **Zen Kaku Gothic New** for everything in the UI, Japanese and English. It is warm, slightly rounded and has no trendy serif signal. Weights 400 and 500 only; 700 is reserved.
- **IBM Plex Mono** for numbers that should line up, versions and code.
- **Zen Old Mincho** only inside hanko-style marks. Never for UI copy.
- Body text is 16px with a 27px line height. Do not tighten it — the air is part of the brand.
- Sentence case everywhere. Japanese-first apps write Japanese UI; English labels are not mixed in for style.

## Space and shape

- 4px base: `space-1` (4) through `space-16` (64). Phone gutters are `space-4`; card padding `space-6`; sections `space-8`. When unsure, add space.
- Corners: `radius-md` (8px) for controls, `radius-lg` (12px) for cards, `radius-seal` (14px) only for the square hanko and the app icon.
- No shadows except `shadow-float` on menus that float over content. Borders are 1px `border`.
- Motion is short (150–200ms) and functional: things fade or slide because they changed. No looping or decorative animation.

## The marks

| Mark | File | Use it for | Minimum size |
| --- | --- | --- | --- |
| Square hanko (primary) | `marks/hanko-square.svg` | About pages, READMEs, store screenshots, the "made by" signature, app icons | 32px tall |
| Round hanko (compact) | `marks/hanko-round.svg` | Favicons, profile pictures, footers, small corners | 20px |

- The hanko is a **single-ink stamp**. The cut-out parts are transparent, so it works on any background. Use the `moss` ink on light grounds and the `marks/*-on-dark` files (lighter moss) on dark grounds.
- Keep clear space of at least a quarter of the mark's width on every side.
- Don't recolor it to anything but the two moss inks, don't rotate, stretch or outline it, don't add shadows, glow or texture, and don't put it on a busy photo.
- The kanji 管狐 are drawn as shapes inside the square hanko; never retype them in another font.

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

## Using this on each platform

The brand lives in the accent color, app icon, type, empty states and words. Native controls stay native: on iOS use system navigation and sheets tinted `moss`; on Windows use standard window chrome; on the web build with these tokens directly. Never fight the platform to look "on brand".

## Colors at a glance

| Token | Light | Dark |
| --- | --- | --- |
| `surface` | `#F3F1EC` | `#1C1E1B` |
| `surface-raised` | `#FBFAF7` | `#252824` |
| `ink` | `#2A2826` | `#ECE9E2` |
| `ink-muted` | `#5E5A53` | `#B0ABA1` |
| `moss` | `#4E6B4F` | `#8FB08F` |
| `moss-tint` | `#DDE5D9` | `#2C382C` |
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
| `icons/` | `favicon-32.png` and `favicon-192.png` (round hanko), `apple-touch-icon-180.png` and `app-icon-1024.png` (fox on the warm ground, ready for an app store icon). |
| `tokens/tokens.css` | CSS custom properties for web projects. Light by default, dark via the system setting or `data-theme="dark"`. |
| `tokens/tokens.ts` | The same values as a plain object for React, React Native and Expo. |
| `tokens/tokens.json` | The source of truth, with a usage note on every token. |

## Using it in a project

Copy this folder into a repo as `brand/`. Then:

- **Web:** `@import "brand/tokens/tokens.css";` and build with `var(--moss)`, `var(--space-6)` and so on.
- **React Native / Expo:** `import { kudagitsune } from "./brand/tokens/tokens";` and pick `kudagitsune.color.light` or `.dark` from the system color scheme.
- **Coding agents:** tell the agent to read `brand/README.md` before touching UI. Everything it needs — rules, tokens and assets — is in this folder.
