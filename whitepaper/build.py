#!/usr/bin/env python3
"""
Build aafl-whitepaper-v1.2.html + aafl-whitepaper-v1.2.pdf

Pipeline:
  1. Pandoc converts the v1.2 markdown body to HTML
  2. Post-process: tag figure captions, replace ASCII diagrams with inline SVGs
  3. Wrap in a kami long-doc-en template customized with v1.1.html palette
  4. WeasyPrint renders the HTML to PDF (A4, 45 pages typeset)

Run with:
  DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build.py
"""
import os
import re
import subprocess
import sys
from pathlib import Path

# ===== Paths (repo-relative; portable) =====
ROOT      = Path(__file__).resolve().parent
SRC_MD    = ROOT / "aafl-whitepaper-v1.2.md"
OUT_HTML  = ROOT / "aafl-whitepaper-v1.2.html"
OUT_PDF   = ROOT / "aafl-whitepaper-v1.2.pdf"
FIGURES   = ROOT / "figures"
TMP       = Path("/tmp/aafl-build")
TMP.mkdir(exist_ok=True)
BODY_FRAG = TMP / "v1.2-body-fragment.html"

# ===== Metadata =====
DOC_TITLE    = "AAFL — An Agent-Augmented Framework for Learning"
DOC_SUBTITLE = "Judgment, Gates, and Workplace Performance in the Agent&nbsp;Era"
AUTHOR       = "Ruchir Bakshi"
VERSION      = "v1.2"
DATE         = "2026-05-14"
PUBLISHER    = "instructionalai.org"
CITATION     = "Bakshi, R. (2026). AAFL: An Agent-Augmented Framework for Learning (v1.2). instructionalai.org."

# ===== Load inline SVG figures =====
HYBRID_STACK_SVG = (FIGURES / "aafl-hybrid-stack.svg").read_text(encoding="utf-8")
PHASE_GRID_SVG   = (FIGURES / "aafl-phase-grid.svg").read_text(encoding="utf-8")

# ===== CSS — v1.1 palette + kami long-doc-en print structure =====

CSS = r"""
:root {
  --bg:           #faf8f1;
  --bg-soft:      #f4efe1;
  --bg-card:      #fdfcf6;
  --rule:         #d8d2bf;
  --rule-soft:    #e8e3d2;
  --ink:          #14181f;
  --ink-soft:     #303641;
  --ink-mute:     #5a6270;
  --accent:       #1e3a5f;
  --accent-soft:  #2e5984;
  --accent-pale:  #e3e9f1;
  --warn:         #8a3b1e;
  --code-bg:      #f1ecdc;
  --code-fg:      #1a1d23;
  --serif: 'Newsreader', Charter, Georgia, Palatino, 'Times New Roman', serif;
  --sans:  'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif;
  --mono:  'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
}

@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

@page {
  size: A4;
  margin: 22mm 24mm 22mm 24mm;
  @top-right    { content: string(section-title); font-family: 'Inter', sans-serif; font-size: 8pt; color: #5a6270; letter-spacing: 0.05em; }
  @top-left     { content: "AAFL v1.2"; font-family: 'Inter', sans-serif; font-size: 8pt; color: #5a6270; letter-spacing: 0.05em; }
  @bottom-center { content: counter(page); font-family: Charter, Georgia, serif; font-size: 9pt; color: #5a6270; }
}
@page:first {
  @top-right { content: ""; }
  @top-left  { content: ""; }
  @bottom-center { content: ""; }
}
@page landscape { size: A4 landscape; margin: 18mm 22mm 18mm 22mm; }
.landscape-page { page: landscape; }

html, body { background: #ffffff; }
@media screen { html, body { background: var(--bg); } }

body {
  color: var(--ink);
  font-family: var(--serif);
  font-size: 10.5pt;
  line-height: 1.55;
  widows: 3;
  orphans: 3;
  font-feature-settings: "kern", "liga", "onum";
  text-rendering: optimizeLegibility;
}

@media screen {
  body { max-width: 210mm; margin: 0 auto; padding: 22mm 24mm; font-size: 12pt; }
}

/* ========== COVER ========== */
.cover {
  min-height: 230mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 30mm 0 10mm 0;
  break-after: page;
  text-align: center;
}
.cover-eyebrow {
  font-family: var(--sans);
  font-size: 9pt;
  color: var(--accent);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 600;
  margin-bottom: 20pt;
}
.cover-title {
  font-family: var(--serif);
  font-size: 32pt;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.1;
  letter-spacing: -0.015em;
  margin-bottom: 12pt;
}
.cover-subtitle {
  font-style: italic;
  font-family: var(--serif);
  font-size: 14pt;
  font-weight: 500;
  color: var(--accent);
  margin: 0 auto 24pt;
  max-width: 160mm;
  line-height: 1.35;
  text-wrap: balance;
}
.cover-byline {
  font-family: var(--sans);
  font-size: 10pt;
  color: var(--ink-mute);
  letter-spacing: 0.02em;
  line-height: 1.7;
}
.cover-byline strong { color: var(--ink); font-weight: 600; }
.cover-byline .sep { display: inline-block; margin: 0 6pt; opacity: 0.5; }
.cover-citation {
  font-family: var(--sans);
  font-size: 8.5pt;
  color: var(--ink-mute);
  margin-top: 30pt;
  letter-spacing: 0.01em;
  max-width: 140mm;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.55;
}

/* ========== HEADINGS ========== */
h1 {
  font-family: var(--serif);
  font-size: 22pt;
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -0.01em;
  margin: 0 0 12pt 0;
  border-left: 3pt solid var(--accent);
  padding-left: 12pt;
  color: var(--ink);
  break-after: avoid;
  string-set: section-title content();
}
h2 {
  font-family: var(--serif);
  font-size: 15pt;
  font-weight: 600;
  line-height: 1.25;
  margin: 22pt 0 9pt 0;
  color: var(--ink);
  break-after: avoid;
}
.chapter-heading { break-before: page; }
h3 {
  font-family: var(--serif);
  font-size: 12.5pt;
  font-weight: 600;
  line-height: 1.3;
  margin: 18pt 0 6pt 0;
  color: var(--ink-soft);
  break-after: avoid;
}
h4 {
  font-family: var(--sans);
  font-size: 10pt;
  font-weight: 600;
  letter-spacing: 0.03em;
  line-height: 1.35;
  margin: 14pt 0 5pt 0;
  color: var(--accent);
  text-transform: none;
  break-after: avoid;
}

/* ========== PARAGRAPHS ========== */
p { margin: 0 0 9pt 0; line-height: 1.55; color: var(--ink); widows: 2; orphans: 2; text-align: left; hyphens: auto; }
strong { font-weight: 600; color: var(--ink); }
em { font-style: italic; }
a { color: var(--accent); text-decoration: none; border-bottom: 0.5pt solid var(--accent-pale); }

/* ========== LISTS ========== */
ul, ol { margin: 6pt 0 9pt 0; padding-left: 18pt; line-height: 1.55; }
ul li, ol li { margin-bottom: 3pt; }
ul li::marker { color: var(--accent); }
ol li::marker { color: var(--accent); font-weight: 600; }

/* ========== QUOTE / HR ========== */
blockquote { border-left: 2.5pt solid var(--accent); margin: 12pt 0; padding: 4pt 0 4pt 16pt; color: var(--ink-soft); font-style: italic; line-height: 1.55; break-inside: avoid; }
hr { border: none; border-top: 0.5pt solid var(--rule); margin: 18pt 0; }

/* ========== CODE (preserved for inline `code` and remaining <pre> blocks that aren't diagrams) ========== */
code { font-family: var(--mono); font-size: 8.5pt; background: var(--code-bg); padding: 1pt 4pt; border-radius: 2pt; color: var(--code-fg); }
pre {
  font-family: var(--mono);
  font-size: 7pt;
  line-height: 1.3;
  background: var(--code-bg);
  border: 0.5pt solid var(--rule);
  border-radius: 4pt;
  padding: 10pt 12pt;
  margin: 14pt 0;
  color: var(--code-fg);
  break-inside: avoid;
  overflow-x: auto;
  white-space: pre;
  letter-spacing: 0;
}
pre code { background: transparent; padding: 0; font-size: inherit; color: inherit; }

/* ========== FIGURE SVG ========== */
.figure-svg {
  margin: 16pt 0 6pt 0;
  text-align: center;
  break-inside: avoid;
}
.figure-svg svg {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
  width: 165mm;
}

/* Figure caption (tagged by build-time post-processing) */
p.figure-caption {
  font-style: italic;
  font-size: 9pt;
  color: var(--ink-soft);
  line-height: 1.5;
  margin-top: 0;
  margin-bottom: 14pt;
  padding-left: 12pt;
  border-left: 1pt solid var(--accent-pale);
  text-align: left;
  break-inside: avoid;
}
p.figure-caption em:first-child {
  font-style: normal;
  font-weight: 600;
  color: var(--accent);
}

/* ========== TABLES ========== */
table { width: 100%; border-collapse: collapse; font-size: 9.5pt; margin: 14pt 0; break-inside: auto; line-height: 1.45; }
thead { background: var(--accent-pale); display: table-header-group; }
th { text-align: left; font-family: var(--sans); font-weight: 600; color: var(--ink); padding: 6pt 8pt; border-bottom: 1pt solid var(--accent); vertical-align: top; font-size: 9pt; }
td { padding: 5pt 8pt; border-bottom: 0.3pt solid var(--rule-soft); vertical-align: top; color: var(--ink); }
table.compact, .landscape-page table { font-size: 7.5pt; line-height: 1.35; }
table.compact th, .landscape-page table th { padding: 4pt 5pt; font-size: 7pt; }
table.compact td, .landscape-page table td { padding: 3pt 5pt; }
tbody tr:nth-child(even) td { background: rgba(228, 236, 245, 0.18); }

/* ========== PRINT: strip all tints for clean white-paper output ========== */
@media print {
  code { background: transparent; }
  pre  { background: transparent; }
  thead { background: transparent; }
  tbody tr:nth-child(even) td { background: transparent; }
}
"""

# ===== Cover HTML =====
COVER_HTML = f"""
<section class="cover">
  <div>
    <div class="cover-eyebrow">Whitepaper · {VERSION} · {DATE}</div>
    <h1 class="cover-title" style="border-left:none;padding-left:0;">{DOC_TITLE}</h1>
    <div class="cover-subtitle">{DOC_SUBTITLE}</div>
  </div>
  <div>
    <div class="cover-byline">
      <strong>{AUTHOR}</strong>
      <span class="sep">·</span>{VERSION}
      <span class="sep">·</span>{DATE}
      <br>{PUBLISHER}
    </div>
    <div class="cover-citation">
      © Ruchir Bakshi 2026, all rights reserved. Suggested citation: {CITATION}
    </div>
  </div>
</section>
"""

# ===== Pandoc convert =====
print("Running pandoc...")
subprocess.run([
    "pandoc", str(SRC_MD),
    "--from", "gfm+yaml_metadata_block",
    "--to", "html5",
    "--syntax-highlighting=none",
    "--output", str(BODY_FRAG),
    "--wrap=preserve",
    "--strip-comments",
], check=True)
body = BODY_FRAG.read_text(encoding="utf-8")

# ===== Post-process body =====

# 1. Tag figure-caption paragraphs (so CSS doesn't break inline italics)
body = re.sub(
    r'<p>(<em>Figure \d+ — alt-text caption\.</em>)',
    r'<p class="figure-caption">\1',
    body,
)

# 2. Replace ASCII diagram <pre> blocks with inline SVG figures.
#    Diagram 1 (hybrid stack) is identified by the GOVERNANCE LAYER ASCII text.
#    Diagram 2 (phase grid) is identified by the ANALYZE header + GATE 1 cluster.
def replace_hybrid_stack(match):
    return f'<div class="figure-svg" id="figure-hybrid-stack">{HYBRID_STACK_SVG}</div>'
def replace_phase_grid(match):
    return f'<div class="figure-svg" id="figure-phase-grid">{PHASE_GRID_SVG}</div>'

body, n1 = re.subn(
    r'<pre><code>[^<]*?GOVERNANCE LAYER.*?</code></pre>',
    replace_hybrid_stack,
    body,
    flags=re.DOTALL,
)
body, n2 = re.subn(
    r'<pre><code>[^<]*?ANALYZE.*?Gate 1.*?</code></pre>',
    replace_phase_grid,
    body,
    flags=re.DOTALL,
)
print(f"  ASCII diagram replacements: hybrid-stack={n1}, phase-grid={n2}")
if n1 != 1 or n2 != 1:
    print("  WARNING: expected exactly 1 of each.", file=sys.stderr)

# 3. Strip the duplicate H1/byline at the top of the markdown body (cover already shows them)
body = re.sub(
    r'^<h1[^>]*>AAFL — An Agent-Augmented Framework for Learning</h1>\s*'
    r'<p><em>Judgment, Gates, and Workplace Performance in the Agent Era</em></p>\s*'
    r'<p><strong>Ruchir Bakshi</strong> · v1\.2 · 2026-05-14</p>\s*'
    r'<hr />\s*',
    '',
    body,
    count=1,
)

# 4. Add chapter-heading class to §-prefixed H2 headings (page break before)
def chapterize(match):
    full = match.group(0)
    text = match.group(2)
    if re.match(r'§\d+\.\s', text) and not re.match(r'§1\.5', text):
        return f'<h2 class="chapter-heading"{match.group(1)}>{text}</h2>'
    if text.startswith('Appendix '):
        return f'<h2 class="chapter-heading"{match.group(1)}>{text}</h2>'
    return full
body = re.sub(
    r'<h2(\s+id="[^"]*")>(§\d+(?:\.\d+)?\.[^<]+|Appendix [A-Z]\.[^<]+|About the Author|Foreword[^<]*|Executive Summary|Table of Contents)</h2>',
    chapterize,
    body,
)

# 5. Wrap Appendix C in a landscape-page section
appc_pattern = re.compile(
    r'(<h2 class="chapter-heading"[^>]*>Appendix B\..*?)(?=<hr />\s*<p><em>Whitepaper v1\.2)',
    re.DOTALL,
)
body = appc_pattern.sub(r'<section class="landscape-page">\1</section>', body)

# 6. Promote chapter-heading h2 elements to h1 (so they get the brand left bar)
def promote_h2_to_h1(match):
    cls = match.group(1) or ''
    attrs = match.group(2) or ''
    text = match.group(3)
    if (text.startswith('§') or text.startswith('Appendix ') or text == 'About the Author'
        or text == 'Executive Summary' or text == 'Table of Contents'
        or text.startswith('Foreword')):
        return f'<h1{cls}{attrs}>{text}</h1>'
    return match.group(0)
body = re.sub(
    r'<h2(\s+class="chapter-heading")?(\s+id="[^"]*")?>([^<]+)</h2>',
    promote_h2_to_h1,
    body,
)

# ===== Assemble final HTML =====
HEAD = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<!-- AAFL v1.2 - inline SVG diagrams for §2 hybrid stack and §4 phase grid - 2026-05-14 -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{DOC_TITLE} · {VERSION} · {AUTHOR}</title>
<meta name="author" content="{AUTHOR}">
<meta name="description" content="AAFL — An Agent-Augmented Framework for Learning. Judgment, gates, and workplace performance in the agent era. Independent IP, © Ruchir Bakshi 2026.">
<meta name="keywords" content="instructional design, AI agents, HITL gates, workplace performance, federal training, ADDIE, agent-augmented learning">
<meta name="generator" content="Kami">
<meta name="theme-color" content="#1e3a5f">
<style>{CSS}</style>
</head>
<body>
{COVER_HTML}
<main>
{body}
</main>
</body>
</html>
"""

OUT_HTML.write_text(HEAD, encoding="utf-8")
print(f"Wrote HTML: {OUT_HTML} ({OUT_HTML.stat().st_size} bytes)")

# ===== Render PDF =====
os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
from weasyprint import HTML  # noqa: E402
print("Rendering PDF (may take 30–60s)...")
HTML(filename=str(OUT_HTML)).write_pdf(str(OUT_PDF))
print(f"Wrote PDF: {OUT_PDF} ({OUT_PDF.stat().st_size} bytes)")
