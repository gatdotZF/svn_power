#! /usr/bin/env python
#coding=GB18030
import os
import time
import sys
import Common.readConifg as readConfig
from fileinput import filename
def creatFile(path,folder_Name):
    #创建文件夹
    list=readConfig.readIniConifg('Power')
    saveSpace=list[1]
    path = saveSpace+'\\'+folder_Name
    if not os.path.exists(path):
        os.mkdir(os.path.join(saveSpace,folder_Name))      #saveSpace下新建report文件夹
    return 

# def creatTimeFile(path):
#     now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
#     os.mkdir(os.path.join(path,now))                      #path路径下新建以时间命名的文件夹
#     return
       
if __name__=='__main__':
    list=readConfig.readIniConifg('Power')
    folder_Name=r'report'
    path=list[1]+'\\'+folder_Name   
    creatFile(path,folder_Name)
#     creatTimeFile(path)