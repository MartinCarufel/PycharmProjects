*** Settings ***
Library    ../resources/main_spire_keyword.py
Resource    ../resources/main_spire_keyword.resource

*** Variables ***
${document}    DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx
${result}    ${none}

*** Test Cases ***

Test Fetch Doc Returns Empty Dict
    Given a test spec word file
    When read and process the word file
    Then the resulting is a dictionary structure
    And the dictionary is not empty



