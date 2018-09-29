# User keyword is like function in many programming language. It can take arguments and retrun value
#
#Section available within user keyword
#[Documentation]
#[Tags]
#[Arguments]
#[Return]
#[Teardown]
#[Timeout]
#

# Argument can be also as part of the keywod name. The avantage is to create comprehansive keyword will passing the value

*** Settings ***
Documentation    User Keyword
Library   Dialogs

*** Test Cases ***
Test title
    [Tags]    DEBUG
    &{my_info} =   ask your info   Martin
    log to console    ${empty}
    log to console    ----------------------------------
    log to console    Your name is &{my_info}[Name]
    log to console    You have &{my_info}[age] years old
    log to console    You be &{my_info}[gender] human
    log to console    ----------------------------------
    log to console    ${empty}

Variable in keyword name
    # in following example the keywords including the arguments value in the keyword title
    send lock
    send unlock
    send trunk


*** Keywords ***

ask your info
    [Documentation]    This keyword ask for personal info and return a dictionary of info
    [Arguments]    ${name}
    ${age} =     get value from user    What is you age ?
    ${gender} =   get selection from user    What is your gender ?  Male    Female
    &{per_info} =    create dictionary    Name  ${name}  age  ${age}  gender  ${gender}
    [Return]  &{per_info}

send ${function}
    run keyword if    '${function}' == 'lock'    log to console    Do lock command
    run keyword if    '${function}' == 'unlock'    log to console    Do unlock command
    run keyword if    '${function}' == 'trunk'    log to console    Do trunk command

