from behave import *
from spire.doc import *

import main_spire


@given(u'Test spec word document')
def step_impl(context):
    context.document = Document()
    context.document.LoadFromFile("DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx")


@when(u'The fetch doc method is called')
def step_impl(context):
    context.tc_table = main_spire.fetch_doc_in_dict(context.document)
    # print("WHEN")
    # print(context.tc_table)
    # raise NotImplementedError(u'STEP: When The fetch doc method is called')


@then(u'the fetch doc method return a structured dictionary')
def step_impl(context):
    assert isinstance(context.tc_table, dict), "The resulting return of fetch_doc_in_dict is not dictionary"

    # print(isinstance(context.tc_table, dict))
    # print("THEN")
    # raise NotImplementedError(u'STEP: Then the fetch doc method return a structured dictionary')

@then("the dictionary is not empty")
def the_dictionary_is_not_empty(context):
    assert len(context.tc_table) > 0, "The resulting dictionary is empty"

exp_sample = {'TC01001': ['TC01001 – Open the software and perform the 1st time setup on touch screen',
            ['Setup', 'Re-install the“softwarexxxxxx” with a new database.\r\nUse a touch screen Device during the test.\r\nCaresConnect user credential available to the SQA team', 'n/a', 'n/a', 'n/a'],
            ['1', 'Open the “MS Windows” start menu and search for “Sirios”.\r\nCheck if the icon is displayed in compliance with the marketing branding guidelines as below:\r\n', '6894_005', 'The product name “Straumann SIRIOS” and the product icon shall be displayed in compliance with the marketing branding guidelines.', 'Observation/ Screenshot'],
            ['2', 'On the desktop, select the “Straumann SIRIOS” shortcut icon using the touchscreen.\r\nCheck if the icon is displayed in compliance with the marketing branding guidelines as below:\r\n', '6894_005, 6894_007', 'The software shall respond to the touchscreen inputs and select the icon.\r\nThe product name “Straumann SIRIOS” and the product icon shall be displayed in compliance with the marketing branding guidelines.', 'Observation/ Screenshot'],
            ['3', 'Double click and start the software using the “touchscreen”.\r\nCheck if the splash Screen is displayed in compliance with the marketing branding guidelines as below:\r\n', '6894_004, 6894_007', 'The software shall respond to the touchscreen inputs, the Splash Screen shall be displayed and includes the following elements:\r\nThe text “Straumann SIRIOS™️”\r\nThe loading bar using “green” color.', 'Observation/ Screenshot'],
            ['4', 'Perform all the steps of the 1st time setup using the touchscreen.', '6894_007', 'The software shall respond to the touchscreen inputs and the 1st time setup shall guide the user to:\r\nSet the Clinic information.\r\nSet up the Cares Connect access.\r\nCreate a dentist account', 'Observation/ Screenshot'],
            ['5', 'Go to the login page, and log in using the touchscreen.', '6894_004, 6894_007', 'The login page shall feature the user that was created, and the login shall occur thought touchscreen inputs.', 'Observation/ Screenshot'],
            ['6', 'Using the touchscreen, on the window bar of the software, perform the following actions:\r\nRestore and slide the window to the left, then to the right.\r\nMaximize the window.\r\nMinimize the window.\r\nClick on Exit and shut down the software.', '6894_006, 6894_007', 'The software shall respond to the touchscreen inputs.\r\nThe window bar of the software shall allow the software to be minimized, maximized.\r\nThe software shall be shut down from the main window.', 'Observation/ Screenshot']],
        'TC01002': ['TC01002 – Scan Workflow on touch screen',
            ['Setup', 'The case has to be performed using the touch screen\r\nCreate a case with one scan body. And go to the scan step.\r\nUse a model with the scan body on the corresponding teeth.', 'n/a', 'n/a', 'n/a'],
            ['1', 'Scan the lower arch.\r\nUsing the touchscreen, zoom, rotate and pan the preview mesh.', '6894_007', 'The user can zoom, rotate and pan the preview mesh.', 'Observation/ Result documentation'],
            ['2', 'Double touch the scan 3D view.', '6894_007', 'The user can reset the preview mesh to centered position and the default zoom level.', 'Observation/ Result documentation'],
            ['3', 'Scan the upper and Bite, proceed to the review step.\r\nOn Display option, use the sliders to show/hide the lower and upper arch.\r\nTurn on the monochrome mode.', '6894_007', 'The user can show/hide the lower and upper arch.\r\nThe model is on monochrome.', 'Observation / Screenshot'],
            ['4', 'Using the touchscreen, open the Tooth tagging toolkit and assign the scan body.', '6894_007', 'The user can validate the implants with the scan body.', 'Observation / Screenshot'],
            ['5', 'Proceed to export view, zoom and rotate the preview mesh of lower, upper and occlusion scan.', '6894_007', 'The user can zoom and rotate the preview scan.', 'Observation/ Result documentation']],
        'TC01003': ['TC01003 – Authorized Scanners',
            ['Setup', 'One compatible scanner (Straumann branded) and one non-compatible scanner (Allied Star branded).\r\nCreate a case or a quick scan and proceed to the scan step.', 'n/a', 'n/a', 'n/a'],
            ['1', 'From the scanner list, connect to a non-compatible scanner.', '6894_002', 'The scanner shall not be connected,\r\nA warning message shall inform that the scanner is not compatible.', 'Observation/ Screenshot'],
            ['2', 'From the scanner list, connect a compatible scanner.', '6894_002', 'The scanner shall be connected.', 'Observation/ Screenshot'],
            ['3', 'Perform a scan of lower, upper and bite.', '6894_002', 'The scans shall be completed', 'Observation/ Result documentation']],
        'TC01004': ['TC01004 – Display the software’s build version',
            ['Setup', 'n/a', 'n/a', 'n/a', 'n/a'],
            ['1', 'Open Straumann IOS.\r\nGo to Options > About.', '6894_001', "The software’s build version is displayed in the format x.x.x.xxxx\r\nThe number’s first 2 digits shall follow Allied star's requirement (1.0).\r\nThe 3rd and 4th digits shall be incremented as per the design and development process.", 'Observation/ Screenshot'],
            ['2', 'On the Windows task bar, show the hidden icons.\r\nHover the Straumann IOS server icon.', '6894_008', 'The tooltip is indicating the software’s build version in the format x.x.x.xxxx.\r\nThe displayed version matches the software version from the previous step.', 'Observation/ Screenshot']]}