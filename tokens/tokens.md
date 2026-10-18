# Kamon brand tokens

Generated from `tokens.json` by `tools/build_tokens_doc.py`. Don't edit this file: change `tokens.json` and rerun.

## Color

`→ name` means the token takes that token's value. An app points `accent` at its own color (see *Apps*).

| Token | Light | Dark | Usage |
| --- | --- | --- | --- |
| `surface` | `#F3F1EC` | `#1C1E1B` | Page background. The warm gray ground every app sits on — never pure white or cream. |
| `surface-raised` | `#FBFAF7` | `#252824` | Cards, sheets and popovers that sit above the page. Separate with border, not shadow. |
| `surface-sunken` | `#E9E6DF` | `#151714` | Inputs, code blocks and wells set into the page. |
| `border` | `#DCD8CF` | `#363A34` | Default hairline between areas, around cards and list rows. |
| `border-strong` | `#C2BDB2` | `#4A4F47` | Hover borders, dividers that need to read, outline buttons. |
| `ink` | `#2A2826` | `#ECE9E2` | Primary text on any surface. |
| `ink-muted` | `#5E5A53` | `#B0ABA1` | Supporting text: descriptions, metadata, secondary labels. |
| `ink-subtle` | `#6B665E` | `#99948A` | Captions, timestamps and placeholders. Still passes 4.5:1 on surface and raised. |
| `moss` | `#4E6B4F` | `#8FB08F` | The brand's own color: the brand logo and the brand's own pages. Apps use accent, which is moss unless the app brings its own color. |
| `moss-hover` | `#435E44` | `#A2BFA1` | Hover and pressed state of moss fills. |
| `moss-deep` | `#3A523C` | `#B5CDB3` | Moss as text on moss-tint (chips, selected rows) and for small brand text that needs extra contrast. |
| `moss-tint` | `#DDE5D9` | `#2C382C` | Quiet brand backgrounds: selected rows, tags, the active nav item. |
| `on-moss` | `#F7F6F1` | `#172016` | Text and icons on a moss fill. |
| `accent` | → `moss` | → `moss` | The current app's color. Primary buttons, links, focus, selected states. One accent-filled control per view. Moss by default; each app sets its own (see apps). |
| `accent-hover` | → `moss-hover` | → `moss-hover` | Hover and pressed state of accent fills. |
| `accent-deep` | → `moss-deep` | → `moss-deep` | Accent as text on accent-tint, and small accent text that needs extra contrast. |
| `accent-tint` | → `moss-tint` | → `moss-tint` | Selected rows, tags, the active nav item. |
| `on-accent` | → `on-moss` | → `on-moss` | Text and icons on an accent fill. |
| `shu` | `#B0501F` | `#EBA57E` | 朱 Shu, a muted vermilion. Kikitori's color. Use it through accent, never alongside another app color. |
| `shu-hover` | `#9A451A` | `#F0B796` | Hover and pressed state of shu fills. |
| `shu-deep` | `#7F3A16` | `#F4C9AF` | Shu as text on shu-tint. |
| `shu-tint` | `#F5E0D3` | `#3B2A20` | Quiet shu backgrounds: selected rows, tags, active nav. |
| `on-shu` | `#F7F6F1` | `#1F140D` | Text and icons on a shu fill. |
| `ai` | `#3B5878` | `#93AACB` | 藍 Ai, indigo. The file manager's color. Use it through accent, never alongside another app color. |
| `ai-hover` | `#324B66` | `#A6BAD6` | Hover and pressed state of ai fills. |
| `ai-deep` | `#2C4460` | `#BACAE0` | Ai as text on ai-tint. |
| `ai-tint` | `#DCE3EC` | `#26303B` | Quiet ai backgrounds: selected rows, tags, active nav. |
| `on-ai` | `#F7F6F1` | `#141A22` | Text and icons on a ai fill. |
| `budo` | `#6E4C6E` | `#C29FC2` | 葡萄 Budō, grape. Free for the next app. Use it through accent, never alongside another app color. |
| `budo-hover` | `#5F415F` | `#CDB0CD` | Hover and pressed state of budo fills. |
| `budo-deep` | `#553A55` | `#D8C1D8` | Budo as text on budo-tint. |
| `budo-tint` | `#E8DEE7` | `#33293A` | Quiet budo backgrounds: selected rows, tags, active nav. |
| `on-budo` | `#F7F6F1` | `#1E161E` | Text and icons on a budo fill. |
| `tetsu` | `#2F6265` | `#86B7B5` | 鉄 Tetsu, iron teal. Free for the next app. Use it through accent, never alongside another app color. |
| `tetsu-hover` | `#285457` | `#9AC4C2` | Hover and pressed state of tetsu fills. |
| `tetsu-deep` | `#224A4C` | `#AED1CF` | Tetsu as text on tetsu-tint. |
| `tetsu-tint` | `#D7E6E5` | `#223434` | Quiet tetsu backgrounds: selected rows, tags, active nav. |
| `on-tetsu` | `#F7F6F1` | `#122020` | Text and icons on a tetsu fill. |
| `sage` | `#C3CFBF` | `#4C5C4A` | Decorative only: illustration fills. Never text or status. |
| `blush` | `#E3B7A6` | `#C99A8A` | Decorative only: rare warm accents in illustrations. Never text or status. |
| `danger` | `#A3473A` | `#E39A8C` | Errors and destructive actions. A muted brick, not alarm red. |
| `danger-tint` | `#F3E1DC` | `#3A2622` | Background of error messages; pair with danger text. |
| `success` | → `moss` | → `moss` | Success uses the brand moss — there is no separate green. |
| `warning` | `#80591A` | `#D9B46A` | Warnings. A dry ochre, never yellow-on-white. |
| `warning-tint` | `#F4EAD6` | `#3A311F` | Background of warnings; pair with warning text. |

## Apps

Each app brings one color from the palette and its own motif inside the shared 木瓜 frame. Set accent to the app's color; everything else is shared.

| App id | Name | Color | Motif |
| --- | --- | --- | --- |
| `brand` | Brand | `moss` | 狐: a fox's head. The brand's own logo, for its pages and anything without an app of its own. |
| `kikitori` | Kikitori | `shu` | 千鳥: the plover of 波に千鳥. |
| `explorer` | Explorer (working name) | `ai` | 入れ子枡: boxes inside boxes, as folders inside folders. |

Free for the next app: `budo`, `tetsu`.

## Type

| Family | Stack |
| --- | --- |
| `font-sans` | `"Zen Kaku Gothic New", "Hiragino Sans", "Yu Gothic UI", system-ui, sans-serif` |
| `font-mono` | `"IBM Plex Mono", ui-monospace, "SF Mono", Menlo, monospace` |

| Style | Family | Size / line height | Weight | Usage |
| --- | --- | --- | --- | --- |
| `display` | sans | 40px / 48px | 500 | One per screen at most: onboarding, empty-state headlines, about pages. |
| `title` | sans | 28px / 36px | 500 | Screen titles. |
| `heading` | sans | 20px / 28px | 500 | Section headings inside a screen. |
| `body` | sans | 16px / 27px | 400 | Default reading text. Generous line height is part of the calm. |
| `body-small` | sans | 14px / 22px | 400 | Dense UI, list secondary lines, helper text. |
| `label` | sans | 14px / 20px | 500 | Buttons, tabs, form labels. |
| `caption` | sans | 12px / 18px | 400 | Timestamps and metadata, in ink-subtle. |
| `mono` | mono | 13px / 20px | 400 | Numbers that line up, versions, code. |

## Spacing

| Token | Value | Usage |
| --- | --- | --- |
| `space-1` | 4px | Icon-to-label gaps, tight inline spacing. |
| `space-2` | 8px | Between related controls; chip padding. |
| `space-3` | 12px | List row vertical padding; gap in button groups. |
| `space-4` | 16px | Screen side gutter on phones; card padding (compact). |
| `space-6` | 24px | Card padding; gap between cards. |
| `space-8` | 32px | Between sections inside a screen. |
| `space-12` | 48px | Around empty states and major page breaks. When unsure, use more space, not less. |
| `space-16` | 64px | Top of pages and hero areas on desktop. |

## Radius

| Token | Value | Usage |
| --- | --- | --- |
| `radius-sm` | 6px | Chips, tags, small inputs. |
| `radius-md` | 8px | Buttons, inputs, list highlights. The default. |
| `radius-lg` | 12px | Cards, sheets, dialogs. |
| `radius-full` | 9999px | Avatars only. |

## Shadow

Depth comes from borders and surfaces, not shadows. One flat shadow exists for floating menus only.

| Token | Light | Dark | Usage |
| --- | --- | --- | --- |
| `shadow-float` | `0 4px 16px rgba(42,40,38,0.08)` | `0 4px 16px rgba(0,0,0,0.4)` | Menus and popovers that float over content. Nothing else. |
