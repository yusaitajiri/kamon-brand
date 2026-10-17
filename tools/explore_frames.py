"""Draw the candidate kamon frames from docs/direction-kamon-frame.md, with each app's motif inside.

Run from the repo root:  pip install skia-pathops resvg-py pillow && python tools/explore_frames.py

This is exploration, not the live kit: it writes only to docs/kamon-frames/, and build_logo.py still
draws the logos in logo/ and icons/. Every mark is on the same 140 x 140 grid as the logos and comes
out as one filled path: the frame as a ring with the motif inside it. The small mark, for 24px and
down, has a heavier ring, a wider gap and the motif without its cut-outs. Colors come from
tokens/tokens.json.
"""

import io
import json
import math
from pathlib import Path

import pathops
import resvg_py
from PIL import Image

from logokit import circle, grow, matrix, minus, parse, smooth, to_svg, transformed, union

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "kamon-frames"

TOKENS = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))
COLORS = {t["name"]: t["value"] for t in TOKENS["color"]["tokens"]}
APPS = {a["id"]: a for a in TOKENS["apps"]["list"]}

RING = 9  # the frame's stroke on the grid, about 2px at 32px
GAP = 7  # the least space between the motif and the ring
SMALL_RING, SMALL_GAP = 14, 9  # at 16px: a 1.6px ring and a 1px gap


# ---------------------------------------------------------------- shape helpers

def shrink(path, d):
    """The shape pulled inward by d; its concave corners come out round."""
    band = pathops.Path()
    band.addPath(path)
    band.stroke(2 * d, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
    band.convertConicsToQuads()
    return minus(path, pathops.simplify(band, fix_winding=True))


def rounded(path, convex=0.0, concave=0.0):
    """Round the shape's outward corners to `convex` and its inward corners to `concave`."""
    if concave:
        path = shrink(grow(path, concave), concave)
    if convex:
        path = grow(shrink(path, convex), convex)
    return smooth(path)


def polygon(points):
    p = pathops.Path()
    p.moveTo(*points[0])
    for q in points[1:]:
        p.lineTo(*q)
    p.close()
    return p


def even_odd(d):
    p = parse(d)
    p.fillType = pathops.FillType.EVEN_ODD
    return pathops.simplify(p, fix_winding=True)


def empty(path):
    return path.area < 0.5


# ---------------------------------------------------------------- the frames

# Both hexagons share one set of corners: flat on top, 132 wide and 112 tall, a little wider than a
# regular hexagon (114), so it sits like a nut rather than a cell.
HEX = [(4, 70), (37, 14), (103, 14), (136, 70), (103, 126), (37, 126)]


def wide_hex():
    """亀甲: the tortoise-shell hexagon, with soft corners."""
    return rounded(polygon(HEX), convex=10)


def four_lobes():
    """木瓜: four lobes, wider than tall, meeting in shallow notches."""
    lobes = union(circle(43, 70, 37), circle(97, 70, 37), circle(70, 47, 37), circle(70, 93, 37))
    return rounded(lobes, concave=3)


def inset_hex(sag=8):
    """The same hexagon with every side bowed inward by `sag`."""
    p = pathops.Path()
    p.moveTo(*HEX[0])
    for a, b in zip(HEX, HEX[1:] + HEX[:1]):
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        towards = (70 - mid[0], 70 - mid[1])
        k = 2 * sag / math.hypot(*towards)
        q = (mid[0] + towards[0] * k, mid[1] + towards[1] * k)  # control point of a quadratic
        c1 = (a[0] + 2 / 3 * (q[0] - a[0]), a[1] + 2 / 3 * (q[1] - a[1]))
        c2 = (b[0] + 2 / 3 * (q[0] - b[0]), b[1] + 2 / 3 * (q[1] - b[1]))
        p.cubicTo(*c1, *c2, *b)
    p.close()
    return rounded(pathops.simplify(p, fix_winding=True), convex=7)


FRAMES = {
    "wide-hex": dict(name="Wide hex (亀甲)", draw=wide_hex,
                     note="Calm and steady, and still a hexagon at 16px. The flat top and wider shape keep it "
                          "apart from the pointy-topped hexagons of dev tools and crypto."),
    "four-lobes": dict(name="Four lobes (木瓜)", draw=four_lobes,
                       note="The most like a real kamon and unlike any app frame. Below 24px the notches close up "
                            "and it reads as a soft rounded square."),
    "inset-hex": dict(name="Inset hex", draw=inset_hex,
                      note="The most striking: the bowed sides read as a seal or a badge more than a ninja star. "
                           "At 16px the bow is gone and it falls back to a plain hexagon."),
}


# ---------------------------------------------------------------- the motifs
# Each motif returns (shape, holes) in its own units: 3 to 5 simple shapes with round corners, the
# heads of the current logos without the snake body. The small one drops anything too fine for 16px.

FOX_HEAD = "M-34 -44L-12 -24H12L34 -44L32 -6L0 26L-32 -6Z"
BIRD_BODY = "M-83 -36.9L-11.84 -52.71A54 54 0 1 1 -47.14 26.57Z"
BIRD_BEAK = "M47.94 0.82L78.47 -19.6L41.93 -23.29Z"


def fox(small):
    """狐: the head and two eyes."""
    head = rounded(parse(FOX_HEAD), convex=4, concave=3)
    if small:
        return head, None
    return head, union(circle(-13, -7, 6), circle(13, -7, 6))


def plover(small):
    """千鳥: body, beak and eye. The logo's wing line is left out: under the eye it reads as a smile."""
    bird = rounded(union(parse(BIRD_BODY), parse(BIRD_BEAK)), convex=3, concave=4)
    if small:
        return bird, None
    return bird, circle(22.56, -18.36, 9)


def boxes(small):
    """入れ子枡: three boxes inside each other; two at 16px."""
    rings = ("M0 -60L60 0L0 60L-60 0Z M0 -44L44 0L0 44L-44 0Z M0 -30L30 0L0 30L-30 0Z "
             "M0 -16L16 0L0 16L-16 0Z M0 -4L4 0L0 4L-4 0Z") if not small else \
        "M0 -60L60 0L0 60L-60 0Z M0 -36L36 0L0 36L-36 0Z M0 -16L16 0L0 16L-16 0Z"
    if not small:
        # The innermost box is solid: drop the tiny hole at its centre.
        rings = rings.rsplit(" M", 1)[0]
    nested = rounded(even_odd(rings), convex=3)
    return nested, None


MOTIFS = {"yusai-tajiri": fox, "kikitori": plover, "explorer": boxes}


def motif_shape(app, small):
    shape, holes = MOTIFS[app](small)
    return shape if holes is None else minus(shape, holes)


def centred(path):
    x0, y0, x1, y1 = path.bounds
    return transformed(path, matrix(70, 70, 0, 1, (x0 + x1) / 2, (y0 + y1) / 2))


def fit(path, room, gap):
    """The largest copy of `path`, centred on the grid, that stays `gap` inside `room`."""
    path = centred(path)
    lo, hi = 0.1, 3.0
    for _ in range(24):
        s = (lo + hi) / 2
        trial = transformed(path, matrix(70, 70, 0, s, 70, 70))
        if empty(minus(grow(trial, gap), room)):
            lo = s
        else:
            hi = s
    return transformed(path, matrix(70, 70, 0, lo, 70, 70))


def mark(frame, app, small=False):
    """The frame as a ring with the motif fitted inside it."""
    ring, gap = (SMALL_RING, SMALL_GAP) if small else (RING, GAP)
    outer = FRAMES[frame]["draw"]()
    inner = shrink(outer, ring)
    return smooth(union(minus(outer, inner), fit(motif_shape(app, small), inner, gap)))


# ---------------------------------------------------------------- the lookalikes, for step 2
# Plain stand-ins for the shapes the doc wants to steer clear of, drawn from geometry, not traced
# from anyone's logo.

def pointy_hex(r=66):
    return polygon([(70 + r * math.cos(math.radians(a)), 70 + r * math.sin(math.radians(a)))
                    for a in range(-90, 270, 60)])


def lookalike_dev():
    """A solid pointy-topped hexagon with soft corners: dev-tool logos (Node.js, GraphQL)."""
    return rounded(pointy_hex(), convex=8)


def lookalike_sticker():
    """A pointy-topped hexagon with a border band: a hex sticker (R packages, laptop stickers)."""
    outer = pointy_hex()
    return union(minus(outer, pointy_hex(58)), pointy_hex(50))


def lookalike_crypto():
    """A thick pointy-topped hexagon outline with sharp corners: crypto tokens (Chainlink and others)."""
    return minus(pointy_hex(), pointy_hex(46))


LOOKALIKES = {
    "dev-tool": dict(name="Dev-tool hex", draw=lookalike_dev),
    "sticker": dict(name="Hex sticker", draw=lookalike_sticker),
    "crypto": dict(name="Crypto hex", draw=lookalike_crypto),
}


# ---------------------------------------------------------------- files

def svg(title, path, color, ground=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140" width="140" height="140">
<title>{title}</title>
{ground}<path fill="{color}" d="{to_svg(path)}"/>
</svg>
"""


def png(markup, size):
    data = resvg_py.svg_to_bytes(svg_string=markup, width=size, height=size)
    return Image.open(io.BytesIO(bytes(data))).convert("RGBA")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def save_mark(stem, title, path, light, dark, sizes):
    for suffix, color in (("", light), ("-on-dark", dark)):
        markup = svg(title, path, color)
        write(OUT / f"{stem}{suffix}.svg", markup)
        for size in sizes:
            png(markup, size).save(OUT / f"{stem}{suffix}-{size}.png")


def phone_tile(frame, app, theme):
    """The mark inside an iOS-style rounded square on the warm ground, as the phone masks it."""
    ground = COLORS["surface"][theme]
    color = COLORS[APPS[app]["color"]][theme]
    tile = f'<rect width="140" height="140" rx="31.5" fill="{ground}"/>\n'
    path = transformed(mark(frame, app), matrix(70, 70, 0, 0.74, 70, 70))
    return svg(f"{FRAMES[frame]['name']} on a phone", path, color, tile)


def build():
    for frame, f in FRAMES.items():
        for app, info in APPS.items():
            light, dark = COLORS[info["color"]]["light"], COLORS[info["color"]]["dark"]
            title = f"{info['name']} in the {f['name']} frame"
            save_mark(f"{frame}-{app}", title, mark(frame, app), light, dark, ())
            save_mark(f"{frame}-{app}-small", f"{title}, small", mark(frame, app, small=True), light, dark, (16,))
        write(OUT / f"{frame}-phone.svg", phone_tile(frame, "yusai-tajiri", "light"))
        write(OUT / f"{frame}-phone-on-dark.svg", phone_tile(frame, "yusai-tajiri", "dark"))
    for key, l in LOOKALIKES.items():
        light, dark = COLORS["ink-muted"]["light"], COLORS["ink-muted"]["dark"]
        save_mark(f"lookalike-{key}", l["name"], l["draw"](), light, dark, (16,))
    write(OUT / "index.html", sheet())


# ---------------------------------------------------------------- the comparison sheet

TYPE = {s["name"]: s for g in TOKENS["type"]["groups"] for s in g["styles"]}


def font(name):
    s = TYPE[name]
    return f"font-size: {s['fontSize']}; line-height: {s['lineHeight']}; font-weight: {s['fontWeight']};"


def picture(stem, size, alt, pixelated=False):
    """The light file, swapped for the -on-dark one when the system is dark."""
    ext = "-16.png" if pixelated or size == 16 else ".svg"
    cls = ' class="zoom"' if pixelated else ""
    return (f'<picture><source srcset="{stem}-on-dark{ext}" media="(prefers-color-scheme: dark)">'
            f'<img{cls} src="{stem}{ext}" width="{size}" height="{size}" alt="{alt}"></picture>')


def figure(content, caption):
    return f"<figure>{content}<figcaption>{caption}</figcaption></figure>"


def sheet():
    cards = []
    for frame, f in FRAMES.items():
        large = "".join(figure(picture(f"{frame}-{app}", 128, f"{info['name']} in the {f['name']} frame"),
                               f"{info['name']}<br>{info['motif'].split(':')[0]}")
                        for app, info in APPS.items())
        sizes = "".join(figure(picture(f"{frame}-{app}", 32, "") + picture(f"{frame}-{app}-small", 16, "")
                               + picture(f"{frame}-{app}-small", 64, "", pixelated=True),
                               "32px, 16px, 16px enlarged") for app in APPS)
        phone = figure(picture(f"{frame}-phone", 96, f"The brand mark in the {f['name']} frame on a phone"),
                       "On a phone")
        cards.append(f"""<section class="card">
<h2>{f['name']}</h2>
<p>{f['note']}</p>
<div class="row">{large}</div>
<div class="row">{sizes}{phone}</div>
</section>""")
    marks = [(f"{frame}-yusai-tajiri", f["name"]) for frame, f in FRAMES.items()]
    others = [(f"lookalike-{key}", l["name"]) for key, l in LOOKALIKES.items()]
    side = lambda size, small: "".join(
        figure(picture(stem + ("-small" if small and not stem.startswith("lookalike") else ""), size, name,
                       pixelated=small), name) for stem, name in marks + others)
    cards.append(f"""<section class="card">
<h2>Next to the hexagons to avoid</h2>
<p>The three frames with the brand's fox, then plain stand-ins for the shapes the direction steers clear of,
drawn from geometry rather than traced from anyone's logo: a solid pointy-topped hexagon as in dev-tool logos,
a hex sticker as on R packages and laptops, and a thick sharp outline as on crypto tokens.</p>
<div class="row">{side(96, False)}</div>
<div class="row">{side(64, True)}</div>
</section>""")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kamon frame candidates</title>
<link rel="stylesheet" href="../../tokens/tokens.css">
<style>
body {{ margin: 0; background: var(--surface); color: var(--ink); font-family: var(--font-sans); {font("body")} }}
main {{ max-width: 1040px; margin: 0 auto; padding: var(--space-12) var(--space-4); }}
h1 {{ margin: 0; {font("title")} }}
h2 {{ margin: 0; {font("heading")} }}
p {{ margin: var(--space-2) 0 0; max-width: 680px; color: var(--ink-muted); }}
.card {{ margin-top: var(--space-8); padding: var(--space-6); background: var(--surface-raised);
  border: 1px solid var(--border); border-radius: var(--radius-lg); }}
.row {{ display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--space-8); margin-top: var(--space-6); }}
figure {{ display: flex; flex-direction: column; align-items: center; gap: var(--space-2); margin: 0; }}
figure picture + picture {{ margin-top: var(--space-2); }}
figcaption {{ color: var(--ink-subtle); text-align: center; {font("caption")} }}
img {{ display: block; }}
img.zoom {{ image-rendering: pixelated; }}
</style>
</head>
<body>
<main>
<h1>Kamon frame candidates</h1>
<p>Step one and two of docs/direction-kamon-frame.md: each frame with Kikitori, Explorer and the brand's own motif,
at app-icon size and at 16px, and the brand mark next to the hexagons it should not be mistaken for.
The page follows the system's light or dark setting. Built by tools/explore_frames.py.</p>
{chr(10).join(cards)}
</main>
</body>
</html>
"""


if __name__ == "__main__":
    build()
