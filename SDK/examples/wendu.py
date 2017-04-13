# -*- coding: utf-8 -*-

from sakshat import SAKSHAT
import time
 
#Declare the SAKS Board
SAKS = SAKSHAT()
 
if __name__ == "__main__":
    while True:
        #从 ds18b20 读取温度（摄氏度为单位）
        temp = SAKS.ds18b20.temperature
        #返回值为 -128.0 表示读取失败
        if temp == -128.0 :
            #10秒后再次尝试
            time.sleep(10)
            continue
 
        print (("%5.1f" % temp).replace(' ','#'))
        #数码管显示温度数值，5位(含小数点)、精确到小数点1后1位
        SAKS.digital_display.show(("%5.1f" % temp).replace(' ','#'))
        time.sleep(5)
    input("Enter any keys to exit...")
