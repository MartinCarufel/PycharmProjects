from behave import *
import main_spire
from robot import run

"""
@Given('Test spec word doc "{filename}"')
def given_Test_spec_word_doc(context, filename):
    context.document = filename"""

@Given('Test spec word doc')
def given_Test_spec_word_doc(context):
    context.document = "DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx"
    
@When("process the data extracted")
def when_process_the_data_extracted(context):
    context.result = main_spire.fetch_doc_in_dict(context.document)
    run(["robot/main_spire.robot", f"--variable", f'DOCUMENT:{context.document}'])


@Then("the output is dictionary structure")
def the_output_is_dictionary_structure(context):
    is_dict = isinstance(context.result, dict)
    assert is_dict, "Output not a dict"



