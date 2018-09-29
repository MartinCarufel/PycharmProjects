# There is four possible section in robot framework, the names of the section is case-insesitive, and singular form can be used.
#   - Settings
#   - Variables
#   - Test Caeses
#   - Keywords

# Most common use file format is tabbed format, if using text editor, two space or more is required.
# It's recommneded to used 4 spaces between keyword and arguments.

#######################
# Built-in variable   #

#${CURDIR}      An absolute path to the directory where the test data file is located. This variable is case-sensitive.
#${TEMPDIR}	    An absolute path to the system temporary directory. In UNIX-like systems this is typically /tmp, and in Windows c:\Documents and Settings\<user>\Local Settings\Temp.
#${EXECDIR}	    An absolute path to the directory where test execution was started from.
#${/}	        The system directory path separator. / in UNIX-like systems and \ in Windows.
#${:}	        The system path element separator. : in UNIX-like systems and ; in Windows.
#${\n}	        The system line separator. \n in UNIX-like systems and \r\n in Windows. New in version 2.7.5.

##########  Numbers  #################
#${99}          Use to refer to an integer instead string, 99 --> string, ${99} --> Number integer 99
#${45.89}       Use to refer to an float instead string, 45.89 --> string, ${45.89} --> Number integer 45.89
#${0b1011}      Use to refer to an binary
#${0o85}        Use to refer to an octal
#${0xf7}        Use to refer to an hexadecimal

########  Boolean and null  ###########
#${true} = ${TRUE} = ${True} = ${TrUe}  Use as (1)/True boolean value case-insensitive
#${False} ...................           Use as (0)/False boolean value case-insensitive
#${None}                                This refer to Python None argument

#########  Space and empty  ##########
#${SPACE}       Refer to one space caracter
#${SPACE * 4}   Refer to four space caracter
#${EMPTY}       Refer to and empty, usefull to set and empty variable.

#########  List, Dictionnary, variable  ##############
#${x_var}     Refer to a standard variable.
#@{x_list}    Refer to a list type variable
#&{x_dict}    Refer to a dictionary type variable as Python did

#########  List automatic variable  ############
var name                Description                                                                                                                                      Available
${TEST NAME}	        The name of the current test case.	                                                                                                             Test case
@{TEST TAGS}	        Contains the tags of the current test case in alphabetical order. Can be modified dynamically using Set Tags and Remove Tags keywords.	         Test case
${TEST DOCUMENTATION}	The documentation of the current test case. Can be set dynamically using using Set Test Documentation keyword. New in Robot Framework 2.7.	     Test case
${TEST STATUS}	        The status of the current test case, either PASS or FAIL.	                                                                                     Test teardown
${TEST MESSAGE}	        The message of the current test case.	                                                                                                         Test teardown
${PREV TEST NAME}	    The name of the previous test case, or an empty string if no tests have been executed yet.	                                                     Everywhere
${PREV TEST STATUS}	    The status of the previous test case: either PASS, FAIL, or an empty string when no tests have been executed.	                                 Everywhere
${PREV TEST MESSAGE}	The possible error message of the previous test case.	                                                                                         Everywhere
${SUITE NAME}	        The full name of the current test suite.	                                                                                                     Everywhere
${SUITE SOURCE}	        An absolute path to the suite file or directory.	                                                                                             Everywhere
${SUITE DOCUMENTATION}	The documentation of the current test suite. Can be set dynamically using using Set Suite Documentation keyword. New in Robot Framework 2.7.	 Everywhere
&{SUITE METADATA}	    The free metadata of the current test suite. Can be set using Set Suite Metadata keyword. New in Robot Framework 2.7.4.	                         Everywhere
${SUITE STATUS}	        The status of the current test suite, either PASS or FAIL.	                                                                                     Suite teardown
${SUITE MESSAGE}	    The full message of the current test suite, including statistics.	                                                                             Suite teardown
${KEYWORD STATUS}	    The status of the current keyword, either PASS or FAIL. New in Robot Framework 2.7	                                                             User keyword teardown
${KEYWORD MESSAGE}	    The possible error message of the current keyword. New in Robot Framework 2.7.	                                                                 User keyword teardown
${LOG LEVEL}	        Current log level. New in Robot Framework 2.8.	                                                                                                 Everywhere
${OUTPUT FILE}	        An absolute path to the output file.	                                                                                                         Everywhere
${LOG FILE}	            An absolute path to the log file or string NONE when no log file is created.	                                                                 Everywhere
${REPORT FILE}	        An absolute path to the report file or string NONE when no report is created.	                                                                 Everywhere
${DEBUG FILE}	        An absolute path to the debug file or string NONE when no debug file is created.	                                                             Everywhere
${OUTPUT DIR}	        An absolute path to the output directory.	                                                                                                     Ever

*** Settings ***
Documentation    Variable usage

*** Variables ***
#How to set variable in variable section
#In varaible section  "=" automatically assign the value the variable
${variable} =   one string
@{new_list} =   first   second    third
&{new_dict} =   key1=value1    key2=value2


*** Test Cases ***
Test title
    [Tags]    DEBUG

    # some way to access to element of variable, list, dict
    log to console    Following variable are define outside test case in variable Table
    log to console    ${variable}
    log to console    @{new_list}[0]
    log to console    @{new_list}[2]
    log to console    &{new_dict}[key2]

    #How to set variable within a test case
    ${tc_var} =    set variable    Test case var only not availble outside
    @{tc_list} =    create list    first item    second item    third item     #
    &{tc_dict} =    create dictionary    key1    value1    key2    value2

    log to console    ${empty}
    log to console    Following variable are define within test case
    log to console    ${tc_var}
    log to console    @{tc_list}[0]
    log to console    @{tc_list}[2]
    log to console    &{tc_dict}[key1]

*** Keywords ***
