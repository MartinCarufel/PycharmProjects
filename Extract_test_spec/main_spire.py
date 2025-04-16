import re
import string
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
                                            new_para = []
                                            para = cell.Paragraphs.get_Item(p)
                                            para_text = para.Text.strip().replace('\r', '\n').replace('\v', '\n')
                                            # Check for double-quote and replace by opening-closing double quote
                                            if para.Text.count("\"") >= 2:
                                                if para.Text.count("\"") % 2 == 0:
                                                    quote = "opening"
                                                    for c in para.Text:
                                                        if c == "\"" and quote == "opening":
                                                            new_para.append("“")
                                                            quote = "close"
                                                        elif c == "\"" and quote == "close":
                                                            new_para.append("”")
                                                            quote = "open"
                                                        else:
                                                            new_para.append(c)
                                                else:
                                                    print(f"This paragraph <<{para_text}>> have even quotation")
                                                    raise Exception
                                                para_text = "".join(new_para)

                                            elif para.Text.count("\"") == 1:
                                                print(f"This paragraph <<{para_text}>> have even quotation")
                                                raise Exception
                                            cell_lines.append(para_text)
                                        cell_text = '\\n'.join(cell_lines)
                                        row_data.append(cell_text)
                                    table_data.append(row_data)

                            tc_tables[tc_code] = table_data
                            break  # Stop looking once we found the next table
            j += 1
    return tc_tables



def csv_construct_header(header_l):
    return ",".join(header_l) + "\n"


def csv_construct_tc(table):
    return f",\"Test Case\", \"{table}\",,,\n"

def csv_construct_test_step(id, text):
    return f",,,\"{id}\",\"{text}\\n\\n"


def csv_construct_req(text):
    # print("Test string:",text)
    pattern = r"\d{4}_\d{3}"
    req_list = re.findall(pattern, text)
    if len(req_list) > 0:
        output = ", ".join(req_list)
    else:
        output = "n/a"
    return f"Requirement(s): {output}\","


def csv_construct_exp_res(text):
    return f"\"{text}\\n\\n"


def csv_construct_tm_oe(text):
    return f"TM / OE:{text}\"\n"


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
    # debug_print(tc_tables)
    document.Close()
    # print(tc_tables)
    with open("export.csv", mode="w", encoding="UTF-8") as f:
        f.write(csv_construct_header(["ID","Work Item Type","Title","Test Step","Step Action","Step Expected"]))
        # Cycle test case
        for tc, table in tc_tables.items():
            f.write(csv_construct_tc(table[0]))

            # cycle test step in test case
            for i in range(1, len(table)):
                f.write(csv_construct_test_step(i, table[i][1]))
                f.write(csv_construct_req(table[i][2]))
                f.write(csv_construct_exp_res(table[i][3]))
                f.write(csv_construct_tm_oe(table[i][4]))
                # print(table[i][2])


if __name__ == "__main__":
    main()