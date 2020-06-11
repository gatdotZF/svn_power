#! /usr/bin/env python
#coding=GB18030
import sys

import Common.readConifg as readConfig
import auto_lib as pywin
import getPos
import startSoft as start


def setUp():
#     softDir=u'E:\模拟\ReleaseV1.02_20190315'
    reload(sys)
    sys.setdefaultencoding('GBK')
    list=readConfig.readIniConifg('Power')
    window_name=list[0]
    softDir=list[1]
#     softName='BatterySimulator.exe'
    softName=list[2]

    start.login(softDir, softName,window_name)
    start.max(window_name)
    app = pywin.Pywin()
#     window_name = u"科梁电池模拟器监控软件V1.0.2"
    app.connect(window_name)
    app.click(window_name, u'系统')   #点击选定坐标基值
    return (getPos.get_pos(0,0))     #返回坐标基值
