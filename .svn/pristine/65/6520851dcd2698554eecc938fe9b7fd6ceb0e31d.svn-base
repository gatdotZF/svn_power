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
# file=ur"E:\模拟\ReleaseV1.02_20190315\config\config.xml"      
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
pyautogui.click(correct_x, correct_y)         #打开校准页面

app = pywin.Pywin()
window_name = list[0]
app.connect(window_name)


for t in range(15):
    card='cardNo'+str(t)
    pyautogui.click(432,86)                      #选择卡号
    time.sleep(1)
    if t != 0:
        app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
    if int(dic[card]) != 2:
        if t != 0:
            pyautogui.click(599,87)                 #通道号重置为1
            time.sleep(1)
            app.Sendk('UP', 2)
        app.Sendk('ENTER', 1)

        for i in range(3):                           #通道号选择
            pyautogui.click(599,87)                
            time.sleep(1)    
            if i != 0:
                app.Sendk('DOWN', 1)
            app.Sendk('ENTER', 1)
            
            pyautogui.click(1286,85)                #复位
            time.sleep(1)
            
            pyautogui.click(726,86)                #查询板卡信息
            time.sleep(1)
            
            if int(dic[card]) == 0:                    #电压卡设定
                pyautogui.click(133,201)          #电压开环校准
                time.sleep(1)
        
                pyautogui.click(263,207)        #电压闭环校准
                time.sleep(1)
                
                pyautogui.click(361,200)          #电压精度验算
                time.sleep(1)
        
                pyautogui.click(586,201)          #电流校准
                time.sleep(1)
        
                pyautogui.click(698,202)          #电流精度验算
                time.sleep(1)
                
                app.Sendk('LEFT', 1)
                time.sleep(1)
                app.Sendk('ENTER', 1)
                time.sleep(1)
            elif int(dic[card]) == 1:             #若板卡为电阻卡
                pyautogui.click(133,201)          #电阻校准
                
            time.sleep(10)
                