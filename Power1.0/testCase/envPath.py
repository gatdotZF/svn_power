#! /usr/bin/env python
#coding=GB18030
import os,sys
if  os.path.exists('testCase') or os.path.exists('Common'):
#     print(sys.path[0])
    sys.path.append(sys.path[0])
else:
    print(os.path.dirname(os.getcwd()))
    sys.path.append(os.path.dirname(os.getcwd()))
