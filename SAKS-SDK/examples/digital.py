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
    num = sys.argv[1]
    # 将显示“1234”4位数字，并且每一位右下角的小点点亮
    SAKS.digital_display.show(num)
