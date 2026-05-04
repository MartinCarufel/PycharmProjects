from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
import re

doc = Document("input.docx")

def iter_block_items(parent):
    """Yield paragraphs and tables in document order"""
    for child in parent.element.body.iterchildren():
        if child.tag.endswith('p'):
            yield Paragraph(child, parent)
        elif child.tag.endswith('tbl'):
            yield Table(child, parent)

current_tc = None

for block in iter_block_items(doc):

    # --- Paragraph ---
    if isinstance(block, Paragraph):
        text = block.text.strip()

        # Detect Header 2 with TCxxxxx
        match = re.search(r"(TC\d+)", text)
        if match:
            current_tc = match.group(1)
            print(f"\nFound TC: {current_tc}")

    # --- Table ---
    elif isinstance(block, Table):
        print(f"Processing table for {current_tc}")

        for r_idx, row in enumerate(block.rows):
            for c_idx, cell in enumerate(row.cells):
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        color = run.font.color

                        if color and color.rgb:
                            # Adjust RGB!
                            if color.rgb == (0, 176, 240):
                                print({
                                    "tc": current_tc,
                                    "row": r_idx,
                                    "col": c_idx,
                                    "text": run.text
                                })