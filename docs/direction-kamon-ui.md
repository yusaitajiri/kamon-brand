# Direction: how much of the kamon goes into UI elements

Status: exploring, not adopted. Written 2026-10-17. `ui/ui.css` has the plain elements, which follow the existing rules, and two opt-in kamon touches that nothing uses yet.

## The two touches

The logo is the 木瓜 frame, so the elements borrow its two details rather than the whole crest:

- **Scooped corners** (`.kamon-corners`): corners curved inward, like the notches between the frame's lobes. CSS `corner-shape: scoop`. Chrome and Edge draw it today; Safari and Firefox show ordinary rounded corners instead, so it can only ever be extra.
- **An inner line** (`.kamon-line`): a thin second line just inside the edge, like the frame's own inner line. It is drawn with an inset `box-shadow`, used as a line, not as depth.

`ui/elements.html` shows each element plain and with each touch (screenshots: `ui/screens/elements-light.png`, `elements-dark.png`).

![Elements, plain and with the kamon touches](../ui/screens/elements-light.png)

## Four densities

`ui/mock.html` is one sample screen in Kikitori's color, four times (screenshots: `ui/screens/density-light.png`, `density-dark.png`):

![The same screen at four densities of the kamon](../ui/screens/density-light.png)

| Density | What carries the kamon | How it reads |
|---|---|---|
| Logo only | The logo in the header | Calm and clean, but nothing but the icon says which family the app is from. |
| **At the edges** | The logo, the one primary button per view, and the empty state's mark | The primary button reads like a seal pressed on the page: one stamp per view, on the action that matters. Everything you type into or read stays plain. |
| Shape language | Scooped corners on every button, input, tag and card; the inner line on the primary | Cards and inputs start to look like tickets and coupons. The notches pull the eye to the corners of everything, and the primary no longer stands apart. |
| Everywhere | Corners and inner lines on everything, a small kamon beside each section title | Busy. Double lines everywhere turn into texture, and the small marks dilute the logo. |

## What the drawings show

- **Kamon is a seal, so use it like one.** A crest marks one thing. The touches work where there is one of something in a view: the primary action, the logo, the empty state. Repeated on every element, they stop meaning anything.
- **That matches a rule we already have.** `accent` fills at most one primary control per view. If the primary is also the only kamon-styled control, the two signals point at the same place.
- **Not on small or repeated elements.** A scooped checkbox reads as a plus sign; scooped tags and list rows look like price labels. Leave checkboxes, switches, tags, rows and inputs plain.
- **The inner line carries it where the corners can't.** Without `corner-shape` (Safari, Firefox), the inner line alone still marks the primary, so it is the safer of the two touches.
- **Native controls stay native.** On iOS and in Windows chrome the primary is the platform's own button tinted with `accent`; the kamon button is for the web and our own desktop UI.

Lean: **at the edges.** The logo, one kamon primary button per view with both touches, and the logo's mark in empty states. Nothing else.

## If adopted

1. Make `.button-primary` carry both touches itself, and remove the `.kamon-*` modifiers from the other elements.
2. Add the empty state's mark (the app's logo, 48px) to `.empty` guidance.
3. Note in `AGENTS.md` and `README.md` that the primary button's inner line is the one inset line allowed, and that it is not a shadow.
