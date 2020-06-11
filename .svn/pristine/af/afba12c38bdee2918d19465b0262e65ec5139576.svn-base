#! /usr/bin/env python
#coding=GB18030
import ConfigParser,sys,os
def readIniConifg(softName):
    readini = ConfigParser.ConfigParser()
    _file = sys.path[0] + r'\data\mainConfig.ini'
    if not os.path.exists(_file):
        _file = os.path.abspath("..") + r"\data\mainConfig.ini"
    if not os.path.exists(_file):
        _file = os.path.abspath("..\..") + r"\data\mainConfig.ini"
    readini.read(_file)
    section = readini.sections()
    _list=[]
    for sectionInfo in section:
        if sectionInfo in softName:
            for key in readini.options(sectionInfo):
                if readini.get(sectionInfo,key):
                    _list.append(readini.get(sectionInfo,key))
                else:
                    print "Configure file wrong!"
                    exit()
    if len(_list) == 5:
        return _list
    else:
        print 'list length:',len(_list)
        print "Configure file wrong!"
        exit()
if __name__=="__main__":
    print readIniConifg('Power')[0]