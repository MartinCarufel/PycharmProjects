*** Settings ***
Documentation    Test all sensing when Ignition is Off
Library  Dialogs

Test Setup  Run Keywords  set ignition off  IGNITION  OFF  ON  OFF  AND  set door close  Door  Close  Open  Close


*** Test Cases ***

Sense Driver door
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_front_door
    ${sensing} =  set variable  Driver Door open and close
    ${exp_status} =  set variable  5
    log to console  Ceci est le test ${TEST NAME}
    pause execution  ${TEST NAME}\nFaire ${sensing} ${exp_status}x
    ${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
    should be equal  ${nb_cycle}  ${5}

Sense Rear Driver door
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_rear_door
    #set global variable  ${sensing}  Ignition
    ${sensing} =  set variable  Rear Driver Door open and close
    ${exp_status} =  set variable  5
    log to console  Ceci est le test ${TEST NAME}
    pause execution  Faire ${sensing} ${exp_status}x
    ${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
    should be equal  ${nb_cycle}  ${5}

Sense Trunk
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_trunk
    ${sensing} =  set variable  Trunk open and close
    ${exp_status} =  set variable  5
    log to console  Ceci est le test ${TEST NAME}
    pause execution  Faire ${sensing} ${exp_status}x
    ${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
    should be equal  ${nb_cycle}  ${5}

Sense Rear Passenger door
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_rear_door
    ${sensing} =  set variable  Rear Passenger Door open and close
    ${exp_status} =  set variable  5
    log to console  Ceci est le test ${TEST NAME}
    pause execution  Faire ${sensing} ${exp_status}x
    ${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
    should be equal  ${nb_cycle}  ${5}

Sense Passenger door
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_front_door
    ${sensing} =  set variable  Passenger Door open and close
    ${exp_status} =  set variable  5
    log to console  Ceci est le test ${TEST NAME}
    pause execution  Faire ${sensing} ${exp_status}x
    ${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
    should be equal  ${nb_cycle}  ${5}

Sense hood
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_hood
    ${sensing} =  set variable  hood open and close
    ${exp_status} =  set variable  5
    log to console  Ceci est le test ${TEST NAME}
    pause execution  Faire ${sensing} ${exp_status}x
    ${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
    should be equal  ${nb_cycle}  ${5}

*** Keywords ***
continue
    [Tags]    DEBUG
    [Arguments]  ${sensing}  ${exp_status}  @{sensestatus}

    :for  ${i}  in range  99999
        \  ${status} =  get selection from user  D2D status de ${sensing}  @{sensestatus}  #Remplacer par get D2D status
        \  ${exit}=  get selection from user  Le status de ${sensing} est ${status} l'etat attendu est ${exp_status}\nReprende le test ?  Yes  No
        \  exit for loop if  '${exit}' == 'No'

count sensing
    [Arguments]  ${sensing}
    ${count} =  get value from user  Indiquer le nombre de cycle ${sensing}  #Remplacer par get D2D status
    ${count} =  convert to integer  ${count}
    [Return]  ${count}

set ignition off
    [Arguments]  ${sensing}  ${exp_status}  @{sensestatus}
    ${sensing} =  set variable  Ignition
    ${exp_status} =  set variable  OFF
    pause execution  Mettre ${sensing} à ${exp_status}
    :for  ${i}  in range  99999
        \  ${status} =  get selection from user  D2D status de ${sensing}  @{sensestatus}  #Remplacer par get D2D status
        \  ${exit}=  get selection from user  Le status de ${sensing} est ${status} l'etat attendu est ${exp_status}\nReprende le test ?  Yes  No
        \  exit for loop if  '${exit}' == 'No'

set door close
    [Arguments]  ${sensing}  ${exp_status}  @{sensestatus}
    ${sensing} =  set variable  Door
    ${exp_status} =  set variable  Close
    pause execution  Mettre ${sensing} à ${exp_status}
    :for  ${i}  in range  99999
        \  ${status} =  get selection from user  D2D status de ${sensing}  @{sensestatus}  #Remplacer par get D2D status
        \  ${exit}=  get selection from user  Le status de ${sensing} est ${status} l'etat attendu est ${exp_status}\nReprende le test ?  Yes  No
        \  exit for loop if  '${exit}' == 'No'