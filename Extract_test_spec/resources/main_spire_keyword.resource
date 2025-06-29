*** Keywords ***
a test spec word file
    ${document}=    load document    ${document}
    Set Test Variable    ${document}

read and process the word file
    ${result}=    process the file    ${document}
    Set Test Variable    ${result}

the resulting is a dictionary structure
    ${result}=    result is a dictionary    ${result}
    Should Be True    ${result}

the dictionary is not empty
    ${len}    result dict is not empty    ${result}
    Should Be True    ${len}    >0