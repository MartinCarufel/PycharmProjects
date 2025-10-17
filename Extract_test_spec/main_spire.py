import re
# import string
from spire.doc import Document, DocumentObjectType
# from spire.doc.common import *
from tkinter import filedialog
from datetime import datetime

def fetch_doc_in_dict(pathfile, extract_type):
    """
        Parses a Word document using Spire.Doc and extracts test case data.

        The function scans for paragraphs that match a test case ID pattern (e.g., "TC12345").
        Once a match is found, it looks ahead for the next table, parses its rows and cells,
        and stores structured content in a dictionary keyed by test case ID.

        Args:
            document (Document): A Spire.Doc Document object.

        Returns:
            dict: A dictionary mapping test case IDs to their corresponding table data.
                  Format: { "TCxxxxx": [title, [row1_data], [row2_data], ...] }
        """

    document = Document()
    document.LoadFromFile(pathfile)
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
                # print(para_text)
                if extract_type == "sirios":
                    match = re.match(r"TC[0-9]{5}", para_text)   # SIRIOS
                if extract_type == "dwos":
                    match = re.match(r"UC\d\d\d\.\d{1,2}", para_text)   # DWOS
                # print(match)
                if match:
                    tc_code = match.group()

                    # Look ahead for the next table
                    for k in range(j + 1, body_items.Count):
                        if extract_type == "sirios":
                            next_item = body_items.get_Item(k)    # SIRIOS
                        if extract_type == "dwos":
                            next_item = body_items.get_Item(k + 1)  # DWOS
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
                                        cell_text = '\r\n'.join(cell_lines)
                                        row_data.append(cell_text)
                                    table_data.append(row_data)

                            tc_tables[tc_code] = table_data
                            break  # Stop looking once we found the next table
            j += 1
    document.Close()
    return tc_tables


def ask_word_file():
    """
        Opens a file dialog to allow the user to select a Word document.

        Returns:
            str: The selected file path.
        """
    return filedialog.askopenfilename()

def csv_construct_header(header_l):
    """
        Constructs the CSV header row.

        Args:
            header_l (list): List of header field names.

        Returns:
            str: Comma-separated header row.
        """
    return ",".join(header_l) + "\n"


def csv_construct_tc(table, extract_type):
    """
        Formats the title row for a test case in CSV.

        Args:
            table (str): Test case title or identifier.

        Returns:
            str: CSV row for the test case header.
        """
    print(table)
    if extract_type == "sirios":
        pattern = r"(TC\d{5})( \W )(.*)"           # SIRIOS
    if extract_type == "dwos":
        pattern = r"(UC\d\d\d\.\d{1,2})( \W )(.*)"   # DWOS
    split_title = re.split(pattern, table)
    # return f",\"Test Case\",\"{table}\",,,\n"
    return f",\"Test Case\",\"{split_title[1]} - {split_title[3]}\",,,\n"


def csv_setup_step(id, text):
    """
        Constructs a setup step row for a test case.

        Args:
            id (int): Step number.
            text (str): Description of the setup step.

        Returns:
            str: Formatted CSV line for the setup step.
        """
    return f",,,\"{id}\",\"Setup: {text}\r\n\r\n"


def csv_construct_test_step(id, text):
    """
        Constructs a normal test step row for a test case.

        Args:
            id (int): Step number.
            text (str): Step description.

        Returns:
            str: CSV formatted row for the test step.
        """
    return f",,,\"{id}\",\"{text}\r\n\r\n"


def csv_construct_req(text):
    """
        Extracts and formats requirement references from a text block.

        The expected format is numeric IDs separated by an underscore (e.g., 1234_001).

        Args:
            text (str): Input text possibly containing requirement IDs.

        Returns:
            str: CSV field for requirements. ex: 6900-001, 6900-002, 6900-003
        """
    # print("Test string:",text)
    pattern = r"\d{4}_\d{3}"
    req_list = re.findall(pattern, text)
    if len(req_list) > 0:
        output = ", ".join(req_list)
    else:
        output = "n/a"
    return f"Requirement(s): {output}\","


def csv_construct_exp_res(text):
    """
        Constructs the expected result field for a test step.

        Args:
            text (str): Expected result text.

        Returns:
            str: Formatted expected result CSV field.
        """
    return f"\"{text}\r\n\r\n"


def csv_construct_tm_oe(text):
    """
        Constructs the Test Method/Objective Evidence field.

        Args:
            text (str): TM/OE information.

        Returns:
            str: Formatted TM/OE CSV field.
        """
    return f"Test Method/Objective Evidence: {text}\"\n"


def debug_print(tc_tables):
    """
        Prints the content of test case tables to console (for debugging).

        Args:
            tc_tables (dict): Dictionary of test cases and their associated table data.
        """
    # Print results
    # print(tc_tables)
    for tc, table in tc_tables.items():
        print(f"\n{tc}")
        for row in table:
            print(row)


def main():
    """
        Main function:
        - Prompts user to select a DOCX file
        - Extracts test cases and associated data
        - Exports the structured content to a CSV file
        """
    extract_type = "sirios"        # set to: sirios, dwos
    tc_tables = fetch_doc_in_dict(ask_word_file(), extract_type)
    # debug_print(tc_tables)
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d_%H%M%S")
    with open(f"export_{formatted_now}.csv", mode="w", encoding="UTF-8", newline='') as f:
        f.write(csv_construct_header(["ID","Work Item Type","Title","Test Step","Step Action","Step Expected"]))
        # Cycle test case
        for tc, table in tc_tables.items():
            f.write(csv_construct_tc(table[0], extract_type))

            # cycle test step in test case
            for i in range(1, len(table)):

                if table[i][0].lower() == "setup":
                    f.write(csv_setup_step(i, table[i][1]))
                else:
                    f.write(csv_construct_test_step(i, table[i][1]))
                f.write(csv_construct_req(table[i][2]))
                f.write(csv_construct_exp_res(table[i][3]))
                f.write(csv_construct_tm_oe(table[i][4]))
                # print(table[i][2])


if __name__ == "__main__":
    main()