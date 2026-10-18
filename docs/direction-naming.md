# Direction: how apps are named

Status: adopted 2026-10-18. Every app is named after its logo motif, with a plain descriptor as a subtitle. The rules are in `README.md` (*Naming apps*) and the brand-ui skill (*Naming*). This page is the record of how that was decided. No app has been renamed yet.

## Where the names stood

The projects had three kinds of names:

- **Japanese phrases for the task:** Kikitori (聞き取り), Itsukaeru (いつ帰る), データ日記 and シミュってみた.
- **English names:** Redress, Agent hub, and all-i-need, the file manager, which the kit calls Explorer.
- **Generic project names:** infinite-evolution, magic-game and ai-world-platform.

The first kind already sounded like a family, but nothing tied any of them to the logos.

## The options

| | Convention | Example | Why not, or why |
|---|---|---|---|
| A | A compound-verb noun for what you do with the app (聞く + 取る → 聞き取り) | Kikitori, Hikidashi, Kisekae | Clear and pleasant, but words like these are already common as app names. |
| **B** | **The motif's crest name, with a plain descriptor** | **Chidori — 文字起こし** | **Chosen.** The name matches the logo exactly, and choosing the motif and naming the app become one decision. On its own the name says little, so the descriptor carries the meaning. |
| C | The brand's name plus a plain noun | Tajiri Notes | Clear, but corporate for a family of personal tools. |

## How the descriptor attaches

- **B1, always together:** "Chidori 文字起こし" everywhere, like Notion Calendar. Clear, but long in a taskbar or window title.
- **B2, as a subtitle (chosen):** the name alone where space is tight or the app is already open. The name with its descriptor where someone meets the app for the first time: the store listing, About, the README title, the website and first run.

## Choosing a descriptor

The descriptor is the word people search for, not the cleverest one. For Kikitori, which writes meetings, lectures and videos down live, 文字起こし / Transcription fits best. Audio memo (音声メモ) sounds like recording yourself, 会議メモ leaves out lectures and videos, and 議事録 sounds business-only.

## Open

- **Kikitori's rename** is planned, probably to Chidori — 文字起こし, the plover already in its logo. Until then the kit keeps the name Kikitori.
- **Explorer** is still a working name. Under this convention it would be named after its motif, 入れ子枡. Masu is the short form, but ます is also the polite verb ending in Japanese, so check how it reads before adopting it.
- **Name checks.** Crest names are ordinary words: Chidori is well known from Naruto, and Kitsune is used widely. Check each name in its own store category before adopting it.
- **A `descriptor` field** in `tokens/tokens.json` → `apps` would give agents one place to read it from. For now it lives in each app's README.
