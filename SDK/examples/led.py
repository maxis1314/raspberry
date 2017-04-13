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
    SAKS.ledrow.off()
    SAKS.ledrow.set_row([(num&0x80)>>7==1, (num&0x40)>>6==1, (num&0x20)>>5==1, (num&0x10)>>4==1 , (num&0x08)>>3==1 , (num&0x04)>>2==1 , (num&0x02)>>1==1,(num&0x01)==1])
    #SAKS.ledrow.set_row([True, False, True, False, True, False, True, False])
    #SAKS.ledrow.set_row([None, True, False, None, None, None, None, True])
    print( SAKS.ledrow.row_status)
    #print( SAKS.ledrow.is_on(1))

