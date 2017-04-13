#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入 SAKS SDK 模块
from sakshat import SAKSHAT
import time
import commands

#Declare the SAKS Board，定义一个SAKS对象
SAKS = SAKSHAT()

#返回浮点型的CPU温度
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp) / 1000
    #如果你想使用华氏温度，打开注释
    #return float(1.8*cpu_temp)+32

#主程序入口
if __name__ == "__main__":
    while True:
        t = get_cpu_temp()
        #如果你希望实时温度的数值输出在屏幕上请取消下面的注释
        #print("%.2f" % t)
        #调用SAKS的数码管对象(digital_display)，让他按照指定格式显示(show)温度数值
        SAKS.digital_display.show("%.2f" % t)
        #这里暂时设定为50度警报响起
        if t > 60:
            #调用SAKS的蜂鸣器对象(buzzer)，让他按照按照一定的频率发出警报(beepAction)，下面的参数是以2毫秒的间隔鸣响30次
            SAKS.buzzer.beepAction(0.02,0.02,30)
        time.sleep(1)

    input("Enter any keys to exit...")
