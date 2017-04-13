#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
#引脚采用BCM编码
GPIO.setmode(GPIO.BCM)
#配置一个数组，依次对应8个灯的引脚BCM编码
pins = [5, 6, 13, 19, 0, 1, 7, 8] #GPIO ports
#由于SAKS的蓝色LED和数码管共享引脚，此处将数码管位选关闭，只让信号作用于LED
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
#定义一个便捷地设置引脚的方法
def setp(n, status='off'):
    if status == 'on':
        GPIO.output(n, GPIO.LOW)
    else:
        GPIO.output(n, GPIO.HIGH)
#遍历数组，将数组中8个LED引脚初始化
for i in pins:
    GPIO.setup(i, GPIO.OUT)
    setp(i, 'off')

print "after init"

i = 0
#点亮数组中第i个LED
print "set on",pins[i]
setp(pins[i], 'on')
#延时0.1秒
time.sleep(0.1)
#熄灭数组中第i个LED
print "set off",pins[i]
setp(pins[i], 'off')
