*** Settings ***
Documentation  Template test script

# **** Set following to your library path  ***************************************
#Library  ${path_D2DWrapper}  ${D2D_PORT}
Library  ${path_D2D2_Lib}  ${D2D2_PORT}
Library  d2d_com.py
#Library    ${path_CANInterface}
#Library  ${path_NvfsInterface}  ${PORT}
Library  ${path_IOLibrary}

# **********************************************************************************
#  Some Robot framework Library

#Library  Dialogs
#Library  Collections
#Library  DateTime
#Library  Library  

# **********************************************************************************

Suite Setup  clear alarm report
Suite Teardown         Close Application

#Test Setup  run keywords  do_unlock

*** Test Cases ***

test1
    [Documentation]  Test to check if the BLE siren or wire shock senssor trig events
    [tags]
    #D2D2 Lock and arm
    #sleep  2s
    #D2D2 Unlock and disarm
    D2D2 Trigger History Request
    sleep  2s
    ${result} =  D2D2 Get Triggered Zones
    log to console  Zone1: ${result.Zone1}
    log to console  Zone2: ${result.Zone2}
    log to console  Zone3: ${result.Zone3}
    log to console  Zone4: ${result.Zone4}
    log to console  Zone5: ${result.Zone5}
    log to console  Zone6: ${result.Zone6}
    log to console  Zone7: ${result.Zone7}

test shock
    [Tags]  x
    :for  ${i}  in range  ${5}

        \  lock_ds4_1
        \  unlock_ds4_1



*** Keywords ***

Close Application
    D2D DISCONNECTED
	D2D2 Disconnect
	IO DISCONNECT



clear alarm report
    unlock_ds4_1
    sleep  3s
    io set value  ign_ds4_1  ${True}
    sleep  6s
    io set value  ignition  ${False}

    unlock_ds4_2
    sleep  3s
    io set value  ign_ds4_2  ${True}
    sleep  6s
    io set value  ignition  ${False}


device io connect
    IO CONNECT DEVICE       ${1}  ${IO_INPUT_PORT}
    IO CONNECT DEVICE       ${2}  ${IO_OUTPUT_PORT}
    IO READ MAP   ${IO_MAP}

clear d2d
    clear buffers