from robot.api.deco import keyword
# from spire.doc import *
import spire.doc
import main_spire


@keyword("load document")
def x_fetch_doc_in_dict(doc):
    document = spire.doc.Document()
    document.LoadFromFile(doc)
    return document

@keyword("process the file")
def process_the_file(doc):
    return main_spire.fetch_doc_in_dict(doc)

@keyword("result is a dictionary")
def result_is_a_dictionary(obj):
    return  isinstance(obj, dict)


@keyword("result dict is not empty")
def result_is_not_empty(obj):
    return len(obj)

