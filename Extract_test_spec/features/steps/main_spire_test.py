from behave import *
from main_spire import fetch_doc_in_dict, csv_construct_req
import json


@given(u'Test spec in word file format')
def step_impl(context):
    context.file = "./Unit_test/test_data/DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx"


@when(u'process the word file')
def step_impl(context):
    context.result = fetch_doc_in_dict(context.file)


@then(u'the extracted data is a dictionary')
def step_impl(context):
    assert isinstance(context.result, dict)


@then(u'the number of test case match')
def step_impl(context):

    with open("./Unit_test/test_data/testdata2.json", encoding="utf-8") as f:
        test_data = json.load(f)
    expected_result = test_data["1"]["number of test case"]
    assert len(context.result) == expected_result

@then(u'the number of test step match')
def step_impl(context):
    with open("./Unit_test/test_data/testdata2.json", encoding="utf-8") as f:
        test_data = json.load(f)
    expected_result = test_data["1"]["test cases"]["number of steps"]
    result = len(context.result["TC01001"])-1
    assert result == expected_result


@given(u'Test case in word')
def step_impl(context):
    file = "./Unit_test/test_data/Extrac requirement challenge.docx"
    context.test_case = fetch_doc_in_dict(file)



@when(u'processing requirement formating')
def step_impl(context):
    context.result = csv_construct_req(context.test_case["TC01001"][2][2])
    print(context.result)


@then(u'the result is formated as CSV')
def step_impl(context):
    expected_result = "Requirement(s): 6894_001, 6894_002, 6894_003, 6894_004, 6894_005\","
    assert context.result == expected_result




