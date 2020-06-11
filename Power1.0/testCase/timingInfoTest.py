#! /usr/bin/env python
#coding=GB18030
import random
import sys
import time

import SendKeys
import pyautogui
import envPath
import Common.Init as init
import Common.auto_lib as pywin
import Common.getPos as getPos
import Common.setup as setup
import Common.fillValue as fill
import Common.readConifg as readConfig

reload(sys)
sys.setdefaultencoding('utf8')
list=readConfig.readIniConifg('Power')
app = pywin.Pywin()
window_name = u"�������ģ����������V1.0.2"
window_name=list[0]
init.check_exist(list[2])
file=list[1]+'\\data\\fault.txt'
# file=r'E:\ģ��\ReleaseV1.02_20190315\data\fault.txt'
# logPath=r'E:\ģ��\ReleaseV1.02_20190315\data\log.txt'
logPath=list[1]+'\\data\\log.txt'
f=open(logPath,"w")
print >>f,u'����'+"    "+'CardNo'+"    "+'CardChannel'
f.close()
    
pos=setup.setUp()
x=pos[0]
y=pos[1]
pyautogui.click(x, y)


timing_x=getPos.get_pos(728,38)[0]
timing_y=getPos.get_pos(728,38)[1]
pyautogui.click(timing_x, timing_y)         #��ʱ��Ϣ

app.connect(window_name)
for i in range(int(list[4])):
    v_value=random.uniform(0.0,5.0)
    checkV_x=x+116
    checkV_y=y+144
    fill.fill_vVal(checkV_x, checkV_y, 0.0, 5.0)             #�����ѹ�����,������ֵ
    
    check_x=x+218
    check_y=y+141
    pyautogui.click(check_x,check_y)        #�������ѹ��ť
    app._wait_child(window_name,u'��ʾ','ready',5,1)
#     app.click(window_name,u'��ʾ')
    app.Sendk('ENTER', 1)
    time.sleep(15)

    with open(file,'r') as f:
        for line in f.readlines():
            if 'Normal' in line:
                f = open(logPath,"a")
                print >> f,str(i)+"        "+line.split('  ')[0]+"        "+line.split('  ')[1]
                f.close()
    
