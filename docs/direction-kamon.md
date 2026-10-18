# Direction: the kamon and its double line

Status: adopted 2026-10-18. Every logo is the 木瓜 frame with the app's motif inside, and inside the UI the kamon appears only as the frame's double line, in three forms. The rules are in `rules/brand.md` and `README.md`; this page says why.

## What the brand wants

- The UI stays standard and calm. The brand is subtle, not a new visual language.
- The apps still read as one family, the way a row of tiles in one frame does: one shared frame, one color and one symbol per app.
- Clean and polished. Not neon, flashy or cluttered, and no imitation materials.

## The logo: a kamon in the 木瓜 frame

A kamon (家紋) is a simple motif inside a frame, flat and in one color: exactly a shared frame with a symbol per app. The logos take that structure without its formality, with thicker strokes and rounded joins, and each motif reduced to 3–5 simple shapes.

- **Four lobes (木瓜).** It is unmistakably kamon and looks like no other app frame. Hexagons were the alternative, but they read as developer stickers or crypto tokens, and a plain circle makes an icon look like any other app. Four is the standard 木瓜 crest: five lobes read as a blossom and three as a clover.
- **A band with a thin line inside it.** The classic 木瓜 crest is drawn as a double outline, so the inner line is the authentic detail. A ring outside it would be the separate 丸に木瓜 crest and make the icon read as a circle. The line is kept slim (a 6-unit band, a 3-unit gap and a 3-unit line on the 140 grid) to leave the motif room.
- **Small sizes.** Below 24px the inner line would be under a pixel, so the small drawing has one heavier band, a wider gap and the motif without its fine cut-outs. At 16px the motif is a few pixels and apps are told apart mostly by color.

`tools/build_logo.py` has the exact geometry.

## In the UI: only the double line

A crest is a seal: it marks one thing. Repeated on every element, any detail of it turns into texture, and cards and inputs start to look like tickets. So the UI takes one detail of the frame, its double line, and only where there is one of something in a view:

- **The primary button** has a 1px line 3px inside its edge, the frame's inner line. It matches the rule that `accent` fills one control per view, so the color and the kamon point at the same place.
- **The rule (子持ち罫)**, a thick line over a thin one, marks the top of the screen under the app bar. In print a 子持ち罫 marks the top of a page, and the thick line goes on top or outside, so it has a direction and loses its meaning when it repeats.
- **The frame**, a band, a gap and a thin line in the logo's proportions, goes on the one container being worked in: an editor, an edit panel, a dialog. It says where the work is.

The rule and the frame are neutral `border-strong`, never `accent`, so the accent still marks only what can be acted on. Everything else, inputs, tags, checkboxes and list rows, stays plain.

## Density: one rule, one frame, one primary

Screens were compared at four densities: one rule only; one rule plus one frame; rules after every section title; and the double line everywhere. One of each is the default:

- **Rules on sections are too much.** Each rule lands just above a card's top edge, stacking lines, and competes with the frame.
- **Frames on every card make a form full of boxes.** Nothing stands out, and a dialog's frame merges with the ones behind it.
- **Views of equal sections need no frame.** Home, boards, settings and file browsers look finished with only the rule. On a board the frame first appears when an item opens, which makes the panel read as where the work moved.
- **A frame on a preview pulls the eye the wrong way.** In a file manager the work is the file list, and a framed preview became the loudest thing on screen. Hence the test: a container you work in, not one that shows something.
- **Never two frames.** When a dialog or panel opens, the frame and the primary move to it.
- **The rule and the frame never touch.** A heading or at least `space-6` between them keeps them from reading as one stack of lines.
- **A framed dialog keeps its float shadow.** It floats, so it has both cues.
- **Fixed weights.** The frame's lines are fixed pixels, so a large editor pane looks as calm as a phone card.

Lighter is always fine. Denser is what to avoid.

These points match what design guidance says about rules and borders:

- Rules support the content and shouldn't compete with it: keep them thin, remove the ones you don't need, and let white space separate where it can. 子持ち罫 makes a hierarchy through the contrast in weight ([Adobe](https://www.adobe.com/jp/creativecloud/roc/blog/design/quiz-challenge/rule-line.html)).
- The thick line goes outside or on top ([DDC printing glossary](https://www.ddc.co.jp/words/archives/20260824173237.html)).
- No divider where margin already separates, and none inside cards, tiles or dialogs, which already separate their content ([Volvo](https://designsystem.volvocars.com/web/components/divider/usage/), [Toyota](https://dx-playbook-prev.toyota-europe.com/cds/components/divider/)). Borders used to group everything become noise ([Andrew Coyle](https://coyleandrew.medium.com/8-rules-to-help-you-design-a-better-card-user-interface-a239257d633d)).

## Native apps

The inner line, the frame and the rule are for the brand's own UI. iOS, Windows and Flutter's native widgets keep their own buttons and containers, tinted with `accent`.
