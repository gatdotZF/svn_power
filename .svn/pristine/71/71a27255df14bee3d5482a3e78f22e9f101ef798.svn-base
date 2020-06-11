#! /usr/bin/env python
#coding=GB18030
import random
import time

import SendKeys
import pyautogui


def fill_vVal(x,y,vMin,vMax):
    pyautogui.click(x,y)            #点击设置输入框    
    v_value=round(random.uniform(vMin,vMax),1)  
    SendKeys.SendKeys("^{a}")
    SendKeys.SendKeys(str(v_value))          #输入值  
    
if __name__=='__main__':
    time.sleep(2)
    fill_vVal(188, 271, 4.5, 5.5)
