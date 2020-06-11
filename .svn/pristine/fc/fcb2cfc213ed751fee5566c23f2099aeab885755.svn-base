#! /usr/bin/env python
#coding=utf-8
from lxml import etree
class lxmlReader(object):
    def __init__(self,strlXml):
        if type(strlXml) == str:
            self.xml=etree.XML(strlXml)
        else:
            self.xml = etree.parse(strlXml)
    
    def getTabNodeValue(self,xpathName):
        
        value = self.xml.xpath(xpathName)
        return value

if __name__=='__main__':
    str1='''<config>
    <!--15个板卡类型设置：cardtype = "0"为电压卡；cardtype = "1"为电阻卡；cardtype = "2"为未知卡；若卡槽未插卡则必须设置为未知卡-->
    <!--txport表示目标电池模拟器的端口，FPGANumber为FPGA设备号-->
    <batterys>
        <battery name = "电池模拟器1" ip = "192.168.1.6" cardtype = "000200020002000" txport = "50098" mac = "0x100001000000" FPGAVersion = "0x10000101" FPGANumber = "19276"/>
    </batterys>
    
    <!--电流校准有关参数：AD8330MeanCount为校准时AD8330回采电压取平均次数,saveData为是否保存AD8330原始数据,
    StartVolt为电流校准/验算范围下限(单位V),EndVolt为电流校准/验算范围上限(单位V)-->
    <CurrentAdjustParam AD8330MeanCount = "2000" saveData = "true" StartVolt = "0.2" EndVolt = "4.3"/>
    
    <!--定时信息参数: interval表示采样时间间隔，单位ms，范围是[10,3600000];   
                      deviation表示偏差值，单位是V，范围是[0, 5];
                      averageTimes表示电流电压定时采集次数，用于求平均值[11, 1000]-->
    <TimmingInfo interval = "1000" deviation = "0.1" averageTimes = "101"/>
    
    <!--FPGA软件rbf文件下载参数-->
    <FPGAs>
        <FPGA name = "通信FPGA" SwapByte = "true" FlashAddress = "0x000000-0x05FFFF"/>
        <FPGA name = "控制FPGA" SwapByte = "true" FlashAddress = "0x100000-0x15FFFF"/>
    </FPGAs>

    <!--网络通信参数：rxport为本地监听端口-->
    <UDPConfig rxport = "50098"/>
    
    <!--日志信息保存相对路径-->
    <LogConfig>
        <AdjustLogConfig savepath = "data/"/>
        <SystemLogConfig savepath = "log/"/>
    </LogConfig>
    </config>'''
    file=ur"E:\模拟\ReleaseV1.02_20190315\config\config.xml"
    s=open(file,'r')
    str1=s.read()
    dom=lxmlReader(str1)
    cardList=dom.getTabNodeValue('//battery/@cardtype')
    s.close()
    dic={}
    for i in range(15):
        key='cardNo'+str(i)
        value=cardList[0][i]
        dic[key]=value
    print dic