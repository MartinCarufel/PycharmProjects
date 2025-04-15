import re
from spire.doc import *
from spire.doc.common import *


def fetch_doc_in_dict(document):
    tc_tables = {}
    for i in range(document.Sections.Count):
        section = document.Sections.get_Item(i)
        body_items = section.Body.ChildObjects
        j = 0
        while j < body_items.Count:
            item = body_items.get_Item(j)

            # Check if the item is a paragraph
            if item.DocumentObjectType == DocumentObjectType.Paragraph:

                para_text = item.Text.strip()
                match = re.match(r"TC[0-9]{5}", para_text)
                if match:
                    tc_code = match.group()

                    # Look ahead for the next table
                    for k in range(j + 1, body_items.Count):
                        next_item = body_items.get_Item(k)
                        if next_item.DocumentObjectType == DocumentObjectType.Table:
                            table = next_item
                            table_data = [para_text]

                            for r in range(table.Rows.Count):
                                if r > 0:
                                    row = table.Rows.get_Item(r)
                                    row_data = []
                                    for c in range(row.Cells.Count):
                                        cell = row.Cells.get_Item(c)
                                        cell_lines = []
                                        for p in range(cell.Paragraphs.Count):
                                            para = cell.Paragraphs.get_Item(p)
                                            para_text = para.Text.strip().replace('\r', '\n').replace('\v', '\n')
                                            cell_lines.append(para_text)
                                        cell_text = '\n'.join(cell_lines)
                                        row_data.append(cell_text)
                                    table_data.append(row_data)

                            tc_tables[tc_code] = table_data
                            break  # Stop looking once we found the next table
            j += 1
    return tc_tables


def debug_print(tc_tables):
    # Print results
    # print(tc_tables)
    for tc, table in tc_tables.items():
        print(f"\n{tc}")
        for row in table:
            print(row)


def main():
    # Load the document
    document = Document()
    document.LoadFromFile("DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx")
    # Dictionary to hold TC codes and their following tables
    tc_tables = fetch_doc_in_dict(document)
    debug_print(tc_tables)
    document.Close()

if __name__ == "__main__":
    main()