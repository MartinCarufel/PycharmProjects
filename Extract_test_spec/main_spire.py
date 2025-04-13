import re
from spire.doc import *
from spire.doc.documents import *
from spire.doc.fields import *

# Load the Word document
doc = Document()
doc.LoadFromFile("your_document.docx")

# Regex to match TC followed by 5 digits
pattern = re.compile(r"TC\d{5}")

# Store results
matches = []

# Flag to indicate next table after a match
looking_for_table = False
current_match_info = None

# Loop through all sections and body items
for section in doc.Sections:
    body_items = section.Body.ChildObjects
    i = 0
    while i < body_items.Count:
        item = body_items[i]

        # Check for matching paragraphs
        if isinstance(item, Paragraph):
            para_text = item.Text
            if pattern.search(para_text):
                print(f"Found match: {para_text}")
                current_match_info = {
                    "match_text": para_text,
                    "table": None,
                    "images": []
                }
                looking_for_table = True
                i += 1
                continue

        # If we're looking for a table after a match
        if looking_for_table:
            if isinstance(item, Table):
                current_match_info["table"] = item
                matches.append(current_match_info)
                current_match_info = None
                looking_for_table = False
            elif isinstance(item, Paragraph):
                # Check for images in paragraphs while looking
                for obj in item.ChildObjects:
                    if isinstance(obj, DocPicture):
                        current_match_info["images"].append(obj)

        i += 1

# Output result
for idx, match in enumerate(matches):
    print(f"\n--- Match {idx + 1} ---")
    print("Text:", match["match_text"])
    print("Table:", "Found" if match["table"] else "Not Found")
    print("Images:", f"{len(match['images'])} image(s) found")

    # If you want to save the found table and images, you could export them here
    # Example: match["table"].SaveToFile(...) or save images to disk
