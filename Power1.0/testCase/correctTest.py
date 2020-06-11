#! /usr/bin/env python
#coding=GB18030
import time

import pyautogui
import Common.Init as init
import Common.auto_lib as pywin
import Common.getPos as getPos
import Common.setup as setup
import Common.readConifg as readConfig
import Common.lxmlReader as xmlReader
list=readConfig.readIniConifg('Power')
file=list[1]+'\\config\\config.xml'
# file=ur"E:\ģ��\ReleaseV1.02_20190315\config\config.xml"      
s=open(file,'r')
str1=s.read()
dom=xmlReader.lxmlReader(str1)
cardList=dom.getTabNodeValue('//battery/@cardtype')
s.close()
dic={}
for i in range(15):
    key='cardNo'+str(i)
    value=cardList[0][i]
    dic[key]=value

init.check_exist(list[2])

pos=setup.setUp()
x=pos[0]
y=pos[1]
pyautogui.click(x, y)

correct_x=getPos.get_pos(244, 38)[0]
correct_y=getPos.get_pos(244, 38)[1]
pyautogui.click(correct_x, correct_y)         #��У׼ҳ��

app = pywin.Pywin()
window_name = list[0]
app.connect(window_name)


for t in range(15):
    card='cardNo'+str(t)
    pyautogui.click(432,86)                      #ѡ�񿨺�
    time.sleep(1)
    if t != 0:
        app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
    if int(dic[card]) != 2:
        if t != 0:
            pyautogui.click(599,87)                 #ͨ��������Ϊ1
            time.sleep(1)
            app.Sendk('UP', 2)
        app.Sendk('ENTER', 1)

        for i in range(3):                           #ͨ����ѡ��
            pyautogui.click(599,87)                
            time.sleep(1)    
            if i != 0:
                app.Sendk('DOWN', 1)
            app.Sendk('ENTER', 1)
            
            pyautogui.click(1286,85)                #��λ
            time.sleep(1)
            
            pyautogui.click(726,86)                #��ѯ�忨��Ϣ
            time.sleep(1)
            
            if int(dic[card]) == 0:                    #��ѹ���趨
                pyautogui.click(133,201)          #��ѹ����У׼
                time.sleep(1)
        
                pyautogui.click(263,207)        #��ѹ�ջ�У׼
                time.sleep(1)
                
                pyautogui.click(361,200)          #��ѹ��������
                time.sleep(1)
        
                pyautogui.click(586,201)          #����У׼
                time.sleep(1)
        
                pyautogui.click(698,202)          #������������
                time.sleep(1)
                
                app.Sendk('LEFT', 1)
                time.sleep(1)
                app.Sendk('ENTER', 1)
                time.sleep(1)
            elif int(dic[card]) == 1:             #���忨Ϊ���迨
                pyautogui.click(133,201)          #����У׼
                
            time.sleep(10)
                