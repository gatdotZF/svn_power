#! /usr/bin/env python
#coding=GB18030
import os
import time
import sys
import Common.readConifg as readConfig
from fileinput import filename
def creatFile(path,folder_Name):
    #�����ļ���
    list=readConfig.readIniConifg('Power')
    saveSpace=list[1]
    path = saveSpace+'\\'+folder_Name
    if not os.path.exists(path):
        os.mkdir(os.path.join(saveSpace,folder_Name))      #saveSpace���½�report�ļ���
    return 

# def creatTimeFile(path):
#     now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
#     os.mkdir(os.path.join(path,now))                      #path·�����½���ʱ���������ļ���
#     return
       
if __name__=='__main__':
    list=readConfig.readIniConifg('Power')
    folder_Name=r'report'
    path=list[1]+'\\'+folder_Name   
    creatFile(path,folder_Name)
#     creatTimeFile(path)