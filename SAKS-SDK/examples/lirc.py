#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Spoony'
__version__  = 'version 0.0.2'
__license__  = 'Copyright (c) 2016 NXEZ.COM'

import commands
import pylirc, time
import urllib2
import socket
import re

urllib2.socket.setdefaulttimeout(10)

blocking = 1;


def is_num(num):
    if re.match('^[0-9]+$',num):
        return True
    else:
        return False
def formatint(num):
    return ("%4d" % num).replace(' ','#')

def led(num):
    return raspsend("type=led&num="+num)    

def digital(num):    
    return raspsend("type=digital&num="+num)
    
def digitalint(num):
    num = formatint(num);
    return raspsend("type=digital&num="+num)    

def beep(num):
    return raspsend("type=beep&num="+num);   

def wendu():
    return raspsend("type=wendu");   

def raspsend(data): 
    address = ('127.0.0.1', 9999)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect(address)    
    s.send(data)  
    rdata = s.recv(512)  
    print 'the data received is',rdata    
    s.close()  
    return rdata

def sendtophp(data):
    try:
        print s
        url = "http://localhost/saks/web/api.php?type=remote&num="+data
        print url
        response = urllib2.urlopen(url)        
        content = response.read()
        print content
    except Exception as err:
        print err
    finally: 
        print("Goodbye!")    



if __name__ == "__main__":
    print("main")
    if pylirc.init("pylirc", "lircrc", blocking):
        code = {"config" : ""}
        nummode = False
        numbuff = 0;
        while True:      
            if(not blocking):
                print "."

            # Delay...
            time.sleep(0.5)

            # Read next code
            try:
                s = pylirc.nextcode(1)
                if s and len(s)>0:
                    inputkey = s[0]["config"]
                    if nummode:
                        if is_num(inputkey):
                            numbuff=numbuff*10+int(inputkey)
                            if numbuff>999:
                                nummode= False
                                digitalint(numbuff)
                                sendtophp(str(numbuff))
                                numbuff=0
                                digital('####')
                            else:
                                digitalint(numbuff)                        
                        else:
                            nummode= False
                            sendtophp(str(numbuff))
                            numbuff=0
                            digital('####')
                    else:
                        if is_num(inputkey):
                            nummode= True
                            numbuff=int(inputkey)
                            digitalint(numbuff)
                        else:
                            sendtophp(inputkey)
            except Exception as err:                
                print err
                code = {"config" : ""}
                nummode = False
                numbuff = 0;
            finally: 
                print("Goodbye!") 

        # Clean up lirc
        pylirc.exit()

   

