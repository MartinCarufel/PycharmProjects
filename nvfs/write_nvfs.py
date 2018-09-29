#coding:utf-8

import sys
import string
sys.path.append('C:/Drive-W/Internal_tools/Libraries/FlashNVFS/trunk/out')
from NvfsInterface import NvfsInterface

module_nvfs = NvfsInterface(Port="COM2")



actual_value = NvfsInterface.nvfs_read("_MANUAL")
print actual_value
NvfsInterface.nvfs_write("_MANUAL", "00")
    #print my_module_dump["BOOT_VER"]
