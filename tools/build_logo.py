"""Build every logo SVG and app icon in this kit from the shapes below.

Run from the repo root:  pip install skia-pathops resvg-py pillow && python tools/build_logo.py

Every logo is the same long body, lying in one ring on the ground with its neck rising from the
ring's front in a gentle S, and the app's own head on top. Everything is on a 140 x 140 grid, and each
logo comes out as one filled path whose cut-outs are transparent. Change a shape, a proportion or a
color here and rebuild; never edit the generated files by hand. logokit.py holds the geometry.
"""

import io
import math
from pathlib import Path

import pathops
import resvg_py
from PIL import Image

from logokit import (Body, Centerline, circle, ease, grow, hobby_path, matrix, minus, parse, polylines,
                    segments, smooth, to_svg, transformed, union)

ROOT = Path(__file__).resolve().parent.parent

INK = "#2A2826"
PAPER = "#FBFAF7"
SURFACE = "#F3F1EC"

# Each app's accent, light and dark. These must match tokens/tokens.json.
APPS = {
    "kudagitsune": {"name": "Kudagitsune", "color": "moss", "light": "#4E6B4F", "dark": "#8FB08F"},
    "kikitori": {"name": "Kikitori", "color": "shu", "light": "#B0501F", "dark": "#EBA57E"},
    "explorer": {"name": "Explorer (working name)", "color": "ai", "light": "#3B5878", "dark": "#93AACB"},
}

# ---------------------------------------------------------------- the heads

FOX_HEAD = "M-34 -44L-12 -24H12L34 -44L32 -6L0 26L-32 -6Z"
FOX_EYES = ((-13, -8, 5), (13, -8, 5))
BIRD_BODY = "M-83 -36.9L-11.84 -52.71A54 54 0 1 1 -47.14 26.57Z"
BIRD_BEAK = "M47.94 0.82L78.47 -19.6L41.93 -23.29Z"
BIRD_EYE = (22.56, -18.36, 8)
BIRD_WING = ((-34, 6), (-14, 26), (16, 26), (34, 10))  # cut out as a round-ended line 7 wide
BOXES = ("M70 12L128 70L70 128L12 70Z M70 24L116 70L70 116L24 70Z M70 36L104 70L70 104L36 70Z "
         "M70 48L92 70L70 92L48 70Z M70 58L82 70L70 82L58 70Z")
BOXES_SMALL = "M70 10L130 70L70 130L10 70Z M70 32L108 70L70 108L32 70Z M70 50L90 70L70 90L50 70Z"


def fox(small):
    holes = None if small else union(*(circle(x, y, r) for x, y, r in FOX_EYES))
    return parse(FOX_HEAD), holes


def plover(small):
    """波に千鳥's plover, without its wave."""
    outline = union(parse(BIRD_BODY), parse(BIRD_BEAK))
    if small:
        return outline, None
    c = Centerline(*BIRD_WING[0], 0).cubic(*BIRD_WING[1:])
    wing = smooth(Body(c.pts, [7] * len(c.pts)).piece(0, len(c.pts) - 1, ("round", "round")))
    return outline, union(circle(*BIRD_EYE), wing)


def boxes(small):
    """入れ子枡: boxes inside boxes, as folders inside folders."""
    nested = parse(BOXES_SMALL if small else BOXES)
    nested.fillType = pathops.FillType.EVEN_ODD
    nested = pathops.simplify(nested, fix_winding=True)
    outline = parse("M70 10L130 70L70 130L10 70Z" if small else "M70 12L128 70L70 128L12 70Z")
    return outline, minus(outline, nested)


# Each head in its own drawing's units: its lowest point (the chin, where every head sits on the
# body) and its size on the grid.
HEADS = {
    "kudagitsune": dict(draw=fox, chin=(0, 26), scale=0.9),
    "kikitori": dict(draw=plover, chin=(-8, 53.4), scale=0.459),
    "explorer": dict(draw=boxes, chin=(70, 128), scale=0.54),
}

# ---------------------------------------------------------------- the body

# The body is the same in every app. Its centre line lies on an ellipse, the ring on the ground
# seen from the front: ring = (cx, cy, rx, ry). The neck leaves the ring's front at x = base,
# crosses the ring's far side upright at x = low, swings through the mid points and meets the
# head's lower right edge square on, `joint` along that edge from the chin. The tail tip lies
# `sweep` degrees back round the ring and the body tapers to it over `tail`; the neck narrows
# to neck_end of the body's width. Wherever the body passes in front of itself, a cut `gap` wide
# separates the two.
BODY = dict(ring=(70, 116.5, 48, 14.5), width=13.5, gap=3.6, base=70, low=58, mid=((66, 86), (80, 75)),
            chin=(70, 67), joint=10, sweep=330, tail=28, neck_end=0.8)

# 24 px and down: a heavier body, wider cuts, a rounder ring and a simpler neck, with the tail
# tucked under the neck, so it holds together at a few pixels. The heads drop their cut-outs.
SMALL_BODY = dict(BODY, ring=(70, 113, 47, 16.5), width=18, gap=6, low=52, mid=((76, 73),), chin=(70, 66),
                  joint=16, sweep=345, tail=20)


def centerline(p):
    """From the tail tip round the ring, then up the neck and on, hidden, into the head."""
    cx, cy, rx, ry = p["ring"]
    front = math.degrees(math.acos((p["base"] - cx) / rx))
    c = Centerline.ellipse(cx, cy, rx, ry, front + 360 - p["sweep"], front + 360)
    neck = len(c.pts) - 1
    low = (p["low"], cy - ry * math.sqrt(1 - ((p["low"] - cx) / rx) ** 2))
    edge = math.radians(-45)
    joint = (p["chin"][0] + p["joint"] * math.cos(edge), p["chin"][1] + p["joint"] * math.sin(edge))
    knots = [(*c.end, c.heading), (*low, 270)] + [(x, y, None) for x, y in p["mid"]] + [(*joint, 225)]
    for c1, c2, q in hobby_path(knots):
        c.cubic(c1, c2, q)
    c.line(12)
    return c.pts, neck


def widths(pts, neck, p):
    s = [0.0]
    for a, b in zip(pts, pts[1:]):
        s.append(s[-1] + math.dist(a, b))
    out = []
    for x in s:
        w = p["width"]
        if x < p["tail"]:
            w *= 1 - (1 - x / p["tail"]) ** 2
        if x > s[neck]:
            w *= 1 - (1 - p["neck_end"]) * ease((x - s[neck]) / (s[-1] - s[neck]))
        out.append(w)
    return out


def head(app, p, small):
    h = HEADS[app]
    outline, holes = h["draw"](small)
    m = matrix(*p["chin"], 0, h["scale"], *h["chin"])
    return transformed(outline, m), (transformed(holes, m) if holes is not None else None)


def logo(app, small=False):
    """The logo as one path: the body with the app's head on top."""
    p = SMALL_BODY if small else BODY
    pts, neck = centerline(p)
    body = Body(pts, widths(pts, neck, p))
    n = len(pts) - 1
    # Painter's order. Behind: the tail, round the far side to the ring's right-hand end. In
    # front: the rest of the ring and the neck. Where the neck passes in front, the part behind
    # is cut back by the gap. The part behind ends a little narrower inside the part in front,
    # so the two never share an edge (path booleans are unreliable on edges that nearly coincide).
    end = max(range(neck // 3, neck + 1), key=lambda i: pts[i][0])
    k = 25
    inset = lambda i: 0.35 * min(1.0, max(0.0, (i - (end - 2 * k)) / k))
    behind = smooth(body.piece(0, end + k, inset=inset))
    front = smooth(body.piece(end - 2 * k, n, ("none", "round")))
    cutter = smooth(body.piece(neck, n, ("round", "round"), grow=p["gap"]))
    shape = smooth(union(minus(behind, cutter), front))
    outline, holes = head(app, p, small)
    face = outline if holes is None else minus(outline, holes)
    return tidy(union(minus(shape, grow(outline, p["gap"])), face))


def tidy(path, least=15):
    """Drop specks under `least` square units, such as the pocket a thick ring leaves at the
    pointed ends of its hole. The smallest real cut-out, an eye, is about 40."""
    out, contour = pathops.Path(), pathops.Path()
    for seg in segments(path):
        if seg[0] == "M":
            contour.moveTo(*seg[1])
        elif seg[0] == "L":
            contour.lineTo(*seg[1])
        elif seg[0] == "C":
            contour.cubicTo(*seg[1], *seg[2], *seg[3])
        else:
            contour.close()
            if contour.area >= least:
                contour.draw(out.getPen())
            contour = pathops.Path()
    return pathops.simplify(out, fix_winding=True)


def fitted(path, scale):
    """The path scaled about the grid's centre."""
    return transformed(path, matrix(70, 70, 0, scale, 70, 70))


def reach(path):
    """How far the path reaches from the grid's centre."""
    return max(math.dist(q, (70, 70)) for poly in polylines(path) for q in poly)


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
    full, small = logo(app), logo(app, small=True)
    logo_dir = ROOT / "logo"

    for suffix, color in (("", info["light"]), ("-on-dark", info["dark"]), ("-ink", INK)):
        write(logo_dir / f"{app}{suffix}.svg", svg(f"{info['name']} logo", full, color))
        write(logo_dir / f"{app}-small{suffix}.svg", svg(f"{info['name']} logo, small", small, color))

    # The app icon is the logo on a paper disc, so it reads on light and dark taskbars alike. The
    # logo reaches past the disc, so it is scaled down to sit inside it.
    disc = f'<circle cx="70" cy="70" r="69" fill="{PAPER}"/>\n'
    on_disc = lambda path: fitted(path, min(1.0, 63 / reach(path)))
    icon = svg(f"{info['name']} app icon", on_disc(full), info["light"], disc)
    icon_small = svg(f"{info['name']} app icon, small", on_disc(small), info["light"], disc)
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

    # Stores and iOS want an opaque square: the logo on the warm ground.
    ground = f'<rect width="140" height="140" fill="{SURFACE}"/>\n'
    store = svg(f"{info['name']} store icon", fitted(full, 0.78), info["light"], ground)
    png(store, 1024).convert("RGB").save(icon_dir / "app-icon-1024.png")

    if app == "kudagitsune":
        # The brand's own site icons are the 管狐 logo.
        icons = ROOT / "icons"
        png(icon, 32).save(icons / "favicon-32.png")
        png(icon, 192).save(icons / "favicon-192.png")
        png(store, 180).convert("RGB").save(icons / "apple-touch-icon-180.png")
        png(store, 1024).convert("RGB").save(icons / "app-icon-1024.png")


if __name__ == "__main__":
    for name in APPS:
        build_app(name)
