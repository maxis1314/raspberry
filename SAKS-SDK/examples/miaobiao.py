#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Spoony'
__license__  = 'Copyright (c) 2015 NXEZ.COM'

from sakshat import SAKSHAT
import time
from datetime import datetime
from sakspins import SAKSPins as PINS

#Declare the SAKS Board
SAKS = SAKSHAT()

__start_time = datetime.utcnow()
__end_time = datetime.utcnow()
__timer_running = False

#在检测到轻触开关触发时自动执行此函数
def tact_event_handler(pin, status):
    '''
    called while the status of tacts changed
    :param pin: pin number which stauts of tact is changed
    :param status: current status
    :return: void
    '''
    global __start_time
    global __end_time
    global __timer_running

    if pin == PINS.TACT_RIGHT and status == True:
        if __timer_running:
            __end_time = datetime.utcnow()
        else:
            __start_time = datetime.utcnow()
            SAKS.digital_display.show(("%02d.%02d" % (0, 0)))
        __timer_running = not __timer_running

if __name__ == "__main__":
    #设定轻触开关回调函数
    SAKS.tact_event_handler = tact_event_handler
    SAKS.digital_display.show(("%02d.%02d" % (0, 0)))

    while True:
        if __timer_running:
            __end_time = datetime.utcnow()
            c = __end_time - __start_time
            #print c.seconds
            #print c.microseconds
            SAKS.digital_display.show(("%02d.%02d" % (c.seconds, c.microseconds)))

        time.sleep(0.01)
    input("Enter any keys to exit...")
