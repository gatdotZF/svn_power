#! /usr/bin/env python
#coding=GB18030
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
from datetime import *
import os
import sys
import xlwt
import xlrd
import time
from numpy import empty
list=[]
def creatExc(excelName,sheet,row,col,list,data_style):
    
    workbook=xlwt.Workbook(encoding='ascii')
    worksheet=workbook.add_sheet(sheet)
    for i in range(len(list)):
        worksheet.write(row,col+i,list[i],data_style)
        worksheet.col(col+i).width=3000
#     worksheet.write_merge(0,0,5,6,'Value',data_style)
#     worksheet.write_merge(0,0,7,8,'Result',data_style)
    workbook.save('./%s.xls'%excelName)
if __name__=='__main__':
    borders=xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    style='pattern: pattern solid, fore_colour yellow; '
    style += 'font: bold on; '
    style += 'align: horz center, vert center; '
    data_style=xlwt.easyxf(style)
    data_style.borders=borders
    item=['Time',u'次数','Card','Channel','Set','Read','Normal','Fault']
    creatExc('123', 'Sheet1',1, 1, item,data_style)
    