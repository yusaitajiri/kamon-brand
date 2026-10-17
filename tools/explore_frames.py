"""Draw the 木瓜 frame from docs/direction-kamon-frame.md, with each app's motif inside.

Run from the repo root:  pip install skia-pathops resvg-py pillow && python tools/explore_frames.py

This is exploration, not the live kit: it writes only to docs/kamon-frames/, and build_logo.py still
draws the logos in logo/ and icons/. Every mark is on the same 140 x 140 grid as the logos and comes
out as one filled path: the four-lobed frame drawn as bands, with the motif fitted inside. Each style
below is a different set of bands. The small mark, for 24px and down, is one heavier band with a wider
gap and the motif without its cut-outs, whatever the style. Colors come from tokens/tokens.json.

The first round, which compared three frames, is kept as candidates-light.png and candidates-dark.png.
"""

import io
import json
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

# The frame: four circles of radius `lobe`, set so the whole is 2 * half_w wide and 2 * half_h tall,
# a little wider than tall. A smaller lobe digs the notches deeper; 33 puts them 46 from the centre,
# deep enough to read as lobes while leaving the motif room. The notches are rounded by `notch`.
FRAME = dict(half_w=64, half_h=60, lobe=33, notch=3)

GAP = 7  # the least space between the motif and the innermost band
SMALL_BANDS, SMALL_GAP = (14,), 9  # at 16px: a 1.6px band and a 1px gap


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


def even_odd(d):
    p = parse(d)
    p.fillType = pathops.FillType.EVEN_ODD
    return pathops.simplify(p, fix_winding=True)


def empty(path):
    return path.area < 0.5


# ---------------------------------------------------------------- the frame

def four_lobes(half_w, half_h, lobe, notch):
    """木瓜: four lobes, wider than tall, meeting in rounded notches."""
    dx, dy = half_w - lobe, half_h - lobe
    lobes = union(circle(70 - dx, 70, lobe), circle(70 + dx, 70, lobe),
                  circle(70, 70 - dy, lobe), circle(70, 70 + dy, lobe))
    return rounded(lobes, concave=notch)


def bands(outer, widths):
    """Alternate filled and open bands inward from `outer`. Returns the bands and the space left inside."""
    shape, edge = pathops.Path(), outer
    for i, w in enumerate(widths):
        inner = shrink(edge, w)
        if i % 2 == 0:
            shape = union(shape, minus(edge, inner))
        edge = inner
    return shape, edge


def maru_ring():
    """丸に木瓜's plain ring, drawn around the frame scaled down to 0.8."""
    return minus(circle(70, 70, 66), circle(70, 70, 58))


# Bands from the outside in, filled first. The inner-line styles are the classic double outline of 木瓜.
STYLES = {
    "plain": dict(name="Without the inner line", bands=(9,),
                  note="One band. The motif gets the most room, and the lobes alone carry the crest."),
    "inner-line": dict(name="With a thin inner line", bands=(6, 4, 3),
                       note="A band, a gap and a thin second line that follows the lobes. The lightest double "
                            "outline, closest to the line drawings in crest books. The line is under a pixel "
                            "at 32px, so it blurs there."),
    "split-band": dict(name="With a split band", bands=(7, 3, 6),
                       note="Two bands nearly as heavy as each other with a thin opening between them. Still a "
                            "double outline, but it reads as one strong frame, and it holds a little better at "
                            "32px."),
    "maru": dict(name="With an outer ring (丸に木瓜)", bands=None,
                 note="The other way to add a line: a plain circle around the whole crest. A common real "
                      "variant, but the circle is what the icon looks like at a glance, which the direction "
                      "ruled out, and everything inside gets smaller."),
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
             "M0 -16L16 0L0 16L-16 0Z") if not small else \
        "M0 -60L60 0L0 60L-60 0Z M0 -36L36 0L0 36L-36 0Z M0 -16L16 0L0 16L-16 0Z"
    return rounded(even_odd(rings), convex=3), None


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


def mark(style, app, small=False):
    """The frame's bands with the motif fitted inside the innermost one."""
    outer = four_lobes(**FRAME)
    if small:
        widths, gap = SMALL_BANDS, SMALL_GAP
    elif STYLES[style]["bands"] is None:
        shape, room = bands(transformed(outer, matrix(70, 70, 0, 0.8, 70, 70)), (8,))
        return smooth(union(maru_ring(), shape, fit(motif_shape(app, False), room, GAP)))
    else:
        widths, gap = STYLES[style]["bands"], GAP
    shape, room = bands(outer, widths)
    return smooth(union(shape, fit(motif_shape(app, small), room, gap)))


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


def phone_tile(style, app, theme):
    """The mark inside an iOS-style rounded square on the warm ground, as the phone masks it."""
    ground = COLORS["surface"][theme]
    color = COLORS[APPS[app]["color"]][theme]
    tile = f'<rect width="140" height="140" rx="31.5" fill="{ground}"/>\n'
    path = transformed(mark(style, app), matrix(70, 70, 0, 0.74, 70, 70))
    return svg(f"{STYLES[style]['name']} on a phone", path, color, tile)


def build():
    for app, info in APPS.items():
        light, dark = COLORS[info["color"]]["light"], COLORS[info["color"]]["dark"]
        for style, s in STYLES.items():
            title = f"{info['name']} in the 木瓜 frame, {s['name'].lower()}"
            save_mark(f"{style}-{app}", title, mark(style, app), light, dark, (32,))
        save_mark(f"small-{app}", f"{info['name']} in the 木瓜 frame, small", mark(None, app, small=True),
                  light, dark, (16,))
    for style in STYLES:
        write(OUT / f"{style}-phone.svg", phone_tile(style, "yusai-tajiri", "light"))
        write(OUT / f"{style}-phone-on-dark.svg", phone_tile(style, "yusai-tajiri", "dark"))
    write(OUT / "index.html", sheet())


# ---------------------------------------------------------------- the comparison sheet

TYPE = {s["name"]: s for g in TOKENS["type"]["groups"] for s in g["styles"]}


def font(name):
    s = TYPE[name]
    return f"font-size: {s['fontSize']}; line-height: {s['lineHeight']}; font-weight: {s['fontWeight']};"


def picture(stem, size, alt, raster=None, pixelated=False):
    """The light file, swapped for the -on-dark one when the system is dark. `raster` picks a PNG
    rendered at that size, so small sizes show what the renderer really makes of them."""
    ext = f"-{raster}.png" if raster else ".svg"
    cls = ' class="zoom"' if pixelated else ""
    return (f'<picture><source srcset="{stem}-on-dark{ext}" media="(prefers-color-scheme: dark)">'
            f'<img{cls} src="{stem}{ext}" width="{size}" height="{size}" alt="{alt}"></picture>')


def figure(content, caption):
    return f"<figure>{content}<figcaption>{caption}</figcaption></figure>"


def sheet():
    cards = []
    for style, s in STYLES.items():
        large = "".join(figure(picture(f"{style}-{app}", 128, f"{info['name']}, {s['name'].lower()}"),
                               f"{info['name']}<br>{info['motif'].split(':')[0]}")
                        for app, info in APPS.items())
        sizes = "".join(figure(picture(f"{style}-{app}", 32, "", raster=32)
                               + picture(f"{style}-{app}", 64, "", raster=32, pixelated=True),
                               "32px and enlarged") for app in APPS)
        phone = figure(picture(f"{style}-phone", 96, f"The brand mark {s['name'].lower()}, on a phone"),
                       "On a phone")
        cards.append(f"""<section class="card">
<h2>{s['name']}</h2>
<p>{s['note']}</p>
<div class="row">{large}</div>
<div class="row">{sizes}{phone}</div>
</section>""")
    small = "".join(figure(picture(f"small-{app}", 16, "", raster=16)
                           + picture(f"small-{app}", 64, f"{info['name']} at 16px, enlarged", raster=16,
                                     pixelated=True), info["name"])
                    for app, info in APPS.items())
    cards.append(f"""<section class="card">
<h2>At 16px</h2>
<p>Every style uses the same small mark: one heavier band and the motif without its cut-outs.
An inner line or an outer ring would be under a pixel here.</p>
<div class="row">{small}</div>
</section>""")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>木瓜 frame study</title>
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
<h1>木瓜 frame study</h1>
<p>The four-lobed frame chosen in docs/direction-kamon-frame.md, with and without the inner line of the
classic crest, and with the outer ring of 丸に木瓜 for reference. The page follows the system's light or
dark setting. Built by tools/explore_frames.py.</p>
{chr(10).join(cards)}
</main>
</body>
</html>
"""


if __name__ == "__main__":
    build()
