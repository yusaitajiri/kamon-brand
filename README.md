# The kamon brand

The personal brand for every app Yusai Tajiri makes: a calm, warm-gray interface and a family of logos. Every logo is a kamon (家紋), a Japanese family crest: the same four-lobed 木瓜 frame in every app, with a different motif inside for each one, an animal or an object that says what the app is for. Each app's logo is in its own color, so a row of them reads as one family and each one is easy to find.

That is the idea of the brand: the apps are ordinary, well-made tools that share one frame, and each one shows its own face.

<p>
  <img src="logo/brand.svg" height="96" alt="Brand logo: a fox's head inside a four-lobed crest frame, in moss">
  &nbsp;&nbsp;
  <img src="logo/kikitori.svg" height="96" alt="Kikitori logo: a plover inside the same frame, in vermilion">
  &nbsp;&nbsp;
  <img src="logo/explorer.svg" height="96" alt="File manager logo: nested measuring boxes inside the same frame, in indigo">
</p>

## Principles

1. **Calm first.** Generous spacing, a warm gray ground, plain words. Nothing in the UI competes for attention.
2. **One color per app, used with intent.** Moss is the brand's own color. Each app brings one color of its own and uses it the way the brand uses moss: to mark what you can act on and what is selected — not decoration. Everything else is shared.
3. **Personality lives at the edges.** The working UI stays normal and native. The logo is the app icon and belongs on the about page and the brand's own pages — never in the middle of a task. Inside the working UI the kamon is only its double line, a few neutral lines, never the crest itself.
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
- Each type style is a token: `display`, `title`, `heading`, `body`, `body-small`, `label`, `caption` and `mono`. Each kit exposes them in its platform's form, such as `font: var(--text-body)` on the web.
- Sentence case everywhere. Japanese-first apps write Japanese UI; English labels are not mixed in for style.

## Space and shape

- 4px base: `space-1` (4) through `space-16` (64). Phone gutters are `space-4`; card padding `space-6`; sections `space-8`. When unsure, add space.
- Corners: `radius-md` (8px) for controls, `radius-lg` (12px) for cards, `radius-sm` (6px) for chips and tags. `radius-full` only for avatars.
- No shadows except `shadow-float` on menus and dialogs that float over content. Borders are 1px `border`, except the frame and the rule below.
- **The kamon in the UI.** A crest marks one thing, so the kamon reaches into the interface only as its double line, the 木瓜 frame's double outline, in three forms. The primary button, the one action per view, has a thin line just inside its edge. A 子持ち罫 rule, a thick line over a thin one, goes under the app bar. And a container you are working in, an editor, an edit panel or a dialog, can take a frame in the logo's proportions: a band, a gap and a thin line. The rule and the frame are neutral border colors, so the accent still marks only what you can act on. The recommended density is one of each per view: one rule, one frame, one primary, with no frame on views of equal parts such as lists, boards and settings. It's a default, not a law. Lighter is fine, but rules on every section or frames on several cards turn the line into texture, and a view never shows two frames: when a dialog or panel opens, the frame and the primary move to it. Every other element stays plain, and empty states may show the app's logo above their sentence. `docs/direction-kamon.md` has the reasoning behind this.
- Motion is short (150–200ms) and functional: things fade or slide because they changed. No looping or decorative animation.

## The logos (app icons)

Every app has a logo drawn in one flat color, built like a kamon (家紋): a simple motif inside a frame. The frame is the same in every app: 木瓜, four lobes a little wider than tall, drawn as a band with a thin line inside it, the double outline of the classic crest. Only the motif inside changes from app to app, an animal or an object reduced to a few simple shapes. The shared frame makes the apps one family; the motif and the color tell them apart. The logos have no letters or kanji, so they read the same in any language.

| App | Motif | Color | Files |
| --- | --- | --- | --- |
| The brand itself | 狐 — a fox's head, for the brand's own pages and anything without an app of its own | 苔 moss | `logo/brand*.svg`, `icons/brand/` |
| Kikitori | 千鳥 — the plover of 波に千鳥 | 朱 shu | `logo/kikitori*.svg`, `icons/kikitori/` |
| File manager (working name *Explorer*) | 入れ子枡 — measuring boxes inside each other, as folders inside folders | 藍 ai | `logo/explorer*.svg`, `icons/explorer/` |

- **Files.** `logo/<app>.svg` is the logo in the app's color, `-on-dark` in its dark-mode color and `-ink` in ink for print and one-color uses. Each is one filled path and its cut-outs are transparent. Below 32px use the `-small` files: the same logo with one heavier band instead of the band and inner line, a wider gap and the motif without the cut-outs too fine to see.
- **App icons.** `icons/<app>/` holds the logo with its frame filled with paper, so it reads on light and dark taskbars alike and keeps the frame's own outline: `icon.svg`, PNGs from 16 to 1024px (24px and down use the small drawing), a Windows `icon.ico` with every size drawn for its size, and `app-icon-1024.png`, an opaque square on the warm ground for stores and iOS.
- **Tray and menu bar.** Use `logo/<app>-small-ink.svg` on light taskbars and `-small-on-dark.svg` on dark ones.
- **One color, flat.** Never two colors, gradients, outlines, shadows or texture. Don't rotate, mirror or stretch a logo, and don't redraw the frame for one app or put it in a circle (丸に木瓜): every app shares it as it is. On iOS and Android the system masks the icon to a rounded square or circle; the store icon already sits the frame inside that on the warm ground.
- **Black-and-white test.** Every logo must be recognisable in solid black at 16px and must not be confused with any other app's logo. Check this before adding one.
- **A new app's logo** is a new motif in the same frame, and the motif also names the app (see *Naming apps* below): an animal or an object, from a traditional crest or the app's own idea, as 3–5 simple filled shapes with rounded corners and cut-outs instead of thin lines. No letters. Add it to `MOTIFS` in `tools/build_logo.py`, which sizes it to fill the frame, run it, and add the app to `tokens/tokens.json` → `apps`.
- `tools/build_logo.py` draws every logo file and icon, taking the colors from `tokens/tokens.json`. Change shapes there and colors in the tokens, then rebuild; never edit the outputs by hand.

## Naming apps

Every app is named after the motif in its logo, with a plain descriptor that says what it does. The name is the app's identity and the descriptor explains it, so choosing the motif and naming the app are one decision.

| Part | What it is | Example |
| --- | --- | --- |
| Name | The motif's crest name, in its shortest form | 千鳥 Chidori, 枡 Masu |
| Descriptor | A plain noun for the app's job, in the language of the UI | 文字起こし / Transcription, ファイル / Files |

- **Spelling the name.** Hepburn without macrons, one word, capital first letter: Chidori, not Chidōri or chidori. Japanese text writes it the way the crest is written (千鳥), with the reading in hiragana where it's hard to read.
- **The app id** is the name in lowercase (`chidori`). It picks the app's accent in each kit (`data-app` on the web), and it's the folder name in `logo/` and `icons/`, the id in `tokens/tokens.json` → `apps`, and the repository name.
- **The descriptor** is the word people would search for, one or two words in each language. Never a coined word, a slogan or the brand's name.
- **Where each appears.** The name alone wherever space is tight or the app is already open: the window title, taskbar and dock, icon label, app bar, tray tooltip and notifications. The name with its descriptor wherever someone meets the app for the first time: the store listing, the About screen, the README title, the website and the first run. Where a store has a subtitle field, the descriptor goes there. Elsewhere they're joined with a spaced em dash: "Chidori — Transcription", 「千鳥 — 文字起こし」.
- **Choosing the motif and its name.** The motif is a traditional crest subject, or an object from the app's own work, that 3–5 simple shapes can draw. Its name is short: two or three syllables, four at most. It's easy to say in English, and has no unfortunate meaning in English or Japanese. A link between the name and the job is welcome but not required.
- **Check before adopting.** Crest names are ordinary words, so search the app stores in the app's category, the web and trademark records. Chidori, for example, is well known from Naruto, and Kitsune is used widely. A clash in another category is acceptable when the descriptor sets the app apart. A clash in the same category is not.
- **The brand itself has no name.** Where it needs a label, it's the kamon brand, after its logos. The fox is its mark, not a name, and its logo files are `logo/brand*.svg`. Don't give it a name, a wordmark or a tagline.
- **Apps from before this convention.** Kikitori will be renamed, probably to Chidori — 文字起こし. Explorer is a working name. Both keep their current names in the kit until they're renamed.

`docs/direction-naming.md` has the reasoning behind this.

## Voice

Plain, calm and brief, like a considerate friend. Say what happened and what to do next. No exclamation marks in system messages, no "successfully", no jokes in error messages. Empty states may have a little warmth, but stay one sentence.

- Good: 「まだ記録がありません。最初の一行を書いてみましょう。」 / "No entries yet. Write your first line."
- Avoid: "Oops!! Nothing here 😢 Let's get started!!!"

The rules for agents (`rules/brand.md`) have more examples, for saving, errors, going offline and confirming a delete.

## Using this on each platform

The brand lives in the accent color, the logo, type, empty states and words. Native controls stay native: on iOS use system navigation and sheets tinted with the app's `accent`, on Windows standard window chrome, in Flutter Material or Cupertino widgets tinted the same way. Never fight the platform to look "on brand".

The brand at the root of this repository is the same on every platform. Next to it, each platform has a kit in its own folder that turns the brand into something an app can install:

| Kit | Folder | For | What an app gets |
| --- | --- | --- | --- |
| `@yusai/kamon-react` | `react/` | React on the web, Tauri included | The tokens as CSS and TypeScript, `ui.css`, React components with the double line built in, the logos and icons, and the `brand-ui` skill. `react/README.md` says how to use it. |
| Flutter kit | `flutter/`, later | Flutter | The tokens as Dart, a theme, widgets, the logos and icons, and the skill |

```
tokens/ logo/ icons/ rules/  ──generate──►  react/    ──tag react-vX.Y.Z──►    Tauri and web apps
                             ──generate──►  flutter/  ──tag flutter-vX.Y.Z──►  Flutter apps
```

Each kit generates its token files from `tokens/tokens.json` and builds its `brand-ui` skill from `rules/brand.md` with a part for its platform. A kit is released on its own, with its own version, changelog and tags. An app pins one kit's tag. `docs/direction-platform-kits.md` has the reasoning.

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

Every token, with its usage note, is in `tokens/tokens.md`, generated from `tokens/tokens.json`.

## Fonts

Both are free (SIL Open Font License) on Google Fonts:

- [Zen Kaku Gothic New](https://fonts.google.com/specimen/Zen+Kaku+Gothic+New) — weights 400, 500
- [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) — weight 400

The web kit loads them from Google Fonts. Native apps bundle the font files.

## Files

| File or folder | What's inside |
| --- | --- |
| `tokens/tokens.json` | The source of truth for every color, type style, space, radius and shadow, with a usage note on each, and the list of apps with their colors. The kits generate their token files from it. |
| `tokens/tokens.md` | The same tokens as tables to read, generated by `tools/build_tokens_doc.py`. |
| `rules/brand.md` | The rules from this guide, condensed for coding agents, with more voice examples and a check to run before finishing UI work. Each kit's `brand-ui` skill starts with it. |
| `logo/` | Each app's logo as SVG: in its color, `-on-dark` and `-ink`, each also as `-small` for 24px and down. Each is one filled path; cut-outs are transparent. |
| `icons/` | One folder per app with its app icon: SVG, PNGs from 16 to 1024px, a Windows `.ico` and a store icon. At the top, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon-180.png` and `app-icon-1024.png` are the brand logo for the brand's own pages. |
| `tools/` | `build_logo.py` draws every file in `logo/` and `icons/` from one set of shapes, with the geometry in `logokit.py`: `uv run tools/build_logo.py`. `build_tokens_doc.py` writes `tokens/tokens.md`. |
| `docs/` | `direction-*.md` say why the brand is the way it is: the kamon and its double line, how apps are named, and and one repository with a kit per platform. |
| `react/` | The React kit: its components, `ui.css`, demo pages and its own `README.md` and `CHANGELOG.md`. The React package's manifest, `package.json`, sits at the root because apps install it from git. |
| `CHANGELOG.md` | Points to each kit's changelog, and keeps the history of `@yusai/brand`, the package this repository used to be. |
| `LICENSE`, `TRADEMARKS.md` | MIT for the style and tools; the logos, icons and names are reserved. |
| `AGENTS.md` | Instructions for agents working here: changing the brand, the kits, releases and rebuilding. |

## Changing the brand

`AGENTS.md` has the steps. A change to the brand regenerates every kit in the same commit, then each kit is released with a new tag, and each app takes it when it upgrades its kit. Two habits keep the rules working:

- **Write each rule twice:** in this README for people and in `rules/brand.md` for agents. Also add an entry to each kit's changelog.
- **Name the stock styles you see.** When an agent's output shows a stock style that isn't in the rules' *Generic defaults to avoid*, add it to that list by name. A general "avoid a generic look" only swaps one default for another, while named patterns get followed.

## License

The style is open and the identity is reserved. The tokens, the rules, the tools and the text of these docs are under the MIT License. The logos, the app icons and the apps' names, such as Kikitori, are all rights reserved. `LICENSE` has the terms. `TRADEMARKS.md` says how to refer to the names and logos, and what a fork of one of the apps should change.
