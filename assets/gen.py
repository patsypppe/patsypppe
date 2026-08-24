#!/usr/bin/env python3
"""
Generate the terminal-style identity panel for the profile README.

Two SVGs, one per colour scheme, selected by <picture> + prefers-color-scheme.
No external fonts, no CSS, no script: GitHub's SVG sanitiser strips those, so
everything is a presentation attribute on the element itself.
"""

from pathlib import Path

FS = 15                      # font size
CW = 9.02                    # advance width of one char at FS in common mono faces
LH = 23                      # line height
PAD_X = 30
TITLEBAR = 40
TOP_GAP = 26
BOT_PAD = 26
WIDTH = 980

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": {
        "bg": "#0B0F14", "titlebar": "#12181F", "border": "#242C36",
        "text": "#C9D1D9", "muted": "#6E7681", "key": "#79C0FF",
        "accent": "#E3B341", "head": "#D2A8FF", "path": "#7EE787",
        "rule": "#2A323D", "title": "#8B949E",
    },
    "light": {
        "bg": "#FFFFFF", "titlebar": "#F6F8FA", "border": "#D0D7DE",
        "text": "#1F2328", "muted": "#57606A", "key": "#0550AE",
        "accent": "#9A6700", "head": "#8250DF", "path": "#116329",
        "rule": "#D0D7DE", "title": "#656D76",
    },
}

# Key/value rows under `cat profile.txt`. Padded to a common column below.
PROFILE = [
    ("role", "M.S. Computer Science, Indiana University (May 2027)"),
    ("now", "SDE Intern @ SparkFX, agent orchestration in TypeScript"),
    ("research", "3 peer-reviewed papers: vision, biosignals, LLM tuning"),
    ("where", "Bloomington, Indiana"),
]

STACK = [
    ("ml", "PyTorch  TensorFlow  Hugging Face  scikit-learn  OpenCV"),
    ("services", "Go  Python  TypeScript  Envoy  JSON-RPC  OpenTelemetry"),
    ("cloud", "AWS Lambda  API Gateway  DynamoDB  Terraform  Docker"),
    ("data", "PostgreSQL  Alembic  pandas  NumPy  SQL"),
    ("rigor", "mypy --strict  ruff  golangci-lint  pytest  go test -race"),
]

# Repo name -> one-line summary, in the order they are pinned.
FEATURED = [
    ("sentinel", "MCP conformance harness, and the server it grades"),
    ("meridian", "agent eval harness, pass^k, CI merge gate"),
    ("serverless-rideshare-aws", "six Lambda services, Terraform, WebSockets"),
    ("cricket-shot-classification", "ViT, 3D ResNet, physics-informed loss"),
    ("metaheuristic-llm-finetuning", "GA and whale optimization, 94.67%"),
    ("EMG-Dumbbell-press", "biosignal form classification, LSTM"),
]


def _kv(rows, gap=3):
    """Left-align values into one column, whatever the longest key is."""
    w = max(len(k) for k, _ in rows) + gap
    return [[("  " + k.ljust(w), "key"), (v, "text")] for k, v in rows]


def _ls(rows, gap=2):
    w = max(len(n) for n, _ in rows) + 1 + gap
    return [[("  " + (n + "/").ljust(w), "path"), (d, "muted")] for n, d in rows]


def _prompt(cmd):
    return [("pranav@github", "path"), (" ~ ", "muted"), ("$", "accent"), (" " + cmd, "text")]


LINES = [
    _prompt("whoami"),
    ("gap",),
    [("  Pranav T Pattanashetty", "text")],
    [("  Applied machine learning, and the infrastructure it runs on.", "muted")],
    ("gap",),
    _prompt("cat profile.txt"),
    ("gap",),
    *_kv(PROFILE),
    ("gap",),
    ("head", "  stack"),
    *_kv(STACK),
    ("gap",),
    _prompt("ls featured/"),
    ("gap",),
    *_ls(FEATURED),
    ("gap",),
    [("pranav@github", "path"), (" ~ ", "muted"), ("$", "accent"), (" █", "text")],
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(theme_name: str) -> str:
    c = THEMES[theme_name]
    body_lines = len(LINES)
    height = TITLEBAR + TOP_GAP + body_lines * LH + BOT_PAD

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" '
        f'aria-label="Terminal panel introducing Pranav T Pattanashetty">',
        "<title>Pranav T Pattanashetty, applied machine learning and infrastructure</title>",
        # panel
        f'<rect x="0.5" y="0.5" width="{WIDTH-1}" height="{height-1}" rx="10" '
        f'fill="{c["bg"]}" stroke="{c["border"]}"/>',
        # title bar
        f'<path d="M0.5 10.5 A10 10 0 0 1 10.5 0.5 H{WIDTH-10.5} A10 10 0 0 1 {WIDTH-0.5} 10.5 '
        f'V{TITLEBAR} H0.5 Z" fill="{c["titlebar"]}"/>',
        f'<line x1="0.5" y1="{TITLEBAR}" x2="{WIDTH-0.5}" y2="{TITLEBAR}" stroke="{c["border"]}"/>',
        # traffic lights
        f'<circle cx="22" cy="{TITLEBAR/2}" r="6" fill="#FF5F57"/>',
        f'<circle cx="43" cy="{TITLEBAR/2}" r="6" fill="#FEBC2E"/>',
        f'<circle cx="64" cy="{TITLEBAR/2}" r="6" fill="#28C840"/>',
        f'<text x="{WIDTH/2}" y="{TITLEBAR/2 + 4.5}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="13" fill="{c["title"]}">pranav@github: ~</text>',
    ]

    y = TITLEBAR + TOP_GAP + FS
    for line in LINES:
        if line == ("gap",):
            y += LH
            continue
        if isinstance(line, tuple) and line[0] == "head":
            label = line[1]
            out.append(
                f'<text y="{y:.1f}" font-family="{MONO}" font-size="{FS}" '
                f'xml:space="preserve"><tspan x="{PAD_X}" fill="{c["head"]}">'
                f'{esc(label)}</tspan></text>'
            )
            rx = PAD_X + (len(label) + 2) * CW
            ry = y - FS * 0.34
            out.append(
                f'<line x1="{rx:.1f}" y1="{ry:.1f}" x2="{WIDTH-PAD_X}" y2="{ry:.1f}" '
                f'stroke="{c["rule"]}"/>'
            )
            y += LH
            continue

        spans, col = [], 0
        for text, key in line:
            spans.append(
                f'<tspan x="{PAD_X + col*CW:.1f}" fill="{c[key]}">{esc(text)}</tspan>'
            )
            col += len(text)
        out.append(
            f'<text y="{y:.1f}" font-family="{MONO}" font-size="{FS}" '
            f'xml:space="preserve">{"".join(spans)}</text>'
        )
        y += LH

    out.append("</svg>")
    return "\n".join(out)


def widest() -> int:
    """Longest rendered line, for checking nothing overflows the panel."""
    n = 0
    for line in LINES:
        if isinstance(line, tuple):
            continue
        n = max(n, sum(len(t) for t, _ in line))
    return n


if __name__ == "__main__":
    here = Path(__file__).parent
    over = PAD_X * 2 + widest() * CW
    assert over <= WIDTH, f"content is {over:.0f}px wide, panel is {WIDTH}px"
    for name in THEMES:
        p = here / f"terminal-{name}.svg"
        p.write_text(build(name), encoding="utf-8")
        print(f"{p.name}  {p.stat().st_size:,} bytes")
