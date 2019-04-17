#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/3 16:05
#@Author  :一剑霜寒 
#@FileName: 9.10.py

#@Software: PyCharm Community Edition



try:

    f =open('D:\\gooldata\\中谷Python学习视频.txt','w')
    for each_lin in f:
        print(each_lin)

except OSError as reason:
    print("出错了")
finally:
    f.close()