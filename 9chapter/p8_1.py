#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/6 11:28
#@Author  :一剑霜寒 
#@FileName: p8_1.py

#@Software: PyCharm Community Edition


f = open("C:\\Users\\hc\\Desktop\\EMEA\\haha.txt")

for each in f:

    (role,line_spoken,hah) = each.split(",",2)
    print(role)
    print(line_spoken)
    print(hah)
f.close()