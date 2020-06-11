#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time

import SendKeys
from pywinauto import application


class Pywin(object):
    def __init__(self):
        self.app = application.Application(backend='uia')
        
        
#     @exp._exception
    def start(self,tl_dir,tl_name):
        _dir=os.getcwd()
        os.chdir(tl_dir)
        self.app.start(tl_name)
        os.chdir(_dir)
        
#     @exp._exception
    def connect(self, window_name):
        self.app.connect(title = window_name)
        
#     @exp._exception
    def pr(self, window_name):
        self.app[window_name].print_control_identifiers()
        
#     @exp._exception
    def close(self, window_name,contorl):
        self.app[window_name][contorl].click_input()
        self.app[window_name][u'确定'].click_input()
        
#     @exp._exception
    def max_window(self, window_name):
        self.app[window_name].Maximize()
        
#     @exp._exception
    def menu_click(self, window_name, menulist):
        self.app[window_name].MenuSelect(menulist)
        
#     @exp._exception
    def input(self, window_name, controller, content):
        self.app[window_name][controller].type_keys(content)
        
#     @exp._exception
    def click(self, window_name, controller):
        self.app[window_name][controller].click_input()
        time.sleep(1)
        
#     @exp._exception
    def right_click(self, window_name, controller):
        self.app[window_name][controller].right_click_input()
        
#     @exp._exception
    def double_click(self, window_name, controller, x ,y):
        self.app[window_name][controller].double_click_input(button = "left",coords = (x, y))
        
#     @exp._exception
    def focus(self,window_name,controller):
        self.app[window_name][controller].set_focus()
        
#     @exp._exception
    def drag(self,window_name,controller,dx,dy,sx,sy):
        self.app[window_name][controller].drag_mouse_input(dst=(dx,dy),src=(sx,sy),button='left',pressed='',absolute=True)
        
#     @exp._exception
    def Sendk(self,key_name,times):
        SendKeys.SendKeys('{%s %d}'%(key_name,times))
        
#     @exp._exception
    def _wait(self, window_name, wait_for, time, interval):
        self.app[window_name].wait(wait_for, timeout=time, retry_interval=interval)
    
#     @exp._exception      
    def _wait_child(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait(wait_for, timeout=time, retry_interval=interval)
    
    def _wait_child_nor(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait(wait_for, timeout=time, retry_interval=interval)
    
#     @exp._exception              
    def _wait_not(self,window_name,wait_for, time, interval):
        self.app[window_name].wait_not(wait_for, timeout=time, retry_interval=interval)
    
    
#     @exp._exception         
    def _wait_not_child(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait_not(wait_for, timeout=time, retry_interval=interval)
                     
    def texts(self,window_name,controller):
        value = self.app[window_name][controller].texts()
        return(value[0])
    
if __name__ ==  "__main__":
    app = Pywin()
    print('__file__:', __file__)
    print('realpath of __file__:', os.path.realpath(__file__))
    print('sys.executable:', sys.executable)
    print('realpath of sys.executable:', os.path.realpath(sys.executable))
    print('sys.argv[0]:', sys.argv[0])
    print('realpath of sys.argv[0]:', os.path.realpath(sys.argv[0]))
    print('sys.path[0]:', sys.path[0])
    print('realpath of sys.path[0]:', os.path.realpath(sys.path[0]))
#     window_name = u"科梁电池模拟器监控软件V1.0.2"
#     app.connect(window_name)
#     app.click(window_name, u'系统')


#     print "ss"
#     app.Sendk('ENTER', 1)