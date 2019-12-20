#coding:utf-8

import os
from time import sleep
import string

import datetime


def pass_arg(line, *args):
    #print(type(arg))
    #print(args)
    #print(line)
    #if (line.__contains__(arg[:])):

    for i in args:
        if(line.__contains__(i)):

            print("Je l'ai retrouvé")
            break

        else:
            #print("Je NE l'ai PAS retrouvé")
            pass

    #
    # list = ["un", "deux", "trois", "quatre", "cinq"]
    #
    # for i in list:
    #     if i in arg:
    #         print("Je l'ai retrouvé")
    #
    #     else:
    #         print("Je NE l'ai PAS retrouvé")
    #



with open(".\\sniffer\\do_unlock.log", "r") as f:
    for line in f:
        pass_arg(line, "F8=SET_OTHER_OPEN", "deux", "trois" )
