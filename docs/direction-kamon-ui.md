# Direction: how much of the kamon goes into UI elements

Status: adopted 2026-10-17, at the edges. The kamon reaches into the UI only through the primary button, the one action per view, plus the logo and the empty state's mark. `ui/ui.css` draws it; the rules are in `AGENTS.md` and `README.md`. This page is the record of how that was decided.

## The two details

The logo is the 木瓜 frame, so elements borrow two of its details rather than the whole crest:

- **The notch.** Where two of the frame's lobes meet, two outward quarter circles come together at an inward point. On a rectangle that is the outline of a wide and a tall rounded rectangle overlapping: at each corner, two small lobes and a notch between them.
- **The inner line.** A thin second line just inside the edge, following the same outline, like the frame's inner line.

## Four densities

The study put one sample screen in Kikitori's color at four densities (`docs/kamon-ui/density-light.png`, `density-dark.png`). It was drawn with the first attempt at the corner, described below.

![The same screen at four densities of the kamon](kamon-ui/density-light.png)

| Density | What carries the kamon | How it reads |
|---|---|---|
| Logo only | The logo in the header | Calm and clean, but nothing but the icon says which family the app is from. |
| **At the edges (adopted)** | The logo, the one primary button per view, and the empty state's mark | The primary button reads like a seal pressed on the page: one stamp per view, on the action that matters. Everything you type into or read stays plain. |
| Shape language | The corners on every button, input, tag and card; the inner line on the primary | Cards and inputs start to look like tickets and coupons, and the primary no longer stands apart. |
| Everywhere | Corners and inner lines on everything, a small kamon beside each section title | Busy. Double lines everywhere turn into texture, and the small marks dilute the logo. |

- **A kamon is a seal, so use it like one.** A crest marks one thing. The details work where there is one of something in a view: the primary action, the logo, the empty state.
- **It matches a rule we already have.** `accent` fills at most one primary control per view, so the color and the kamon point at the same place.
- **Not on small or repeated elements.** With the corner on them, checkboxes read as plus signs and tags as price labels.

## The corner, corrected

The first attempt used CSS `corner-shape: scoop`: one concave arc cut into each corner. That is a ticket stub's corner, not the crest's, and it is a large part of why the denser screens looked like tickets (`docs/kamon-ui/scooped-elements-light.png`). The 木瓜 notch is the opposite: two convex quarter circles meeting at an inward point.

The adopted button draws that outline with `clip-path: shape()`, which follows the button at any size. The fill and the inner line are two layers behind the label, so the focus ring is untouched and no shadow is involved. `shape()` works in current Chrome, Edge and Safari; a browser without it shows the plain primary button.

![The primary button's corner enlarged beside the logo](../ui/screens/elements-light.png)

## Where it does not apply

Native controls stay native. On iOS and in Windows chrome the primary is the platform's own button tinted with `accent`; the kamon button is for the web and the brand's own desktop UI.
