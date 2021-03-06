#! /usr/bin/env python
#coding=GB18030
from xlutils.copy import copy
from xlrd import open_workbook
import os,sys
import xlwt
print sys.path
import Common.readConifg as readConfig

list=readConfig.readIniConifg('Power')
file=list[1]+'\\data\\fault.txt'
def wrexcel(row,column,val,sheetNum,data_style):
    f=open('name_exc')
    name=f.read()
    f.close()
    excel=r'./%s'%name
    rb=open_workbook(excel,formatting_info=True)
    wb=copy(rb)
    sheet=wb.get_sheet(sheetNum)
    borders=xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    data_style.borders=borders
    sheet.write(row,column,val,data_style)
#     sheet.col(column).width=cell_width
    os.remove(excel)
    wb.save(excel)
row=3
count=0
with open(file,'r') as f:
    for line in f.readlines():
        line=line.strip('\n').split("  ")
#         print line
        style='pattern: pattern solid, fore_colour white; '
        style += 'font: bold on; '
        style += 'align: horz center, vert center; '
        d_style=xlwt.easyxf(style)
        wrexcel(row+count, 3, line[0], 0, d_style)
        wrexcel(row+count, 4, line[1], 0, d_style)
        wrexcel(row+count, 6, line[3], 0, d_style)
        if line[2] == "Normal":
            wrexcel(row+count, 7, line[2], 0, d_style)
            wrexcel(row+count, 8, '', 0, d_style)
        else:
            wrexcel(row+count, 7, ' ', 0, d_style)
            wrexcel(row+count, 8, line[2], 0, d_style)
        count+=1