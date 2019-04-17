#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/6 15:33
#@Author  :一剑霜寒 
#@FileName: p9_1.py

#@Software: PyCharm Community Edition

try:

 file_name = input("请输入要打开文件的名字：")
 str1 = str("C:\\Users\\hc\\Desktop\\EMEA\\")
 f = open(str1 + file_name,'r')
 print("文件的内容是：")

 for each in f:
          print(each)

except OSError:
    print("文件袋开的过程出错了")