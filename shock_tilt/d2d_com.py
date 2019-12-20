#coding:utf-8

import sys
import os
from time import sleep

sys.path.append(r'C:\Drive-W\Internal_tools\Libraries\D2DProjectLibrary\trunk\out')

from D2DWrapper import D2DWrapper

def unlock_ds4_1():
    d2d_conn = D2DWrapper("COM2")
    sleep(1)
    d2d_conn.Send_D2D_Function('unlock door rem1 on')
    sleep(4)
    d2d_conn.D2D_Disconnected()

def unlock_ds4_2():
    d2d_conn = D2DWrapper("COM2")
    sleep(1)
    d2d_conn.Send_D2D_Function('unlock door rem1 on')
    sleep(4)
    d2d_conn.D2D_Disconnected()


def lock_ds4_1():
    d2d_conn = D2DWrapper("COM2")
    sleep(1)
    d2d_conn.Send_D2D_Function('lock rem1 on')
    sleep(4)
    d2d_conn.D2D_Disconnected()


def lock_ds4_2():
    d2d_conn = D2DWrapper("COM2")
    sleep(1)
    d2d_conn.Send_D2D_Function('lock rem1 on')
    sleep(4)
    d2d_conn.D2D_Disconnected()