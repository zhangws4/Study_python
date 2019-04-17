#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/4 14:21
#@Author  :一剑霜寒 
#@FileName: p6_5.py

#@Software: PyCharm Community Edition

# 在理解方面，我更倾向于这一种的递归

def f(n):

    if n == 1:
        return 1
    else:
        return n * f(n-1)
number = int(input("请输入一个整数："))
result = f(number)
print(result)
