#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import xlrd
def read_excela(filename):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    data = []

    for i in range(sheet.ncols):
        data.append(sheet.col_values(i)[1])

    return data

'''print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_yyzx.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_fws.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_sj.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_md1.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_md2.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_hbcDCZ.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_fwfDCZ.xls'))
print(read_excela(r'D:\Python project\yunyingpingtai\excel\test_mdxfZB.xls'))'''