#coding:utf-8

import sys
import string
sys.path.append('C:/Drive-W/Internal_tools/Libraries/FlashNVFS/trunk/out')
from NvfsInterface import NvfsInterface

module_nvfs = NvfsInterface(Port="COM2")



my_module_dump = module_nvfs.nvfs_dump()
print chr(0x35)
    #print my_module_dump["BOOT_VER"]
