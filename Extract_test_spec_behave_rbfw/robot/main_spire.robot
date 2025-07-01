*** Settings ***
Library    main_spire.py
Resource    ../resources/spire_main_keyword.resource


*** Variables ***
${document}    d.doc

*** Test Cases ***

Extract data from word document
    ${document}    Ask Word File
    ${data}=    fetch doc in dict    ${document}
    Log To Console    ${data}
    ${is_dict}=    Evaluate    isinstance(${data}, int)
    Should Be True    ${is_dict}
    Dictionary Should Not Be Empty    ${data}


