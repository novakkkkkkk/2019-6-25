#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import xlwt

wr = xlwt.Workbook()
sheet = wr.add_sheet('test')
sheet.write(1,0,'刘哲小店')
sheet.write(1,1,r'C:\Users\andreprevin\Desktop\新运营平台\测试用图片\5.jpg')


wr.save('test_mdxfZB.xls')