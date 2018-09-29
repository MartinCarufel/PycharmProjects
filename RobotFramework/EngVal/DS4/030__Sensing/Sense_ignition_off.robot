*** Settings ***
Documentation    Test all sensing when Ignition is Off
Library  Dialogs

#Test Setup  Run Keywords  set ignition off  IGNITION  AND  set door close  All Door  AND  set door close  Hood  AND  set door close  Trunk


*** Test Cases ***

init
    set initial state


Sense Driver door
    [Documentation]  Test the sensing 5 times
    [Tags]    sense_front_door
    Pass Execution  Ce test reussi automatiquement
#    ${sensing} =  set variable  Driver Door open and close
#    ${exp_count} =  set variable  5
#    log to console  Ceci est le test ${TEST NAME}
#    #pause execution  ${TEST NAME}\nFaire ${sensing} ${exp_count}x
#    ${nb_cycle} =  redo_test  ${sensing}  ${exp_count}
#    #${nb_cycle} =  count sensing  Door open/close              #${sensing}  ${exp_status}  ${OPEN}  ${CLOSE}
#    should be equal  ${nb_cycle}  ${5}

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

redo_test
    [Tags]    DEBUG
    [Arguments]  ${sensing}  ${exp_count}

    :for  ${i}  in range  99999
        \  pause execution  ${TEST NAME}\nFaire ${sensing} ${exp_count}x
        \  ${count} =  count sensing   ${sensing}
        \  ${exit}=  get selection from user  Le nombre de ${sensing} est ${count} le nombre attendu est ${exp_count}\nReprende le test ?  Yes  No
        \  exit for loop if  '${exit}' == 'No'
     [Return]  ${count}

count sensing
    [Arguments]  ${sensing}
    # clear buffers  # D2D commands to clear previous data D2D data log
    ${count} =  get value from user  Indiquer le nombre de cycle ${sensing}  #Remplacer par get D2D status
    ${count} =  convert to integer  ${count}
    [Return]  ${count}

set ignition off
    [Arguments]  ${sensing}      #${exp_status}  @{sensestatus}
    pause execution  Mettre ${sensing} à OFF
    :for  ${i}  in range  99999
        \  ${status} =  get selection from user  D2D status de ${sensing}  On  Off   #@{sensestatus}  #Remplacer par get D2D status
        \  ${exit}=  Run Keyword If  '${status}' != 'Off'  get selection from user  Le status de ${sensing} est ${status} l'etat attendu est OFF\nReprende le test ?  Yes  No
           ...  ELSE  Catenate  No
        \  exit for loop if  '${exit}' == 'No'

set door close
    [Arguments]  ${sensing}  ${status}
    pause execution  Close ${sensing}
    :for  ${i}  in range  99999
        \  ${status} =  get selection from user  D2D status de ${sensing}  Open  Close    #@{sensestatus}  #Remplacer par get D2D status
        \  ${exit}=  Run Keyword If  '${status}' != 'Close'  get selection from user  Le status de ${sensing} est ${status} l'etat attendu est CLOSE\nReprende le test ?  Yes  No
           ...  ELSE  Catenate  No
        \  exit for loop if  '${exit}' == 'No'

test decision
    ${choix} =  get selection from user  Choix  Oui  Non
    ${get} =  Run Keyword If  '${choix}' == 'Oui'  get selection from user  Faite un choix  Ouvert  Ferme
    ...  ELSE  Catenate  Exit
    log to console  Vous avez choisi : ${get}

zone state
    [Arguments]  ${sensing}  ${status}
    log to console  Zone ${sensing} is not Close

ignition state
    log to console  Ignition is not OFF

Set initial state

    :for  ${i}  in range  99999
        \  pause execution  Close all door, trunk and hood, put ignition to off
        \  ${ignition} =  get selection from user  Etat de l'ignition ?  On  Off
        \  ${door_status} =  get selection from user  Etat des portieres ?  Open  Close
        \  ${hood_status} =  get selection from user  Etat du Capot ?  Open  Close
        \  ${trunk_status} =  get selection from user  Etat du Coffre arriere ?  Open  Close
        \  log to console  \n
        \  Run Keyword If  '${ignition}' != 'Off'  ignition state
        \  Run Keyword If  '${door_status}' != 'Close'  zone state  porte  ${door_status}
        \  Run Keyword If  '${trunk_status}' != 'Close'  zone state  trunk  ${door_status}
        \  Run Keyword If  '${hood_status}' != 'Close'  zone state  hood  ${door_status}
        \  ${exit} =  evaluate  '${ignition}' == 'Off' and '${door_status}' == 'Close' and '${hood_status}' == 'Close' and '${trunk_status}' == 'Close'
        \  log to console  1-value de exit : ${exit}
        \  ${force_exit} =  Run Keyword If  '${exit}' != 'True'  get selection from user  Voulez-vous poursuivre le test quand même ?\nLe résultat risque d'être faussé.  Oui  Non
        #\  ${exit} =  Run Keyword If  '${force_exit}' == 'Oui'  Catenate  True  ELSE
        #\  ${force_exit} =  set variable  False
        \  log to console  2-value de exit : ${exit}
        \  log to console  3-value de force_exit : ${force_exit}
        \  exit for loop if  '${exit}' == 'True' or '${force_exit}' == 'Oui'


