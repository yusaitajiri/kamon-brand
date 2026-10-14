"""Build every mon SVG and app icon in this kit from the shapes below.

Run from the repo root:  pip install resvg-py pillow && python tools/build_mon.py

Each mon is drawn on a 140 x 140 grid as a mask: white is ink, black is a cut-out, so cut-outs
stay transparent in every file. Change a shape or a color here and rebuild; never edit the
generated files by hand.
"""

import io
from pathlib import Path

import resvg_py
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
W, B = "#fff", "#000"

INK = "#2A2826"
PAPER = "#FBFAF7"
SURFACE = "#F3F1EC"

# Each app's accent, light and dark. These must match tokens/tokens.json.
APPS = {
    "kudagitsune": {"name": "Kudagitsune", "color": "moss", "light": "#4E6B4F", "dark": "#8FB08F"},
    "kikitori": {"name": "Kikitori", "color": "shu", "light": "#B0501F", "dark": "#EBA57E"},
    "explorer": {"name": "Explorer (working name)", "color": "ai", "light": "#3B5878", "dark": "#93AACB"},
}

BIRD_BODY = "M-83 -36.9L-11.84 -52.71A54 54 0 1 1 -47.14 26.57Z"
BIRD_BEAK = "M47.94 0.82L78.47 -19.6L41.93 -23.29Z"
FOX_HEAD = "M-34 -44L-12 -24H12L34 -44L32 -6L0 26L-32 -6Z"
WAVE = "M16 104C28 90 42 90 52 104C62 118 76 118 88 104C98 92 112 92 124 104"

# The full mon, for 32 px and up.
FULL = {
    # The fox looking out of its bamboo tube, as on the hanko.
    "kudagitsune": f"""<g transform="translate(70 70) scale(1.08) translate(-70 -72)">
  <g transform="translate(70 54) scale(0.66)">
    <path d="{FOX_HEAD}" fill="{W}"/>
    <circle cx="-13" cy="-8" r="5" fill="{B}"/>
    <circle cx="13" cy="-8" r="5" fill="{B}"/>
  </g>
  <rect x="36" y="66" width="68" height="12" rx="3" fill="{W}" stroke="{B}" stroke-width="6" paint-order="stroke"/>
  <rect x="41" y="82" width="58" height="42" rx="4" fill="{W}"/>
  <rect x="41" y="100" width="58" height="3" fill="{B}"/>
</g>""",
    # 波に千鳥: a plover over a wave. The wave is Kikitori's recording line.
    "kikitori": f"""<g transform="translate(66 52) scale(0.5)">
  <path d="{BIRD_BODY}" fill="{W}"/>
  <path d="{BIRD_BEAK}" fill="{W}"/>
  <circle cx="22.56" cy="-18.36" r="8" fill="{B}"/>
  <path d="M-34 6C-14 26 16 26 34 10" fill="none" stroke="{B}" stroke-width="7" stroke-linecap="round"/>
</g>
<path d="{WAVE}" fill="none" stroke="{W}" stroke-width="10" stroke-linecap="round"/>""",
    # 入れ子枡: boxes inside boxes, as folders inside folders.
    "explorer": f"""<path fill="{W}" fill-rule="evenodd" d="M70 12L128 70L70 128L12 70Z M70 24L116 70L70 116L24 70Z M70 36L104 70L70 104L36 70Z M70 48L92 70L70 92L48 70Z M70 58L82 70L70 82L58 70Z"/>""",
}

# The small mon, for 24 px and down: the same outline with the cut-outs too fine to see removed.
SMALL = {
    "kudagitsune": f"""<g transform="translate(70 70) scale(1.08) translate(-70 -72)">
  <g transform="translate(70 54) scale(0.66)"><path d="{FOX_HEAD}" fill="{W}"/></g>
  <rect x="36" y="66" width="68" height="58" rx="5" fill="{W}"/>
</g>""",
    "kikitori": f"""<g transform="translate(66 52) scale(0.5)">
  <path d="{BIRD_BODY}" fill="{W}"/>
  <path d="{BIRD_BEAK}" fill="{W}"/>
</g>
<path d="{WAVE}" fill="none" stroke="{W}" stroke-width="16" stroke-linecap="round"/>""",
    "explorer": f"""<path fill="{W}" fill-rule="evenodd" d="M70 10L130 70L70 130L10 70Z M70 32L108 70L70 108L32 70Z M70 50L90 70L70 90L50 70Z"/>""",
}


def ringed(shape: str, ring_width: float, radius: float, scale: float) -> str:
    """丸に〜: the shared ring of the family, with the mon inside it."""
    return (
        f'<circle cx="70" cy="70" r="{radius}" fill="none" stroke="{W}" stroke-width="{ring_width}"/>\n'
        f'<g transform="translate(70 70) scale({scale}) translate(-70 -70)">\n{shape}\n</g>'
    )


def svg(title: str, mask: str, color: str, ground: str = "") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140" width="140" height="140">
<title>{title}</title>
<defs>
<mask id="mon" maskUnits="userSpaceOnUse" x="0" y="0" width="140" height="140">
<rect width="140" height="140" fill="{B}"/>
{mask}
</mask>
</defs>
{ground}<rect width="140" height="140" fill="{color}" mask="url(#mon)"/>
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
    full = ringed(FULL[app], 9, 64, 0.7)
    small = ringed(SMALL[app], 14, 62, 0.66)
    mon_dir = ROOT / "mon"

    for suffix, color in (("", info["light"]), ("-on-dark", info["dark"]), ("-ink", INK)):
        write(mon_dir / f"{app}{suffix}.svg", svg(f"{info['name']} mon", full, color))
        write(mon_dir / f"{app}-small{suffix}.svg", svg(f"{info['name']} mon, small", small, color))

    # The app icon is the mon on a paper disc, so it reads on light and dark taskbars alike.
    disc = f'<circle cx="70" cy="70" r="69" fill="{PAPER}"/>\n'
    icon = svg(f"{info['name']} app icon", full, info["light"], disc)
    icon_small = svg(f"{info['name']} app icon, small", small, info["light"], disc)
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

    # Stores and iOS want an opaque square: the mon on the warm ground.
    store = svg(f"{info['name']} store icon", ringed(FULL[app], 9, 64, 0.7), info["light"])
    store = store.replace(
        f'<rect width="140" height="140" fill="{info["light"]}" mask="url(#mon)"/>',
        f'<rect width="140" height="140" fill="{SURFACE}"/>\n'
        f'<g transform="translate(70 70) scale(0.78) translate(-70 -70)">'
        f'<rect width="140" height="140" fill="{info["light"]}" mask="url(#mon)"/></g>',
    )
    png(store, 1024).convert("RGB").save(icon_dir / "app-icon-1024.png")

    if app == "kudagitsune":
        # The brand's own site icons are the 管狐 mon.
        icons = ROOT / "icons"
        png(icon, 32).save(icons / "favicon-32.png")
        png(icon, 192).save(icons / "favicon-192.png")
        png(store, 180).convert("RGB").save(icons / "apple-touch-icon-180.png")
        png(store, 1024).convert("RGB").save(icons / "app-icon-1024.png")


if __name__ == "__main__":
    for name in APPS:
        build_app(name)
