"""Geometry for drawing the logos as real outlines instead of painted strokes.

A body is a centre line with a width along it. Its outline is computed from the normals of the
centre line, then fitted with a few cubic curves. Skia's path engine (skia-pathops) does the
unions and the cuts, so a whole logo comes out as one filled path that any vector editor can open.
tools/build_logo.py holds the shapes; this file only holds the geometry.
"""
import math
import re

import pathops
from pathops import Path, PathOp, FillType, LineCap, LineJoin

# ---------------------------------------------------------------- small vector helpers

def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, k): return (a[0] * k, a[1] * k)
def dot(a, b): return a[0] * b[0] + a[1] * b[1]
def length(a): return math.hypot(a[0], a[1])


def unit(a):
    d = length(a)
    return (a[0] / d, a[1] / d) if d > 1e-12 else (0.0, 0.0)


# ---------------------------------------------------------------- centre lines

class Centerline:
    """A centre line drawn like a turtle: ellipse arcs, cubic curves and straight runs, sampled
    finely. Headings are in degrees on the SVG grid (0 = right, 90 = down)."""

    STEP = 0.2

    def __init__(self, x, y, heading):
        self.pts = [(x, y)]
        self.h = math.radians(heading)

    @property
    def end(self):
        return self.pts[-1]

    @property
    def heading(self):
        return math.degrees(self.h)

    def line(self, d):
        x, y = self.end
        n = max(1, int(abs(d) / self.STEP))
        for i in range(1, n + 1):
            t = d * i / n
            self.pts.append((x + t * math.cos(self.h), y + t * math.sin(self.h)))
        return self

    def cubic(self, c1, c2, p3):
        p0 = self.end
        n = 400
        for i in range(1, n + 1):
            t = i / n
            u = 1 - t
            self.pts.append((u**3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t**3 * p3[0],
                             u**3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t**3 * p3[1]))
        d = sub(p3, c2) if length(sub(p3, c2)) > 1e-9 else sub(p3, c1)
        self.h = math.atan2(d[1], d[0])
        return self

    @classmethod
    def ellipse(cls, cx, cy, rx, ry, th0, th1):
        """Start a centre line on an ellipse arc, from angle th0 to th1 (degrees)."""
        a0, a1 = math.radians(th0), math.radians(th1)
        c = cls(cx + rx * math.cos(a0), cy + ry * math.sin(a0), 0)
        c.ellipse_to(cx, cy, rx, ry, a0, a1)
        return c

    def ellipse_to(self, cx, cy, rx, ry, a0, a1):
        perim = math.pi * (3 * (rx + ry) - math.sqrt((3 * rx + ry) * (rx + 3 * ry)))
        n = max(8, int(abs(a1 - a0) / (2 * math.pi) * perim / self.STEP))
        for i in range(1, n + 1):
            t = a0 + (a1 - a0) * i / n
            self.pts.append((cx + rx * math.cos(t), cy + ry * math.sin(t)))
        s = 1 if a1 > a0 else -1
        self.h = math.atan2(s * ry * math.cos(a1), -s * rx * math.sin(a1))
        return self


# ---------------------------------------------------------------- outlines

def circle(cx, cy, r, path=None):
    """A circle as four cubic arcs."""
    k = 0.5522847498 * r
    p = path if path is not None else Path()
    p.moveTo(cx + r, cy)
    p.cubicTo(cx + r, cy + k, cx + k, cy + r, cx, cy + r)
    p.cubicTo(cx - k, cy + r, cx - r, cy + k, cx - r, cy)
    p.cubicTo(cx - r, cy - k, cx - k, cy - r, cx, cy - r)
    p.cubicTo(cx + k, cy - r, cx + r, cy - k, cx + r, cy)
    p.close()
    return p


def segments(path):
    """The path's segments with every quadratic run turned into cubics: yields ("M", p),
    ("L", p), ("C", c1, c2, p) and ("Z",). skia-pathops reports a run of quadratics as one
    qCurveTo with several off-curve points (TrueType style, on-curve points implied midway)."""
    last = start = None
    for verb, pts in path.segments:
        if verb == "moveTo":
            last = start = pts[0]
            yield ("M", pts[0])
        elif verb == "lineTo":
            last = pts[0]
            yield ("L", pts[0])
        elif verb == "curveTo":
            last = pts[2]
            yield ("C", pts[0], pts[1], pts[2])
        elif verb == "qCurveTo":
            offs, end = list(pts[:-1]), pts[-1]
            for i, q in enumerate(offs):
                p = end if i == len(offs) - 1 else ((q[0] + offs[i + 1][0]) / 2, (q[1] + offs[i + 1][1]) / 2)
                c1 = (last[0] + 2 / 3 * (q[0] - last[0]), last[1] + 2 / 3 * (q[1] - last[1]))
                c2 = (p[0] + 2 / 3 * (q[0] - p[0]), p[1] + 2 / 3 * (q[1] - p[1]))
                yield ("C", c1, c2, p)
                last = p
        elif verb in ("closePath", "endPath"):
            yield ("Z",)
            last = start


def polylines(path, step=0.15):
    """Flatten a path into closed polylines (one per contour)."""
    out, cur, last = [], [], None
    for seg in segments(path):
        kind = seg[0]
        if kind == "M":
            if len(cur) > 2:
                out.append(cur)
            cur = [seg[1]]
            last = seg[1]
        elif kind == "L":
            cur.append(seg[1])
            last = seg[1]
        elif kind == "C":
            c1, c2, p = seg[1:]
            p0 = last
            d = length(sub(c1, p0)) + length(sub(c2, c1)) + length(sub(p, c2))
            m = max(4, int(d / step))
            for k in range(1, m + 1):
                t = k / m
                u = 1 - t
                cur.append((u**3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t**3 * p[0],
                            u**3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t**3 * p[1]))
            last = p
        elif kind == "Z":
            if len(cur) > 2:
                out.append(cur)
            cur = []
    if len(cur) > 2:
        out.append(cur)
    # drop a repeated closing point
    clean = []
    for c in out:
        if length(sub(c[0], c[-1])) < 1e-6:
            c = c[:-1]
        # remove near-duplicate consecutive points
        d = [c[0]]
        for p in c[1:]:
            if length(sub(p, d[-1])) > 1e-4:
                d.append(p)
        if len(d) > 2:
            clean.append(d)
    return clean


# ---------------------------------------------------------------- smoothing: polylines to a few cubics


def _corners(poly, angle=32.0, reach=1.2):
    """Indices of sharp corners on a closed polyline: where the direction over `reach` units
    before and after the point differs by more than `angle` degrees."""
    n = len(poly)

    def walk(i, dist, direction):
        j, acc = i, 0.0
        while acc < dist:
            k = (j + direction) % n
            acc += length(sub(poly[k], poly[j]))
            j = k
            if j == i:
                break
        return j

    turn = []
    for i in range(n):
        a = poly[walk(i, reach, -1)]
        b = poly[walk(i, reach, +1)]
        u, v = unit(sub(poly[i], a)), unit(sub(b, poly[i]))
        c = max(-1.0, min(1.0, dot(u, v)))
        turn.append(math.degrees(math.acos(c)))
    cands = [i for i in range(n) if turn[i] > angle]
    # keep the sharpest point of each cluster
    keep = []
    for i in cands:
        lo, hi = walk(i, reach, -1), walk(i, reach, +1)
        window = []
        j = lo
        while True:
            window.append(j)
            if j == hi:
                break
            j = (j + 1) % n
        if all(turn[i] >= turn[j] for j in window) and not any(abs(i - k) <= 1 for k in keep):
            keep.append(i)
    return sorted(keep)


def _bez(b, t):
    u = 1 - t
    return (u**3 * b[0][0] + 3 * u * u * t * b[1][0] + 3 * u * t * t * b[2][0] + t**3 * b[3][0],
            u**3 * b[0][1] + 3 * u * u * t * b[1][1] + 3 * u * t * t * b[2][1] + t**3 * b[3][1])


def _bez1(b, t):
    u = 1 - t
    return (3 * (u * u * (b[1][0] - b[0][0]) + 2 * u * t * (b[2][0] - b[1][0]) + t * t * (b[3][0] - b[2][0])),
            3 * (u * u * (b[1][1] - b[0][1]) + 2 * u * t * (b[2][1] - b[1][1]) + t * t * (b[3][1] - b[2][1])))


def _bez2(b, t):
    u = 1 - t
    return (6 * (u * (b[2][0] - 2 * b[1][0] + b[0][0]) + t * (b[3][0] - 2 * b[2][0] + b[1][0])),
            6 * (u * (b[2][1] - 2 * b[1][1] + b[0][1]) + t * (b[3][1] - 2 * b[2][1] + b[1][1])))


def _chord(pts):
    u = [0.0]
    for a, b in zip(pts, pts[1:]):
        u.append(u[-1] + length(sub(b, a)))
    return [x / u[-1] for x in u] if u[-1] > 0 else u


def _generate(pts, u, t1, t2):
    p0, p3 = pts[0], pts[-1]
    C = [[0.0, 0.0], [0.0, 0.0]]
    X = [0.0, 0.0]
    for p, t in zip(pts, u):
        s = 1 - t
        b0, b1, b2, b3 = s**3, 3 * s * s * t, 3 * s * t * t, t**3
        A0, A1 = mul(t1, b1), mul(t2, b2)
        C[0][0] += dot(A0, A0)
        C[0][1] += dot(A0, A1)
        C[1][1] += dot(A1, A1)
        tmp = sub(p, add(add(mul(p0, b0 + b1), mul(p3, b2 + b3)), (0, 0)))
        X[0] += dot(A0, tmp)
        X[1] += dot(A1, tmp)
    C[1][0] = C[0][1]
    det = C[0][0] * C[1][1] - C[1][0] * C[0][1]
    seg = length(sub(p3, p0))
    if abs(det) > 1e-12:
        al = (X[0] * C[1][1] - X[1] * C[0][1]) / det
        ar = (C[0][0] * X[1] - C[1][0] * X[0]) / det
    else:
        al = ar = seg / 3
    if al < 1e-6 * seg or ar < 1e-6 * seg:
        al = ar = seg / 3
    return [p0, add(p0, mul(t1, al)), add(p3, mul(t2, ar)), p3]


def _max_error(pts, b, u):
    worst, split = 0.0, len(pts) // 2
    for i, (p, t) in enumerate(zip(pts, u)):
        d = length(sub(_bez(b, t), p))
        if d > worst:
            worst, split = d, i
    return worst, split


def _reparam(b, pts, u):
    out = []
    for p, t in zip(pts, u):
        q, q1, q2 = _bez(b, t), _bez1(b, t), _bez2(b, t)
        num = dot(sub(q, p), q1)
        den = dot(q1, q1) + dot(sub(q, p), q2)
        out.append(min(1.0, max(0.0, t - num / den)) if abs(den) > 1e-12 else t)
    return out


def _tangent(pts, i, direction, reach=0.8):
    """Unit tangent at pts[i] looking `direction` (+1 forward, -1 backward) over about `reach` units."""
    j, acc = i, 0.0
    while 0 <= j + direction < len(pts) and acc < reach:
        acc += length(sub(pts[j + direction], pts[j]))
        j += direction
    return unit(sub(pts[j], pts[i]))


def _fit(pts, t1, t2, err, depth=0):
    if len(pts) == 2 or depth > 24:
        d = length(sub(pts[-1], pts[0])) / 3
        return [[pts[0], add(pts[0], mul(t1, d)), add(pts[-1], mul(t2, d)), pts[-1]]]
    u = _chord(pts)
    b = _generate(pts, u, t1, t2)
    e, split = _max_error(pts, b, u)
    if e < err:
        return [b]
    if e < err * 6:
        for _ in range(30):
            u = _reparam(b, pts, u)
            b = _generate(pts, u, t1, t2)
            e, split = _max_error(pts, b, u)
            if e < err:
                return [b]
    split = max(1, min(len(pts) - 2, split))
    tc = unit(sub(pts[split - 1], pts[split + 1]))
    if tc == (0.0, 0.0):
        tc = unit(sub(pts[split - 1], pts[split]))
    return _fit(pts[:split + 1], t1, tc, err, depth + 1) + _fit(pts[split:], mul(tc, -1), t2, err, depth + 1)


def fit_polyline(poly, err=0.02, angle=32.0):
    """Fit cubic curves to one closed polyline, keeping its sharp corners."""
    n = len(poly)
    corners = _corners(poly, angle)
    if not corners:
        # no corners: split at two far-apart points and keep the tangent smooth through them
        a, b = 0, n // 2
        runs = [poly[a:b + 1], poly[b:] + poly[:a + 1]]
        out = []
        for run in runs:
            i0 = poly.index(run[0])
            t1 = unit(sub(poly[(i0 + 2) % n], poly[(i0 - 2) % n]))
            i1 = poly.index(run[-1])
            t2 = unit(sub(poly[(i1 - 2) % n], poly[(i1 + 2) % n]))
            out += _fit(run, t1, t2, err)
        return out
    out = []
    for k, c in enumerate(corners):
        d = corners[(k + 1) % len(corners)]
        run = poly[c:d + 1] if d > c else poly[c:] + poly[:d + 1]
        if len(run) < 2:
            continue
        t1 = _tangent(run, 0, +1)
        t2 = _tangent(run, len(run) - 1, -1)
        out += _fit(run, t1, t2, err)
    return out


def smooth(path, err=0.02, angle=32.0):
    """Turn a polygon path into a path of a few cubic curves (corners kept)."""
    out = Path()
    for poly in polylines(path):
        if abs(_area(poly)) < 0.05:
            continue
        curves = fit_polyline(poly, err, angle)
        out.moveTo(*curves[0][0])
        for b in curves:
            out.cubicTo(*b[1], *b[2], *b[3])
        out.close()
    return pathops.simplify(out, fix_winding=True)


def _area(poly):
    return 0.5 * sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1]
                     for i in range(len(poly)))


# ---------------------------------------------------------------- boolean helpers

def union(*paths):
    out = Path()
    for p in paths:
        if p is not None:
            out = pathops.op(out, p, PathOp.UNION)
    return out


def minus(a, *bs):
    out = a
    for b in bs:
        if b is not None:
            out = pathops.op(out, b, PathOp.DIFFERENCE)
    return out


def grow(path, d):
    """The shape grown outward by d (round corners), for making clear cuts around it."""
    band = Path()
    band.addPath(path)
    band.stroke(2 * d, LineCap.ROUND_CAP, LineJoin.ROUND_JOIN, 4)
    band.convertConicsToQuads()
    return union(path, pathops.simplify(band, fix_winding=True))


# ---------------------------------------------------------------- SVG path in and out

_TOKEN = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]|-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def _affine(m, p):
    a, b, c, d, e, f = m
    return (a * p[0] + c * p[1] + e, b * p[0] + d * p[1] + f)


def matrix(tx=0, ty=0, rot=0, scale=1, ox=0, oy=0):
    """translate(tx ty) rotate(rot) scale(scale) translate(-ox -oy) as an affine matrix."""
    r = math.radians(rot)
    cs, sn = math.cos(r) * scale, math.sin(r) * scale
    return (cs, sn, -sn, cs, tx - cs * ox + sn * oy, ty - sn * ox - cs * oy)


def _arc_to_cubics(p0, rx, ry, phi, large, sweep_flag, p1):
    """SVG elliptical arc (endpoint form) as cubic Bézier segments."""
    if rx == 0 or ry == 0:
        return [(p0, p0, p1, p1)]
    phi = math.radians(phi)
    cp, sp = math.cos(phi), math.sin(phi)
    dx, dy = (p0[0] - p1[0]) / 2, (p0[1] - p1[1]) / 2
    x1p, y1p = cp * dx + sp * dy, -sp * dx + cp * dy
    rx, ry = abs(rx), abs(ry)
    lam = x1p**2 / rx**2 + y1p**2 / ry**2
    if lam > 1:
        rx, ry = rx * math.sqrt(lam), ry * math.sqrt(lam)
    num = rx**2 * ry**2 - rx**2 * y1p**2 - ry**2 * x1p**2
    den = rx**2 * y1p**2 + ry**2 * x1p**2
    co = math.sqrt(max(0, num / den)) if den else 0
    if large == sweep_flag:
        co = -co
    cxp, cyp = co * rx * y1p / ry, -co * ry * x1p / rx
    cx = cp * cxp - sp * cyp + (p0[0] + p1[0]) / 2
    cy = sp * cxp + cp * cyp + (p0[1] + p1[1]) / 2

    def ang(u, v):
        a = math.atan2(u[0] * v[1] - u[1] * v[0], u[0] * v[0] + u[1] * v[1])
        return a

    t1 = ang((1, 0), ((x1p - cxp) / rx, (y1p - cyp) / ry))
    dt = ang(((x1p - cxp) / rx, (y1p - cyp) / ry), ((-x1p - cxp) / rx, (-y1p - cyp) / ry))
    if not sweep_flag and dt > 0:
        dt -= 2 * math.pi
    elif sweep_flag and dt < 0:
        dt += 2 * math.pi
    segs = max(1, int(math.ceil(abs(dt) / (math.pi / 2) - 1e-9)))
    out = []
    d = dt / segs
    k = 4 / 3 * math.tan(d / 4)
    for i in range(segs):
        a0, a1 = t1 + i * d, t1 + (i + 1) * d

        def pt(a):
            x, y = rx * math.cos(a), ry * math.sin(a)
            return (cp * x - sp * y + cx, sp * x + cp * y + cy)

        def dpt(a):
            x, y = -rx * math.sin(a), ry * math.cos(a)
            return (cp * x - sp * y, sp * x + cp * y)

        q0, q3 = pt(a0), pt(a1)
        q1 = add(q0, mul(dpt(a0), k))
        q2 = sub(q3, mul(dpt(a1), k))
        out.append((q0, q1, q2, q3))
    return out


def parse(d, m=(1, 0, 0, 1, 0, 0)):
    """An SVG path string (absolute or relative M L H V C A Z) as a Path, through matrix m."""
    toks = _TOKEN.findall(d)
    p = Path()
    i, cmd = 0, None
    cur = start = (0.0, 0.0)

    def num():
        nonlocal i
        v = float(toks[i])
        i += 1
        return v

    while i < len(toks):
        if re.match(r"[A-Za-z]", toks[i]):
            cmd = toks[i]
            i += 1
            if cmd in "Zz":
                p.close()
                cur = start
                continue
        rel = cmd.islower()
        c = cmd.upper()
        base = cur if rel else (0.0, 0.0)
        if c == "M":
            cur = add(base, (num(), num()))
            start = cur
            p.moveTo(*_affine(m, cur))
            cmd = "l" if rel else "L"
        elif c == "L":
            cur = add(base, (num(), num()))
            p.lineTo(*_affine(m, cur))
        elif c == "H":
            x = num()
            cur = (cur[0] + x if rel else x, cur[1])
            p.lineTo(*_affine(m, cur))
        elif c == "V":
            y = num()
            cur = (cur[0], cur[1] + y if rel else y)
            p.lineTo(*_affine(m, cur))
        elif c == "C":
            c1 = add(base, (num(), num()))
            c2 = add(base, (num(), num()))
            cur = add(base, (num(), num()))
            p.cubicTo(*_affine(m, c1), *_affine(m, c2), *_affine(m, cur))
        elif c == "A":
            rx, ry, phi, large, sw = num(), num(), num(), num(), num()
            end = add(base, (num(), num()))
            for q0, q1, q2, q3 in _arc_to_cubics(cur, rx, ry, phi, int(large), int(sw), end):
                p.cubicTo(*_affine(m, q1), *_affine(m, q2), *_affine(m, q3))
            cur = end
        else:
            raise ValueError(f"unsupported path command {cmd}")
    return p


def transformed(path, m):
    out = Path()
    for seg in segments(path):
        q = [_affine(m, p) for p in seg[1:]]
        if seg[0] == "M":
            out.moveTo(*q[0])
        elif seg[0] == "L":
            out.lineTo(*q[0])
        elif seg[0] == "C":
            out.cubicTo(*q[0], *q[1], *q[2])
        elif seg[0] == "Z":
            out.close()
    return out


def to_svg(path, nd=2):
    """Path data with `nd` decimals, lines and cubics only."""
    def f(v):
        s = f"{v:.{nd}f}".rstrip("0").rstrip(".")
        return "0" if s in ("-0", "") else s
    out = []
    for seg in segments(path):
        if seg[0] == "Z":
            out.append("Z")
        else:
            out.append(seg[0] + " ".join(f(c) for p in seg[1:] for c in p))
    return "".join(out).replace(" -", "-")


# ---------------------------------------------------------------- a body with layers

class Body:
    """One continuous body: centre-line samples and the full width at each. Pieces of it are
    built from the same edge points, so neighbouring pieces meet exactly."""

    def __init__(self, pts, widths):
        self.pts, self.widths = pts, widths
        n = len(pts)
        self.L, self.R, self.T = [], [], []
        for i in range(n):
            a, b = pts[max(0, i - 2)], pts[min(n - 1, i + 2)]
            t = unit(sub(b, a))
            nx, ny = -t[1], t[0]
            w = widths[i] / 2
            x, y = pts[i]
            self.T.append(t)
            self.L.append((x + nx * w, y + ny * w))
            self.R.append((x - nx * w, y - ny * w))

    def _cap(self, i, r, start):
        x, y = self.pts[i]
        t = self.T[i]
        base = math.atan2(t[1], t[0])
        a0, a1 = (base - math.pi / 2, base - 3 * math.pi / 2) if start else (base + math.pi / 2, base - math.pi / 2)
        m = 48
        return [(x + r * math.cos(a0 + (a1 - a0) * k / m), y + r * math.sin(a0 + (a1 - a0) * k / m)) for k in range(1, m)]

    def piece(self, i0, i1, caps=("none", "none"), grow=0.0, inset=None):
        """Polygon of the body between samples i0 and i1, optionally grown by `grow` all round.
        `inset(i)` narrows the piece at sample i (each side), so a piece can end strictly inside
        a neighbouring one and the two never share an edge."""
        i0, i1 = max(0, i0), min(len(self.pts) - 1, i1)
        if grow or inset:
            L, R = [], []
            for i in range(i0, i1 + 1):
                t = self.T[i]
                nx, ny = -t[1], t[0]
                w = self.widths[i] / 2 + grow - (inset(i) if inset else 0)
                x, y = self.pts[i]
                L.append((x + nx * w, y + ny * w))
                R.append((x - nx * w, y - ny * w))
        else:
            L, R = self.L[i0:i1 + 1], self.R[i0:i1 + 1]
        ring = list(L)
        if caps[1] == "round":
            ring += self._cap(i1, self.widths[i1] / 2 + grow, False)
        ring += R[::-1]
        if caps[0] == "round":
            ring += self._cap(i0, self.widths[i0] / 2 + grow, True)
        p = Path()
        p.fillType = FillType.WINDING
        p.moveTo(*ring[0])
        for q in ring[1:]:
            p.lineTo(*q)
        p.close()
        return pathops.simplify(p, fix_winding=True)


def ease(t):
    """Smooth 0..1 ramp."""
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- Hobby's curves through knots

def _rho(a, b):
    """Hobby's velocity: how long a handle should be for tangent angles a, b off the chord."""
    sa, sb, ca, cb = math.sin(a), math.sin(b), math.cos(a), math.cos(b)
    num = 2 + math.sqrt(2) * (sa - sb / 16) * (sb - sa / 16) * (ca - cb)
    den = 1 + (math.sqrt(5) - 1) / 2 * ca + (3 - math.sqrt(5)) / 2 * cb
    return num / den


def _hobby_run(pts, h_start, h_end):
    """Hobby's open curve through pts with given end directions; interior directions are solved
    so curvature runs on smoothly (METAFONT's 'mock curvature' equations, tension 1)."""
    n = len(pts) - 1
    d = [math.dist(pts[k], pts[k + 1]) for k in range(n)]
    ch = [math.atan2(pts[k + 1][1] - pts[k][1], pts[k + 1][0] - pts[k][0]) for k in range(n)]
    wrap = lambda a: math.atan2(math.sin(a), math.cos(a))
    psi = [0.0] + [wrap(ch[k] - ch[k - 1]) for k in range(1, n)] + [0.0]
    th0 = wrap(math.radians(h_start) - ch[0])
    phn = wrap(ch[n - 1] - math.radians(h_end))
    if n == 1:
        th, ph = [th0], [None, phn]
    else:
        # tridiagonal system in theta_1..theta_{n-1}
        a, b, c, r = [], [], [], []
        for k in range(1, n):
            A, B, C, D = 1 / d[k - 1], 2 / d[k - 1], 2 / d[k], 1 / d[k]
            rhs = -B * psi[k] - D * psi[k + 1]
            lo, mid, hi = A, B + C, D
            if k == 1:
                rhs -= A * th0
                lo = 0.0
            if k == n - 1:
                rhs -= D * (-phn)
                hi = 0.0
            a.append(lo); b.append(mid); c.append(hi); r.append(rhs)
        m = len(b)
        for i in range(1, m):  # Thomas algorithm
            w = a[i] / b[i - 1]
            b[i] -= w * c[i - 1]
            r[i] -= w * r[i - 1]
        x = [0.0] * m
        x[-1] = r[-1] / b[-1]
        for i in range(m - 2, -1, -1):
            x[i] = (r[i] - c[i] * x[i + 1]) / b[i]
        th = [th0] + x
        ph = [None] + [-psi[k] - th[k] for k in range(1, n)] + [phn]
    segs = []
    for k in range(n):
        t, f = th[k], ph[k + 1]
        ra, rb = _rho(t, f) / 3 * d[k], _rho(f, t) / 3 * d[k]
        a0, a1 = ch[k] + t, ch[k] - f
        c1 = (pts[k][0] + ra * math.cos(a0), pts[k][1] + ra * math.sin(a0))
        c2 = (pts[k + 1][0] - rb * math.cos(a1), pts[k + 1][1] - rb * math.sin(a1))
        segs.append((c1, c2, pts[k + 1]))
    return segs


def hobby_path(knots):
    """Knots (x, y, heading or None). Headings are kept where given (always at both ends);
    elsewhere Hobby's equations choose them, so the curve bends evenly."""
    segs, start = [], 0
    for i in range(1, len(knots)):
        if knots[i][2] is not None or i == len(knots) - 1:
            run = knots[start:i + 1]
            segs += _hobby_run([(k[0], k[1]) for k in run], run[0][2], run[-1][2])
            start = i
    return segs
