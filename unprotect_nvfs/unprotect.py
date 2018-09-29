#coding:utf-8

import sys
from NvfsInterface import NvfsInterface as nvfs



allVar = nvfs.nvfs_print_all_variables()
print allVar

# nvfsa.nvfs_remove_write_protected("$BRAND")
#
# allVar = nvfs.nvfs_print_all_variables()
# print allVar