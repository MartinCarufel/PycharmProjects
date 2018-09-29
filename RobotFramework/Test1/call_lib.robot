*** Settings ***
Documentation    Suite description
Library  mylib.py

*** Test Cases ***
Call ext. lib bye
    [Tags]    DEBUG
    say hello


*** Keywords ***
