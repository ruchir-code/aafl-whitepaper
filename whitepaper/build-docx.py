#!/usr/bin/env python3
"""
Build aafl-whitepaper-v1.2.docx from the v1.2 markdown source.

Pipeline:
  1. Convert the two inline SVG diagrams to high-res PNGs (cairosvg)
  2. Pre-process the markdown: replace the two ASCII diagram blocks with
     image references pointing at the freshly rendered PNGs
  3. Run pandoc to produce a styled .docx

Run with:
  DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build-docx.py
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT     = Path(__file__).resolve().parent
SRC_MD   = ROOT / "aafl-whitepaper-v1.2.md"
OUT_DOCX = ROOT / "aafl-whitepaper-v1.2.docx"
FIGURES  = ROOT / "figures"
TMP      = Path("/tmp/aafl-docx-build")
TMP.mkdir(exist_ok=True)

# ===== 1. SVG → PNG =====
os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
import cairosvg  # noqa: E402

SVG_TO_PNG = [
    (FIGURES / "aafl-hybrid-stack.svg", TMP / "aafl-hybrid-stack.png"),
    (FIGURES / "aafl-phase-grid.svg",   TMP / "aafl-phase-grid.png"),
]
for svg_path, png_path in SVG_TO_PNG:
    print(f"Rendering {svg_path.name} → {png_path.name}")
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(png_path),
        output_width=1800,  # high-res for print quality in Word
    )

# ===== 2. Pre-process markdown =====
md = SRC_MD.read_text(encoding="utf-8")

# Replace ASCII fenced code blocks containing the diagrams with image references.
# The hybrid-stack ASCII contains "GOVERNANCE LAYER"; the phase-grid contains "Gate 1" + "ANALYZE".
def replace_fenced(pattern_inside, png_path, alt_text):
    """Replace a ``` ... ``` fenced block matching pattern_inside with a markdown image."""
    pattern = re.compile(
        r'```[ \t]*\n([^`]*?' + pattern_inside + r'[^`]*?)\n```',
        re.DOTALL,
    )
    img = f'![{alt_text}]({png_path.as_posix()})'
    return pattern, img

p1, img1 = replace_fenced(r'GOVERNANCE LAYER',  TMP / "aafl-hybrid-stack.png", "Figure 1 — AAFL Hybrid Stack")
p2, img2 = replace_fenced(r'Gate 1',            TMP / "aafl-phase-grid.png",   "Figure 2 — Eight HITL Gates Across the ADDIE Phases")

md, n1 = p1.subn(img1, md)
md, n2 = p2.subn(img2, md)
print(f"  Diagram replacements: hybrid-stack={n1}, phase-grid={n2}")
if n1 != 1 or n2 != 1:
    print("  WARNING: expected exactly 1 of each.", file=sys.stderr)

PRE_MD = TMP / "aafl-whitepaper-v1.2-docx-source.md"
PRE_MD.write_text(md, encoding="utf-8")

# ===== 3. Pandoc → DOCX =====
print("Running pandoc → docx...")
subprocess.run([
    "pandoc",
    str(PRE_MD),
    "--from",        "gfm+yaml_metadata_block",
    "--to",          "docx",
    "--output",      str(OUT_DOCX),
    "--toc",
    "--toc-depth",   "2",
    "--number-sections=false",
    "--wrap",        "preserve",
    "--standalone",
    f"--resource-path={TMP}:{ROOT}",
], check=True)

print(f"Wrote DOCX: {OUT_DOCX} ({OUT_DOCX.stat().st_size} bytes)")
