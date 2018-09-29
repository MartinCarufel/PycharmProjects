*** Settings ***
Documentation    Suite description
Library  Dialogs

*** Test Cases ***
Do while same test
    [Tags]    DEBUG

    :for  ${i}  in range  99999
        \  pause execution  message = Allo
        \  ${exit}=  get selection from user  Reprende le test ?  Yes  No
        \  log to console  ${exit}
        \  exit for loop if  '${exit}' == 'No'

