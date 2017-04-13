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
import json
from subprocess import Popen,PIPE
from iospush import ios_push

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

def beep2(SAKS,num):
    num = int(num)
    b = SAKS.buzzer
    #secs, sleepsecs, times
    b.beepAction(0.1,0.1,num)

def temperature(SAKS,num):
    while True:
        #从 ds18b20 读取温度（摄氏度为单位）
        temp = SAKS.ds18b20.temperature
        #返回值为 -128.0 表示读取失败
        if temp == -128.0 :
            #10秒后再次尝试
            time.sleep(10)
            continue
        return temp        


def common_loop(SAKS,function,num,format="%4d",type='digital'):
    global share
    share['cancel']=0
    while True:
        #从 ds18b20 读取温度（摄氏度为单位）
        temp = function(SAKS,num)
        #返回值为 -128.0 表示读取失败
        if temp == -1 :
            #10秒后再次尝试
            time.sleep(10)
            continue
        if type=='digital':
            digital(SAKS,(format % temp).replace(' ','#'))
            print format % temp
        elif type=='led':
            led(SAKS,str(temp))

        time.sleep(10)
        if share.get('cancel') == 1:
            digital(SAKS,'####')
            led(SAKS,'0')
            share['cancel']=0
            break

def alarm(SAKS):
    global share
    share['cancel']=0
      
    __dp = True
    __alarm_beep_status = False
    __alarm_beep_times = 0
    # 以下代码获取系统时间、时、分、秒、星期的数值
    while True:
        __alarm_hour = share.get('alarm_hour')
        __alarm_minitue = share.get('alarm_minitue')  

        if share.get('cancel') == 1:
            digital(SAKS,'####')
            led(SAKS,'0')
            share['cancel']=0
            break

        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        w = time.strftime('%w',t)
        #print h,m,s,w
        print "%02d:%02d:%02d" % (h, m, s)
 
        __alarm_time = "%02d:%02d" % (__alarm_hour, __alarm_minitue)#"12:33"
        if ("%02d:%02d" % (h, m)) == __alarm_time:
            __alarm_beep_status = True
            __alarm_beep_times = 0
 
        if __dp:
            # 数码管显示小时和分，最后一位的小点每秒闪烁一次
            SAKS.digital_display.show(("%02d%02d." % (h, m)))
            # 判断是否应该响起闹钟
            if __alarm_beep_status:
                #SAKS.buzzer.on()
                led(SAKS,"1")                
                __alarm_beep_times = __alarm_beep_times + 1
                # 30次没按下停止键则自动停止闹铃
                if __alarm_beep_times > 30:
                    __alarm_beep_status = False
                    __alarm_beep_times = 0
                    led(SAKS,"0")  
        else:
            SAKS.digital_display.show(("%02d%02d" % (h, m)))
            if __alarm_beep_status:
                #SAKS.buzzer.off()
                led(SAKS,"0")                
        __dp = not __dp
        time.sleep(1)

def learning(SAKS,allt,learnt):
    global share
    share['cancel']=0
  
    # 以下代码获取系统时间、时、分、秒、星期的数值
    __dp = True
    count = allt
    while True:
        if share.get('cancel') == 1:
            digital(SAKS,'####')
            led(SAKS,'0')
            share['cancel']=0
            break
        
        print "%02d:%02d" % (count/60, count%60)
        count=count-1 
        if __dp:
            # 数码管显示小时和分，最后一位的小点每秒闪烁一次
            SAKS.digital_display.show(("%02d.%02d" % (count/60, count%60)))
        else:
            SAKS.digital_display.show(("%02d.%02d" % (count/60, count%60)))

        if count==allt-learnt:            
            led(SAKS,"2")
            beep(SAKS,3)
        if count<=allt-learnt:
            #SAKS.buzzer.on()
            led(SAKS,"1")

        if count==0:
            count = allt
            led(SAKS,"0")
            beep2(SAKS,3)

        __dp = not __dp
        time.sleep(1)


def fireworks(SAKS):
    led(SAKS,'0')    
    for i in range(0,8):
        led(SAKS,str(1<<i))
        time.sleep(0.5)
    led(SAKS,'0')

def dfireworks(SAKS):    
    digital(SAKS,'####')    
    for i in range(0,1):
        digital(SAKS,'###0') 
        time.sleep(0.5)
        digital(SAKS,'##0#') 
        time.sleep(0.5)
        digital(SAKS,'#0##') 
        time.sleep(0.5)
        digital(SAKS,'0###') 
        time.sleep(0.5)
    digital(SAKS,'####')

def countdown(SAKS,num):
    global share
    share['cancel']=0
    for i in range(num,-1,-1):
        if share.get('cancel') == 1:
            share['cancel']=0
            return False
        else:
            digitalint(SAKS,i)
        time.sleep(1)
    digital(SAKS,'####')
    return True

def execcmd(cmd):
    proc=Popen(cmd, shell=True, stdout=PIPE, ) 
    output=proc.communicate()[0]
    return output

def get_netcontent(SAKS,num):    
    req = urllib2.Request("http://115.28.24.177:8092/project/wx_special_get.php?pass=s321&num="+num)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        weatherJSON = json.JSONDecoder().decode(content)
        #print(content)
        try:
            if weatherJSON['ret'] == 0:
                if weatherJSON['data'].has_key('num'):
                    print(weatherJSON['data']['num'])
                    return int(weatherJSON['data']['num'])
                else:
                    return -1
            else:
                return -1
        except:
            return -1

class TaskThread(threading.Thread):
 
    '''
        初始化
    '''
    def __init__(self,SAKS,data,client):
        threading.Thread.__init__(self)
        self.SAKS = SAKS
        self.data = data
        self.client = client
    '''
     执行线程
    '''
    def run(self):
        timestr = time.ctime(time.time())+"\r\n" #时间羽化输出
        strs = '现在是：'+timestr
        global share
        share['count']+=1
        print share
        SAKS = self.SAKS
        client = self.client
        try:
            #process data
            pair = self.data.split('&')            
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
            if kv.get('type')=='notify':
                strs="%s %s" % (strs,ios_push(kv['num']))
            if kv.get('type')=='clear':
                share['cancel']=1
                time.sleep(2)
                digital(SAKS,'####')
                led(SAKS,'0')
            if kv.get('type')=='cancel':
                share['cancel']=1
                print "cancel countdown!"
                print share
            if kv.get('type')=='beep':
                beep(SAKS,kv['num'])
            if kv.get('type')=='setalarm':
                newalarm = int(kv['num'])
                share['alarm_hour']=newalarm/100
                share['alarm_minitue']=newalarm%100
            if kv.get('type')=='net':
                client.send(strs+str(share)) #发送输数据 
                client.close()
                common_loop(SAKS,get_netcontent,kv['num'],"%4d")                
                return
            if kv.get('type')=='netled':
                client.send(strs+str(share)) #发送输数据 
                client.close()
                common_loop(SAKS,get_netcontent,kv['num'],"%4d",'led')                
                return
            if kv.get('type')=='alarm':
                client.send(strs+str(share)) #发送输数据 
                client.close()
                alarm(SAKS)                
                return
            if kv.get('type')=='learning':
                client.send(strs+str(share)) #发送输数据 
                client.close()
                learning(SAKS,1800,300)                
                return
            if kv.get('type')=='fireworks':
                fireworks(SAKS)
            if kv.get('type')=='dfireworks':
                dfireworks(SAKS)
            if kv.get('type')=='wendu':
                client.send(strs+str(share)) #发送输数据 
                client.close()
                common_loop(SAKS,temperature,0,"%5.1f")
                return
            if kv.get('type')=='shutdown':
                print "shutdown"
                downtimes = int(kv.get('num','10'))
                if countdown(SAKS,downtimes):
                    fireworks(SAKS)
                    os.system("sudo shutdown -h now")
            if kv.get('type')=='reboot':
                print "reboot"
                downtimes = int(kv.get('num','10'))
                if countdown(SAKS,downtimes):
                    fireworks(SAKS)
                    os.system("sudo reboot")
            if kv.get('type')=='update':
                print "update"
                strs="%s %s" % (strs,execcmd("sudo svn up /var/www/html/saks/"))
        except Exception as err:
            strs="%s %s" %(strs, err)
            print err
        finally: 
            print("Goodbye! %s" % strs) 


        client.send(strs+str(share)) #发送输数据 
        client.close()
   

if __name__ == "__main__":
    print("main")
    SAKS.dip_switch_status_changed_handler = dip_switch_status_changed_handler
    SAKS.tact_event_handler = tact_event_handler

     #Socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建tcp socket
    s.settimeout(None)
    s.bind(('localhost',9999))#绑定到9999
    s.listen(5) #监听，但只能挂起5以下链接
 
    share={'count':1,'cancel':0,'wendu':0,'alarm_hour':12,'alarm_minitue':12}
    #system started 
    led(SAKS,'0')
    digital(SAKS,'####')
    for i in range(0,5):
        led(SAKS,'1')
        time.sleep(0.5)
        led(SAKS,'0')


    while True:
        client,addr = s.accept()#连接
        addr = str(addr)
        print("从 %s 获取一个连接"%addr) #直接输出到控制台

        #client.send(strs) #发送输数据
        data = str(client.recv(1024))
        cs = '%s 客户端返回的数据为：%s'%(addr,data) #接收客户端数据
        print(cs)        

        #client.send(strs+str(share)) #发送输数据 
        #client.close()        
        
        #开始线程   
        t = TaskThread(SAKS,data,client)
        t.setDaemon(True) #子线程随主线程一起退出
        t.start() #启动线程
        t.join(10) #保证每个线程运行，但只等10s
 
        
