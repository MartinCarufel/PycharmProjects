*** Keywords ***
Dictionary Should Not Be Empty
    [Arguments]    ${dictionary}
    ${length}=    Get Length    ${dictionary}
    Should Be True    ${length} > 0