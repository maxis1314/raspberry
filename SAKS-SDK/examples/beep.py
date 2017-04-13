#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Spoony'
__version__  = 'version 0.0.2'
__license__  = 'Copyright (c) 2016 NXEZ.COM'

from sakshat import SAKSHAT
import time
import commands
import sys
#Declare the SAKS Board
SAKS = SAKSHAT()


if __name__ == "__main__":
    num = int(sys.argv[1])
    b = SAKS.buzzer
    #secs, sleepsecs, times
    b.beepAction(0.02,0.02,num)
    #b.beep(1)
