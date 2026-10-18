# /// script
# requires-python = ">=3.11"
# dependencies = ["skia-pathops", "resvg-py", "pillow"]
# ///
"""Build every logo SVG and app icon in the brand from the shapes below.

Run from the repo root:  uv run tools/build_logo.py

Every logo is a kamon (家紋): the same four-lobed 木瓜 frame, drawn as a band with a thin line inside
it, and the app's own motif in the middle, an animal or an object reduced to a few simple shapes.
Everything is on a 140 x 140 grid, and each logo comes out as one filled path whose cut-outs are
transparent. Colors come from tokens/tokens.json. Change a shape or a proportion here and rebuild;
never edit the generated files by hand. logokit.py holds the geometry.
"""

import io
import json
from pathlib import Path

import pathops
import resvg_py
from PIL import Image

from logokit import circle, grow, matrix, minus, parse, rounded, shrink, smooth, to_svg, transformed, union

ROOT = Path(__file__).resolve().parent.parent

TOKENS = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))
COLORS = {t["name"]: t["value"] for t in TOKENS["color"]["tokens"]}
APPS = {a["id"]: a for a in TOKENS["apps"]["list"]}

INK = COLORS["ink"]["light"]
PAPER = COLORS["surface-raised"]["light"]
SURFACE = COLORS["surface"]["light"]

# ---------------------------------------------------------------- the frame

# 木瓜: four circles of radius `lobe`, set so the whole is 2 * half_w wide and 2 * half_h tall, a little
# wider than tall. A smaller lobe digs the notches deeper but squeezes the motif, whose corners run
# into them; 35 puts the notches 48 from the centre, still clearly lobed. They are rounded by `notch`.
FRAME = dict(half_w=64, half_h=60, lobe=35, notch=3)

# The frame's bands from the outside in, filled first: a band, a gap and the thin inner line of the
# classic crest, kept slim to leave the motif room. `gap` is the least space between the motif and
# the innermost band.
FULL = dict(bands=(6, 3, 3), gap=5)

# 24px and down: one heavier band, a wider gap, and the motif without its cut-outs, so it holds
# together at a few pixels. The inner line would be under a pixel there.
SMALL = dict(bands=(14,), gap=9)


def four_lobes(half_w, half_h, lobe, notch):
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


# ---------------------------------------------------------------- the motifs
# Each motif is 3 to 5 simple shapes with round corners, as (shape, holes) in its own units; it is
# centred and sized to fill the frame. The small one drops anything too fine for 24px and down.

FOX_HEAD = "M-34 -44L-12 -24H12L34 -44L32 -6L0 26L-32 -6Z"
BIRD_BODY = "M-83 -36.9L-11.84 -52.71A54 54 0 1 1 -47.14 26.57Z"
BIRD_BEAK = "M47.94 0.82L78.47 -19.6L41.93 -23.29Z"
BOXES = "M0 -60L60 0L0 60L-60 0Z M0 -44L44 0L0 44L-44 0Z M0 -30L30 0L0 30L-30 0Z M0 -16L16 0L0 16L-16 0Z"
BOXES_SMALL = "M0 -60L60 0L0 60L-60 0Z M0 -36L36 0L0 36L-36 0Z M0 -16L16 0L0 16L-16 0Z"


def fox(small):
    """狐: the head and two eyes."""
    head = rounded(parse(FOX_HEAD), convex=4, concave=3)
    return head, None if small else union(circle(-13, -7, 6), circle(13, -7, 6))


def plover(small):
    """千鳥: the plover of 波に千鳥, as body, beak and eye. No wing line: under the eye it reads as a smile."""
    bird = rounded(union(parse(BIRD_BODY), parse(BIRD_BEAK)), convex=3, concave=4)
    return bird, None if small else circle(22.56, -18.36, 9)


def boxes(small):
    """入れ子枡: measuring boxes inside each other, as folders inside folders; two at 24px and down."""
    nested = parse(BOXES_SMALL if small else BOXES)
    nested.fillType = pathops.FillType.EVEN_ODD
    return rounded(pathops.simplify(nested, fix_winding=True), convex=3), None


MOTIFS = {"brand": fox, "chidori": plover, "explorer": boxes}


def fit(path, room, gap):
    """The largest copy of `path`, centred on the grid, that stays `gap` inside `room`."""
    x0, y0, x1, y1 = path.bounds
    path = transformed(path, matrix(70, 70, 0, 1, (x0 + x1) / 2, (y0 + y1) / 2))
    lo, hi = 0.1, 3.0
    for _ in range(24):
        s = (lo + hi) / 2
        if minus(grow(transformed(path, matrix(70, 70, 0, s, 70, 70)), gap), room).area < 0.5:
            lo = s
        else:
            hi = s
    return transformed(path, matrix(70, 70, 0, lo, 70, 70))


def logo(app, small=False):
    """The logo as one path: the frame's bands with the app's motif fitted inside."""
    p = SMALL if small else FULL
    shape, room = bands(four_lobes(**FRAME), p["bands"])
    outline, holes = MOTIFS[app](small)
    motif = outline if holes is None else minus(outline, holes)
    return smooth(union(shape, fit(motif, room, p["gap"])))


# ---------------------------------------------------------------- files

def svg(title: str, path, color: str, ground: str = "") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140" width="140" height="140">
<title>{title}</title>
{ground}<path fill="{color}" d="{to_svg(path)}"/>
</svg>
"""


def png(markup: str, size: int) -> Image.Image:
    data = resvg_py.svg_to_bytes(svg_string=markup, width=size, height=size)
    return Image.open(io.BytesIO(bytes(data))).convert("RGBA")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def build_app(app: str) -> None:
    info = APPS[app]
    light, dark = COLORS[info["color"]]["light"], COLORS[info["color"]]["dark"]
    full, small = logo(app), logo(app, small=True)
    logo_dir = ROOT / "logo"

    for suffix, color in (("", light), ("-on-dark", dark), ("-ink", INK)):
        write(logo_dir / f"{app}{suffix}.svg", svg(f"{info['name']} logo", full, color))
        write(logo_dir / f"{app}-small{suffix}.svg", svg(f"{info['name']} logo, small", small, color))

    # The app icon is the logo with its frame filled with paper, so it reads on light and dark
    # taskbars alike and keeps the frame's own outline. The paper stops a little inside the band,
    # so no light edge shows around it.
    paper = f'<path fill="{PAPER}" d="{to_svg(shrink(four_lobes(**FRAME), 2))}"/>\n'
    icon = svg(f"{info['name']} app icon", full, light, paper)
    icon_small = svg(f"{info['name']} app icon, small", small, light, paper)
    icon_dir = ROOT / "icons" / app
    write(icon_dir / "icon.svg", icon)
    write(icon_dir / "icon-small.svg", icon_small)

    frames = {}
    for size in (16, 20, 24, 32, 48, 64, 128, 256, 1024):
        image = png(icon_small if size <= 24 else icon, size)
        image.save(icon_dir / f"icon-{size}.png")
        frames[size] = image
    ico_sizes = [16, 20, 24, 32, 48, 64, 256]
    frames[256].save(
        icon_dir / "icon.ico",
        sizes=[(s, s) for s in ico_sizes],
        append_images=[frames[s] for s in ico_sizes if s != 256],
    )

    # Stores and iOS want an opaque square: the logo on the warm ground, inside the platform's mask.
    ground = f'<rect width="140" height="140" fill="{SURFACE}"/>\n'
    store = svg(f"{info['name']} store icon", transformed(full, matrix(70, 70, 0, 0.74, 70, 70)), light, ground)
    png(store, 1024).convert("RGB").save(icon_dir / "app-icon-1024.png")

    if app == "brand":
        # The brand's own site icons are the brand logo.
        icons = ROOT / "icons"
        png(icon, 32).save(icons / "favicon-32.png")
        png(icon, 192).save(icons / "favicon-192.png")
        png(store, 180).convert("RGB").save(icons / "apple-touch-icon-180.png")
        png(store, 1024).convert("RGB").save(icons / "app-icon-1024.png")


if __name__ == "__main__":
    for name in APPS:
        build_app(name)
