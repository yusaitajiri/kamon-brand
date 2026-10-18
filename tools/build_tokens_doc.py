"""Write tokens/tokens.md, a readable table of every token, from tokens/tokens.json.

Run from the repo root:  uv run tools/build_tokens_doc.py

tokens.json stays the source of truth: the platform kits generate their own files from it, and this
page is only for people to read. Change a value in tokens.json and rerun; never edit tokens.md by hand.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))


def cell(text) -> str:
    return str(text).replace("|", "\\|")


def color_value(value: str) -> str:
    """A hex value as code, or a reference such as {moss} as the token it points at."""
    ref = re.fullmatch(r"\{(.+)\}", value)
    return f"→ `{ref.group(1)}`" if ref else f"`{value}`"


def table(head: list[str], rows: list[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    lines += ["| " + " | ".join(cell(c) for c in row) + " |" for row in rows]
    return lines + [""]


def build() -> str:
    t = TOKENS
    out = [
        f"# {t['name']} tokens",
        "",
        "Generated from `tokens.json` by `tools/build_tokens_doc.py`. Don't edit this file: change `tokens.json` and rerun.",
        "",
        "## Color",
        "",
        "`→ name` means the token takes that token's value. An app points `accent` at its own color (see *Apps*).",
        "",
    ]
    out += table(
        ["Token", "Light", "Dark", "Usage"],
        [[f"`{c['name']}`", color_value(c["value"]["light"]), color_value(c["value"]["dark"]), c["usage"]]
         for c in t["color"]["tokens"]],
    )

    out += ["## Apps", "", t["apps"]["note"], ""]
    out += table(
        ["App id", "Name", "Color", "Motif"],
        [[f"`{a['id']}`", a["name"], f"`{a['color']}`", a["motif"]] for a in t["apps"]["list"]],
    )
    out += ["Free for the next app: " + ", ".join(f"`{c}`" for c in t["apps"]["free"]) + ".", ""]

    out += ["## Type", ""]
    out += table(["Family", "Stack"], [[f"`font-{k}`", f"`{v}`"] for k, v in t["type"]["families"].items()])
    out += table(
        ["Style", "Family", "Size / line height", "Weight", "Usage"],
        [[f"`{s['name']}`", g["family"], f"{s['fontSize']} / {s['lineHeight']}", s["fontWeight"], s["usage"]]
         for g in t["type"]["groups"] for s in g["styles"]],
    )

    out += ["## Spacing", ""]
    out += table(["Token", "Value", "Usage"], [[f"`{s['name']}`", s["value"], s["usage"]] for s in t["spacing"]["tokens"]])

    out += ["## Radius", ""]
    out += table(["Token", "Value", "Usage"], [[f"`{r['name']}`", r["value"], r["usage"]] for r in t["radius"]["tokens"]])

    out += ["## Shadow", "", t["shadow"]["note"], ""]
    out += table(
        ["Token", "Light", "Dark", "Usage"],
        [[f"`{s['name']}`", f"`{s['value']['light']}`", f"`{s['value']['dark']}`", s["usage"]] for s in t["shadow"]["tokens"]],
    )
    return "\n".join(out).rstrip() + "\n"


if __name__ == "__main__":
    (ROOT / "tokens" / "tokens.md").write_text(build(), encoding="utf-8", newline="\n")
