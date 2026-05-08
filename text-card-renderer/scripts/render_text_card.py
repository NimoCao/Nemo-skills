#!/usr/bin/env python3
import argparse
import json
import math
import shutil
import subprocess
import re
from html import escape
from pathlib import Path


FONT = "PingFang SC, Hiragino Sans GB, Arial, sans-serif"

THEMES = {
    "default": {
        "bg1": "#f7f3ec",
        "bg2": "#edf5f1",
        "ink": "#17212b",
        "muted": "#5f6b76",
        "card": "#ffffff",
        "accent": "#3c6255",
        "accent2": "#d96c5f",
        "soft": "#edf1ef",
    },
    "dark": {
        "bg1": "#111827",
        "bg2": "#1f2937",
        "ink": "#f8fafc",
        "muted": "#cbd5e1",
        "card": "#f8fafc",
        "accent": "#7dd3b0",
        "accent2": "#f48b7f",
        "soft": "#26313d",
    },
}


def text_width_units(s: str) -> float:
    units = 0.0
    for ch in s:
        if ord(ch) < 128:
            units += 0.56
        else:
            units += 1.0
    return units


def is_cjk(ch: str) -> bool:
    code = ord(ch)
    return (
        0x4E00 <= code <= 0x9FFF
        or 0x3400 <= code <= 0x4DBF
        or 0x3040 <= code <= 0x30FF
        or 0xAC00 <= code <= 0xD7AF
    )


def tokenize_for_wrap(text: str) -> list[str]:
    tokens = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\n":
            tokens.append("\n")
            i += 1
        elif ch.isspace():
            i += 1
        elif is_cjk(ch) or ch in "，。！？；：、（）《》“”‘’…":
            tokens.append(ch)
            i += 1
        else:
            m = re.match(r"[A-Za-z0-9_.:/@#%+-]+", text[i:])
            if m:
                tokens.append(m.group(0))
                i += len(m.group(0))
            else:
                tokens.append(ch)
                i += 1
    return tokens


def wrap_text(text: str, max_units: float) -> list[str]:
    if not text:
        return []
    lines = []
    current = ""
    for token in tokenize_for_wrap(text):
        if token == "\n":
            if current:
                lines.append(current)
                current = ""
            continue
        if token == "":
            continue
        needs_space = current and token and current[-1].isascii() and token[0].isascii()
        candidate = token if not current else current + (" " if needs_space else "") + token
        if text_width_units(candidate) <= max_units:
            current = candidate
            continue
        if current:
            lines.append(current)
        if text_width_units(token) <= max_units:
            current = token
        else:
            buf = ""
            for ch in token:
                cand = buf + ch
                if text_width_units(cand) > max_units and buf:
                    lines.append(buf)
                    buf = ch
                else:
                    buf = cand
            current = buf
    if current:
        lines.append(current)
    return lines


def text_block(x, y, text, size, color, weight=400, max_units=24, line_gap=1.35, anchor="start"):
    lines = wrap_text(str(text or ""), max_units)
    out = []
    for i, line in enumerate(lines):
        out.append(
            f'<text x="{x}" y="{y + i * size * line_gap:.1f}" text-anchor="{anchor}" '
            f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(line)}</text>'
        )
    return "\n".join(out), len(lines) * size * line_gap


def svg_shell(width, height, theme, body):
    t = theme
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["bg1"]}"/>
      <stop offset="1" stop-color="{t["bg2"]}"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#17212b" flood-opacity="0.12"/>
    </filter>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#bg)"/>
  <circle cx="{width * 0.08:.0f}" cy="{height * 0.92:.0f}" r="{min(width, height) * 0.18:.0f}" fill="{t["accent"]}" opacity="0.10"/>
  <circle cx="{width * 0.88:.0f}" cy="{height * 0.10:.0f}" r="{min(width, height) * 0.15:.0f}" fill="{t["accent2"]}" opacity="0.12"/>
  {body}
</svg>
'''


def layout_cover(spec, t):
    w, h = spec["width"], spec["height"]
    margin = w * 0.07
    title_size = spec.get("title_size") or max(42, min(82, int(w / 12)))
    subtitle_size = spec.get("subtitle_size") or max(18, int(title_size * 0.42))
    kicker = spec.get("kicker", "")
    body = []
    if kicker:
        body.append(text_block(margin, h * 0.18, kicker, subtitle_size, t["muted"], 500, 28)[0])
    body.append(text_block(margin, h * 0.34, spec.get("title", ""), title_size, t["ink"], 750, 10)[0])
    if spec.get("subtitle"):
        body.append(text_block(margin, h * 0.74, spec["subtitle"], subtitle_size, t["muted"], 450, 30)[0])
    return "\n".join(body)


def layout_cards(spec, t):
    w, h = spec["width"], spec["height"]
    cards = spec.get("cards", [])
    margin = w * 0.065
    body = [
        text_block(margin, h * 0.12, spec.get("title", ""), spec.get("title_size", 36), t["ink"], 750, 28)[0],
        text_block(margin, h * 0.18, spec.get("subtitle", ""), spec.get("subtitle_size", 20), t["muted"], 450, 44)[0],
    ]
    n = max(1, len(cards))
    gap = w * 0.035
    card_w = (w - margin * 2 - gap * (n - 1)) / n
    card_h = h * 0.25
    y = h * 0.34
    for i, card in enumerate(cards):
        x = margin + i * (card_w + gap)
        body.append(f'<g filter="url(#shadow)">')
        body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{card_w:.1f}" height="{card_h:.1f}" rx="22" fill="{t["card"]}"/>')
        body.append(text_block(x + card_w / 2, y + card_h * 0.33, card.get("title", ""), 30, t["ink"], 750, 9, anchor="middle")[0])
        body.append(text_block(x + card_w / 2, y + card_h * 0.58, card.get("label", ""), 22, t["accent"], 500, 12, anchor="middle")[0])
        body.append(text_block(x + card_w / 2, y + card_h * 0.80, card.get("body", ""), 16, t["muted"], 450, 18, anchor="middle")[0])
        body.append("</g>")
    if spec.get("footer"):
        footer_w = w * 0.44
        footer_x = (w - footer_w) / 2
        footer_y = h * 0.74
        body.append(f'<rect x="{footer_x:.1f}" y="{footer_y:.1f}" width="{footer_w:.1f}" height="{h * 0.12:.1f}" rx="24" fill="{t["ink"]}"/>')
        body.append(text_block(w / 2, footer_y + h * 0.075, spec["footer"], 24, "#ffffff", 700, 22, anchor="middle")[0])
    return "\n".join(body)


def layout_stack(spec, t):
    w, h = spec["width"], spec["height"]
    items = spec.get("items") or spec.get("cards", [])
    margin = w * 0.07
    body = [
        text_block(margin, h * 0.10, spec.get("title", ""), spec.get("title_size", 38), t["ink"], 750, 24)[0],
        text_block(margin, h * 0.15, spec.get("subtitle", ""), spec.get("subtitle_size", 21), t["muted"], 450, 42)[0],
    ]
    n = max(1, len(items))
    top = h * 0.24
    available = h * 0.56
    gap = h * 0.045
    item_h = (available - gap * (n - 1)) / n
    x = w * 0.19
    card_w = w * 0.63
    for i, item in enumerate(items):
        y = top + i * (item_h + gap)
        body.append('<g filter="url(#shadow)">')
        body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{card_w:.1f}" height="{item_h:.1f}" rx="26" fill="{t["card"]}"/>')
        cx = x + card_w * 0.11
        cy = y + item_h / 2
        color = [t["accent2"], t["accent"], "#3b6f9e", "#8b6fcb", "#b7791f"][i % 5]
        body.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{min(item_h * 0.28, 42):.1f}" fill="{color}" opacity="0.18"/>')
        body.append(text_block(cx, cy + 9, str(i + 1), 27, color, 750, 2, anchor="middle")[0])
        body.append(text_block(x + card_w * 0.20, y + item_h * 0.40, item.get("title", ""), 32, t["ink"], 750, 18)[0])
        body.append(text_block(x + card_w * 0.20, y + item_h * 0.68, item.get("body") or item.get("label", ""), 21, t["muted"], 450, 34)[0])
        body.append("</g>")
    if spec.get("footer"):
        body.append(text_block(w / 2, h * 0.90, spec["footer"], 27, t["ink"], 750, 28, anchor="middle")[0])
    return "\n".join(body)


def layout_quote(spec, t):
    w, h = spec["width"], spec["height"]
    margin = w * 0.09
    body = []
    body.append(text_block(margin, h * 0.28, spec.get("title", ""), spec.get("title_size", 64), t["ink"], 800, 12)[0])
    if spec.get("subtitle"):
        body.append(text_block(margin, h * 0.58, spec["subtitle"], spec.get("subtitle_size", 28), t["accent"], 650, 22)[0])
    if spec.get("body"):
        body.append(text_block(margin, h * 0.72, spec["body"], spec.get("body_size", 22), t["muted"], 450, spec.get("body_max_units", 22))[0])
    return "\n".join(body)


def layout_note(spec, t):
    w, h = spec["width"], spec["height"]
    outer = spec.get("outer_margin", 54)
    pad_x = spec.get("pad_x", 58)
    pad_y = spec.get("pad_y", 58)
    note_x = outer
    note_y = outer
    note_w = w - outer * 2
    note_h = h - outer * 2
    title = spec.get("title", "")
    date = spec.get("date", "")
    paragraphs = spec.get("paragraphs") or []
    if isinstance(spec.get("body"), str):
        paragraphs = spec["body"].split("\n\n")

    title_size = spec.get("title_size", 44)
    body_size = spec.get("body_size", 30)
    date_size = spec.get("date_size", 21)
    max_units = spec.get("body_max_units", 28)
    line_gap = spec.get("line_gap", 1.55)
    para_gap = spec.get("para_gap", 24)

    body = []
    body.append('<g filter="url(#shadow)">')
    body.append(f'<rect x="{note_x}" y="{note_y}" width="{note_w}" height="{note_h}" rx="34" fill="#fffdf8"/>')
    body.append(f'<rect x="{note_x}" y="{note_y}" width="{note_w}" height="92" rx="34" fill="#fff7d8"/>')
    body.append(f'<circle cx="{note_x + 36}" cy="{note_y + 46}" r="7" fill="#ffcc4d"/>')
    body.append(f'<circle cx="{note_x + 62}" cy="{note_y + 46}" r="7" fill="#ffdf7a"/>')
    body.append(f'<circle cx="{note_x + 88}" cy="{note_y + 46}" r="7" fill="#ffeaa7"/>')
    if date:
        body.append(text_block(note_x + note_w - pad_x, note_y + 55, date, date_size, "#9a8f72", 450, 18, anchor="end")[0])
    y = note_y + pad_y + 96
    if title:
        block, used = text_block(note_x + pad_x, y, title, title_size, "#1f2933", 760, spec.get("title_max_units", 12), 1.22)
        body.append(block)
        y += used + 34
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        block, used = text_block(note_x + pad_x, y, p, body_size, "#2f3a45", 430, max_units, line_gap)
        body.append(block)
        y += used + para_gap
    body.append("</g>")
    return "\n".join(body)


LAYOUTS = {
    "cover": layout_cover,
    "cards": layout_cards,
    "stack": layout_stack,
    "quote": layout_quote,
    "note": layout_note,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    width = int(spec.get("width", 1200))
    height = int(spec.get("height", 675))
    spec["width"] = width
    spec["height"] = height
    theme = THEMES.get(spec.get("theme", "default"), THEMES["default"])
    layout = spec.get("layout", "cards")
    if layout not in LAYOUTS:
        raise SystemExit(f"Unsupported layout: {layout}")

    body = LAYOUTS[layout](spec, theme)
    svg = svg_shell(width, height, theme, body)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    svg_path = out.with_suffix(".svg")
    svg_path.write_text(svg, encoding="utf-8")

    sips = shutil.which("sips")
    if not sips:
        print(f"Wrote SVG only: {svg_path} (sips not found)")
        return
    subprocess.run([sips, "-s", "format", "png", str(svg_path), "--out", str(out)], check=True)
    print(f"Wrote {out}")
    print(f"Wrote {svg_path}")


if __name__ == "__main__":
    main()
