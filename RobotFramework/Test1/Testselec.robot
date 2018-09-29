*** Settings ***
Documentation    Suite description
Library  Dialogs

*** Test Cases ***
Sense 1
    [Tags]    Test 1
    log to console  Ceci est le test 1
    continue
    Execute Manual Step  This test is pass od fail

Sense 2
    [Tags]    Test 2
    log to console  Ceci est le test 2
    Execute Manual Step  This test is pass od fail

Sense 3
    [Tags]    Test 3
    log to console  Ceci est le test
    continue
    Execute Manual Step  This test is pass od fail


aSense 1
    [Tags]    aTest 1
    log to console  Ceci est le test a1
    continue
    Execute Manual Step  This test is pass od fail


aSense 2
    [Tags]    aTest 2
    log to console  Ceci est le test a2
    continue
    Execute Manual Step  This test is pass od fail


*** Keywords ***
continue
    [Tags]    DEBUG

    :for  ${i}  in range  99999
        \  ${exit}=  get selection from user  Reprende le test ?  Yes  No
        \  log to console  ${exit}
        \  exit for loop if  '${exit}' == 'No'

