# from spire.doc import *
# from spire.doc.common import *

from docx import Document
from docx.oxml.ns import qn
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table
import re
import csv


def get_doc_structure(doc):
    all_elements = []
    for child in doc._element.body.iterchildren():
        if isinstance(child, CT_P):
            all_elements.append(Paragraph(child, doc))
        elif isinstance(child, CT_Tbl):
            all_elements.append(Table(child, doc))
    return all_elements

def get_table(file_structure, para_index):
    para_count = 0
    for idx, elem in enumerate(file_structure):
        if isinstance(elem, Paragraph):
            if para_count == para_index:
                # Scan ahead to find the next table
                for next_elem in file_structure[idx + 1:]:
                    if isinstance(next_elem, Table):
                        return next_elem
            para_count += 1

    return None  # No table found after the specified paragraph index


# "DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx"

if __name__ == "__main__":
    # d = Word_collector("DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx")
    path_file = "DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx"
    document = Document(path_file)
    # document.LoadFromFile(path_file)
    # layoutDoc = FixedLayoutDocument(document)
    # layoutPage = layoutDoc.Pages[1]
    # page_text = layoutPage.Text
    # print(page_text)


    par = document.paragraphs
    for i in range(len(par)):
        if par[i].text.lower() == "test specifications":
            # print(i)
            # print(par[i].text)
            pass

    # Find the test case
    for i in range(len(par)):
        x = re.match("TC[0-9]{5}", par[i].text)
        if x != None:
            # print(i, end="- ")
            # print(par[i].text)
            pass


    s = get_doc_structure(document)
    # for idx, elem in enumerate(s):
    #     if isinstance(elem, Paragraph):
    #         print(elem.text)

    next_table = get_table(s, 9)
    for row in next_table.rows:
        print([cell.text for cell in row.cells])


"""
solution proposé
from docx import Document
from docx.oxml.ns import qn
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

def get_next_table_after_paragraph(doc, para_index):
    # This list holds all block-level elements in order: paragraphs and tables
    all_elements = []
    for child in doc._element.body.iterchildren():
        if isinstance(child, CT_P):
            all_elements.append(Paragraph(child, doc))
        elif isinstance(child, CT_Tbl):
            all_elements.append(Table(child, doc))

    # Now, go through elements and find the first table after para_index
    para_count = 0
    for idx, elem in enumerate(all_elements):
        if isinstance(elem, Paragraph):
            if para_count == para_index:
                # Scan ahead to find the next table
                for next_elem in all_elements[idx+1:]:
                    if isinstance(next_elem, Table):
                        return next_elem
            para_count += 1

    return None  # No table found after the specified paragraph index

# Usage example
doc = Document("your_document.docx")
table = get_next_table_after_paragraph(doc, 9)

if table:
    for row in table.rows:
        print([cell.text for cell in row.cells])
else:
    print("No table found after paragraph 9.")
"""