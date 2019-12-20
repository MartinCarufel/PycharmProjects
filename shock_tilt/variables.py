from System import *

D2D_PORT = "COM2"
D2D2_PORT = "COM20"
IO_INPUT_PORT = ""
IO_OUTPUT_PORT = ""
IO_MAP = "DS4-Analog Harness_3.xml"

#Local path for library
path_NvfsInterface = "C:/Drive-W/Internal_tools/Libraries/FlashNVFS/trunk/out/NvfsInterface.py"
path_D2DWrapper = "C:/Drive-W/Internal_tools/Libraries/D2DProjectLibrary/trunk/out/D2DWrapper.py"
path_CANInterface = "C:/Drive-W/Internal_tools/Libraries/CANOBDIILibrary/trunk/out/CANInterface.py"
path_IOLibrary = "C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out/IOWrapper.py"
path_D2D2_Lib = "C:/Drive-W/Internal_tools/Libraries/D2D2Library/trunk/out/D2D2Wrapper.py"


#D2D patern and filter

fd_door_test_count = 5  #front driver door count


snsdoor = Array[String](['SET_OTHER_OPEN', 'SET_OTHER_CLOSE'])
ext_stat = Array[String](['SET_EXTENDED_STATUS'])

