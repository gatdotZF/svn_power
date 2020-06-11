#! /usr/bin/env python
#coding=GB18030
import time
import os
import Common.auto_lib as pywin
import pyautogui
import random
import Common.readConifg as readConfig
import Common.fillValue as fillValue
import Common.Init as init
import Common.getPos as getPos
import Common.setup as setup
import Common.lxmlReader as xmlReader
import Common.createFile as creatFile
from pywinauto.base_wrapper import ImageGrab
list=readConfig.readIniConifg('Power')
app = pywin.Pywin()
window_name = list[0]
init.check_exist(list[2])

file=list[1]+'\\config\\config.xml'  
s=open(file,'r')
str1=s.read()
dom=xmlReader.lxmlReader(str1)
cardList=dom.getTabNodeValue('//battery/@cardtype')
s.close()
dic={}
for i in range(15):
    key='cardNo'+str(i)
    value=cardList[0][i]
    dic[key]=value
print dic
pos=setup.setUp()
x=pos[0]
y=pos[1]
pyautogui.click(x, y)

bus_x=getPos.get_pos(74, 38)[0]
bus_y=getPos.get_pos(74, 38)[1]
pyautogui.click(bus_x, bus_y)         #��У׼ҳ��

app = pywin.Pywin()
app.connect(window_name)
t1_x=288
t2_x=688
t3_x=1088
t1_y=t2_y=t3_y=150
t = 0
l=[]
l.append(0)
count=0
def setting(no,t,t_x,t_y):                                      #�����ѹ����ֵ���������ѡ���л�
    card='cardNo'+str(no)
    if int(dic[card]) == 2:
        for a in range(3):
            t=t+1
        l[0]=t
    else:
#         print t
        for a in range(3):
            y=t*39
            if int(dic[card]) == 0:
                fillValue.fill_vVal(getPos.get_MultiPos(t_x,t_y,0,y)[0], getPos.get_MultiPos(t_x,t_y,0,y)[1], 0, 5)
                value=random.randint(0,1)
                if value == 1:
                    pyautogui.click(getPos.get_MultiPos(t_x+120,150,0,y)[0],getPos.get_MultiPos(t_x+120,150,0,y)[1])
                if int(list[3]) == 1:
                    dis=random.choice([143,168,193,218])
                    pyautogui.click(getPos.get_MultiPos(t_x+dis,150,0,y)[0],getPos.get_MultiPos(t_x+dis,150,0,y)[1])
                    time.sleep(1)

            else:
                randValue = random.randint(0,2)
                if randValue == 0 or randValue == 1:
                    fillValue.fill_vVal(getPos.get_MultiPos(t_x,t_y,0,y)[0], getPos.get_MultiPos(t_x,t_y,0,y)[1], 0, 999)
                else:
                    fillValue.fill_vVal(getPos.get_MultiPos(t_x,t_y,0,y)[0], getPos.get_MultiPos(t_x,t_y,0,y)[1], 0, 2)
                time.sleep(1) 
                pyautogui.click(getPos.get_MultiPos(t_x+120,150,0,y)[0],getPos.get_MultiPos(t_x+120,150,0,y)[1])
                time.sleep(1)
                app.Sendk("DOWN", randValue)
                time.sleep(1)
                app.Sendk("ENTER",1)
                time.sleep(1)
                if int(list[3]) == 1:
                    dis=random.choice([143,168])
                    pyautogui.click(getPos.get_MultiPos(t_x+dis,150,0,y)[0],getPos.get_MultiPos(t_x+dis,150,0,y)[1])
                    time.sleep(1)

            t+=1
        l[0]=t


    #�����ļ���
now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
folder_Name=r'report'  
filename = os.path.basename(__file__)       #��ȡ��ǰִ�нű�����
path = list[1]+'\\'+folder_Name
creatFile.creatFile(path,folder_Name)        #������saveSpace�´���folder_Name��Ӧ�����ļ���  
t=filename.split('.')[0]+now
os.mkdir(os.path.join(path,t))             #��folder_Name·���´����Խű�����+ʱ���������ļ���
path1=path+'\\'+t
print filename

for j in range(int(list[4])):                                                  #���Դ���
    for i in range(15):
        if i/5 < 1:                                                 #��һ���������
            setting(i, l[0], t1_x, t1_y)
            if i==4:
                l[0]=0
     
        elif i/5 >= 1 and i/5 < 2:                                  #�ڶ����������
            setting(i, l[0], t2_x, t2_y)
            if i==9:
                l[0]=0
        else:                                                       #�������������
            setting(i, l[0], t3_x, t3_y)
            if i == 14:
                l[0]=0
    pyautogui.click(852,101)                                        #�����·�
    time.sleep(1)
    pyautogui.click(1069,102)                                       #��λ
    print j
     
    #��ͼ
    if j==0 or j==int(list[4])-1:                                      #��ǰ��һ�λ����һ������ʱ��ִ�н�ͼ        
        im=ImageGrab.grab()   
        now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))  
        picFile=path1+'\\'+now+'.png'
        print 'screenshot:'+picFile,len('screenshot:'+picFile)
        im.save(picFile)                                      #��ͼ�洢��report�ļ�����