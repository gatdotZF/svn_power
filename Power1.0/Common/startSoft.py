#! /usr/bin/env python
#coding=GB18030
import time

import pyautogui

import auto_lib as pywin 
import getPos

# window_name=u'科梁电池模拟器监控软件V1.0.2'
app=pywin.Pywin()
def login(tl_dir,tl_name,window_name):
    app.start(tl_dir,tl_name)
    app._wait(window_name, 'exists', 5, 1)

def max(window_name):
    controller='TitleBar'
    app.connect(window_name)
    app.click(window_name,controller)
    x=getPos.get_pos(0,0)[0]
    y=getPos.get_pos(0,0)[1]
    pyautogui.doubleClick(x, y)
if __name__=='__main__':
    login(u'E:\模拟\ReleaseV1.02_20190315','BatterySimulator.exe',)
    max()