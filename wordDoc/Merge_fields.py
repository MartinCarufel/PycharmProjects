from __future__ import print_function
from mailmerge import MailMerge

template = "Template_field_merge.docx"
document = MailMerge(template)
document.merge(nom="Martin Carufel", adresse="72 Avenue Quintal, Laval")
document.write("Field_merge_output.docx")
document.merge_rows()