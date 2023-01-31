import pandas as pd
from docxtpl import DocxTemplate

doc = DocxTemplate("QUF63-5448 Template CSV Validation Specifications (v1.2)_variable.docx")
tr_objectif = "The objective is ti test variable generated doc"
tr_scope = "DW-IO-100"
tr_requirement = "001, 002, 003, 004"

context = {"tr_objective": tr_objectif, "tr_scope": tr_scope, "tr_requirement_list": tr_requirement}
doc.render(context)
doc.save("file_with var.docx")


df = pd.read_excel("list_documents.xlsx", sheet_name="Sheet1")


for index, row in df.iterrows():
    context_2  = {
        'tr_objective': row['Objective'],
        'tr_scope': row['Scope'],
        'tr_requirement_list': row['Requirement']
        }
    doc.render(context_2)
    doc.save(f"doc_{index}.docx")
