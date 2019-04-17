#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/3 15:50
#@Author  :一剑霜寒 
#@FileName: 9.8.py

#@Software: PyCharm Community Edition


def showmaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是%d'%(num,count))
            break
        count -= 1
    else:
        print('%d是素数！'% num)
num = int(input('请输入一个数：'))
showmaxFactor(num)

