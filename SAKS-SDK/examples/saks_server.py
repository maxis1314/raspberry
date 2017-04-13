#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Spoony'
__version__  = 'version 0.0.2'
__license__  = 'Copyright (c) 2016 NXEZ.COM'

from sakshat import SAKSHAT
import time
import commands
import urllib2
import socket
import threading
import Queue
import os

urllib2.socket.setdefaulttimeout(10)

#Declare the SAKS Board
SAKS = SAKSHAT()


def dip_switch_status_changed_handler(status):
    '''
    called while the status of dip switch changed
    :param status: current status
    :return: void
    '''
    print('on_dip_switch_status_changed:')
    print(status)
    param = "status1=%s&status2=%s" % tuple(status)
    if True:
        url = "http://localhost/saks/web/api.php?type=dip&"+param
        response = urllib2.urlopen(url)
        print url
        content = response.read()
        print content

def tact_event_handler(pin, status):
    '''
    called while the status of tacts changed
    :param pin: pin number which stauts of tact is changed
    :param status: current status
    :return: void
    '''
    print('tact_event_handler')
    print("%d - %s" % (pin, status))
    param = "pin=%d&status=%s" % (pin, status)
    if status == 1:
        url = "http://localhost/saks/web/api.php?type=tact&"+param
        response = urllib2.urlopen(url)
        print url
        content = response.read()
        print content

def led(SAKS,num):
    num = int(num)
    SAKS.ledrow.off()
    SAKS.ledrow.set_row([(num&0x80)>>7==1, (num&0x40)>>6==1, (num&0x20)>>5==1, (num&0x10)>>4==1 , (num&0x08)>>3==1 , (num&0x04)>>2==1 , (num&0x02)>>1==1,(num&0x01)==1])    
    return  SAKS.ledrow.row_status

def digital(SAKS,num):    
    SAKS.digital_display.show(num)

def digitalint(SAKS,num):    
    SAKS.digital_display.show(("%4d" % num).replace(' ','#'))

def beep(SAKS,num):
    num = int(num)
    b = SAKS.buzzer
    #secs, sleepsecs, times
    b.beepAction(0.02,0.02,num)
def temperature(SAKS):
    while True:
        #从 ds18b20 读取温度（摄氏度为单位）
        temp = SAKS.ds18b20.temperature
        #返回值为 -128.0 表示读取失败
        if temp == -128.0 :
            #10秒后再次尝试
            time.sleep(10)
            continue
        
        SAKS.digital_display.show(("%5.1f" % temp).replace(' ','#'))
        return temp

def countdown(SAKS,num):
    for i in range(num,0,-1):
        digitalint(SAKS,i)
        time.sleep(1)

if __name__ == "__main__":
    print("main")
    SAKS.dip_switch_status_changed_handler = dip_switch_status_changed_handler
    SAKS.tact_event_handler = tact_event_handler

     #Socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建tcp socket
    s.settimeout(None)
    s.bind(('localhost',9999))#绑定到9999
    s.listen(5) #监听，但只能挂起5以下链接
 
    while True:
        client,addr = s.accept()#连接
        addr = str(addr)
        print("从 %s 获取一个连接"%addr) #直接输出到控制台
        timestr = time.ctime(time.time())+"\r\n" #时间羽化输出
        strs = '现在是：'+timestr
        #client.send(strs) #发送输数据
        data = str(client.recv(1024))
        cs = '%s 客户端返回的数据为：%s'%(addr,data) #接收客户端数据
        print(cs)
        

        try:
            #process data
            pair = data.split('&')
            print pair
            kv={}
            for x in pair:
                y = x.split('=')
                print y
                if len(y) ==2:
                    kv.setdefault(y[0],y[1])      
            print kv
            if kv.get('type')=='led':
                stat = led(SAKS,kv['num'])
                print stat
                print type(stat)
                strs="%s %s" %(strs, ' '.join(map(str,stat)))
                print strs
            if kv.get('type')=='digital':
                digital(SAKS,kv['num'])
            if kv.get('type')=='beep':
                beep(SAKS,kv['num'])
            if kv.get('type')=='wendu':
                strs="%s %f" %(strs, temperature(SAKS))
            if kv.get('type')=='shutdown':
                print "shutdown"
                countdown(SAKS,10)     
                os.system("sudo shutdown -t 5 now")
            if kv.get('type')=='reboot':
                print "reboot"
                countdown(SAKS,10) 
                os.system("sudo shutdown -r -t 5 now")
        except Exception as err:
            strs="%s %s" %(strs, err)
            print err
        finally: 
            print("Goodbye!") 

        client.send(strs) #发送输数据 
        client.close()

        #任务
        #task = task.split('|')
        #将任务写入到队列中
        #for i in task:
        #    queue.put(i)
 
        #开始线程   
        #for i in task:
        #    t = TaskThread(queue)
        #    t.setDaemon(True) #子线程随主线程一起退出
        #    t.start() #启动线程
        #    t.join(10) #保证每个线程运行，但只等10s
 
        #queue.join() #等所有任务都处理后，再退出
