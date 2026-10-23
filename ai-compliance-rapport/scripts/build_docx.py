#!/usr/bin/env python3
"""Zet een rapport in eenvoudige Markdown om naar een Word-bestand (.docx).

Gebruik:
    python build_docx.py rapport.md rapport.docx

Ondersteunde Markdown:
    # Titel                 -> documenttitel
    ## Kop                  -> Kop 1 (Heading 1)
    ### Subkop              -> Kop 2 (Heading 2)
    #### Subsubkop          -> Kop 3 (Heading 3)
    gewone tekst            -> alinea (lege regel = nieuwe alinea)
    - punt / * punt         -> opsomming (2 of 4 spaties inspringen = dieper niveau)
    1. punt                 -> genummerde lijst (idem)
    | a | b |  (met |---|)  -> tabel; eerste rij is de kopregel
    > tekst                 -> kader (bijv. disclaimer)
    **vet** en *cursief*    -> binnen een regel

Opmaak: Arial 11, regelafstand 1,15, koppen niet vet, tabellen met dunne rand.
Vereist: python-docx (pip install python-docx).
"""
import re
import sys

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor
except ImportError:
    sys.exit("python-docx ontbreekt: installeer met 'pip install python-docx' en probeer opnieuw.")

FONT = "Arial"
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


def set_font(style, size, bold=False, color=None):
    style.font.name = FONT
    style.font.size = Pt(size)
    style.font.bold = bold
    if color:
        style.font.color.rgb = RGBColor.from_string(color)
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.append(fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), FONT)


def setup_styles(doc):
    normal = doc.styles["Normal"]
    set_font(normal, 11)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(6)
    set_font(doc.styles["Title"], 22, color="1F2A44")
    for name, size in (("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)):
        st = doc.styles[name]
        set_font(st, size, bold=False, color="1F2A44")
        st.paragraph_format.space_before = Pt(14 if name == "Heading 1" else 10)
        st.paragraph_format.space_after = Pt(6)
        st.paragraph_format.keep_with_next = True


def add_inline(par, text):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            par.add_run(part[2:-2]).bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            par.add_run(part[1:-1]).italic = True
        else:
            par.add_run(part)


def set_cell_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "808080")
        borders.append(el)
    tblPr.append(borders)


def shade(cell, fill="E8ECF3"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def add_table(doc, rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
    width = max(len(r) for r in cells)
    table = doc.add_table(rows=len(cells), cols=width)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_borders(table)
    for i, row in enumerate(cells):
        for j in range(width):
            cell = table.cell(i, j)
            par = cell.paragraphs[0]
            par.paragraph_format.space_after = Pt(2)
            add_inline(par, row[j] if j < len(row) else "")
            for run in par.runs:
                run.font.size = Pt(10)
            if i == 0:
                shade(cell)
    doc.add_paragraph()


def add_box(doc, text):
    table = doc.add_table(rows=1, cols=1)
    set_cell_borders(table)
    cell = table.cell(0, 0)
    shade(cell, "F4F4F4")
    par = cell.paragraphs[0]
    add_inline(par, text)
    for run in par.runs:
        run.font.size = Pt(9.5)
    doc.add_paragraph()


def build(md_text, out_path):
    doc = Document()
    setup_styles(doc)
    lines = md_text.splitlines()
    para, i = [], 0

    def flush():
        if para:
            add_inline(doc.add_paragraph(), " ".join(para))
            para.clear()

    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            flush()
        elif s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            add_table(doc, rows)
            continue
        elif s.startswith(">"):
            flush()
            box = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                box.append(lines[i].strip().lstrip(">").strip())
                i += 1
            add_box(doc, " ".join(box))
            continue
        elif s.startswith("#### "):
            flush(); doc.add_heading(s[5:], level=3)
        elif s.startswith("### "):
            flush(); doc.add_heading(s[4:], level=2)
        elif s.startswith("## "):
            flush(); doc.add_heading(s[3:], level=1)
        elif s.startswith("# "):
            flush(); doc.add_heading(s[2:], level=0)
        elif re.match(r"^[-*] ", s):
            flush()
            level = min((len(line) - len(line.lstrip())) // 2, 2)
            style = "List Bullet" if level == 0 else f"List Bullet {level + 1}"
            add_inline(doc.add_paragraph(style=style), s[2:])
        elif re.match(r"^\d+[.)] ", s):
            flush()
            level = min((len(line) - len(line.lstrip())) // 2, 2)
            style = "List Number" if level == 0 else f"List Number {level + 1}"
            add_inline(doc.add_paragraph(style=style), re.sub(r"^\d+[.)] ", "", s))
        else:
            para.append(s)
        i += 1
    flush()
    doc.save(out_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        build(f.read(), sys.argv[2])
    print(f"geschreven: {sys.argv[2]}")
