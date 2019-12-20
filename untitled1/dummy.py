:for    ${i}  in range  ${3}
    \    D2D2 Car Finder
    \    sleep  20s
    \    ${result} =  D2D2 Is Car Finder On  ${25}
    \    log to console  D2D2 Is Panic On : ${result}
    \    Should Be True    ${result}    
    \    D2D2 Unlock and disarm
    \    sleep  5