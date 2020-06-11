#! /usr/bin/env python
#coding=GB18030
import os

import win32com.client


def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)
    if len(processCodeCov) > 0:
        os.system('taskkill /IM %s /F'%pro_name)
        return 1
    else:
        print "%s is not exist"%pro_name
        return 0
if __name__=='__main__':
    check_exist('BatterySimulator.exe')
#     os.system('taskkill /IM BatterySimulator.exe /F')