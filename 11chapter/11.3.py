#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/3 17:58
#@Author  :一剑霜寒 
#@FileName: 11.3.py

#@Software: PyCharm Community Edition


class parent:
    def hello(self):
        print("正在调用父类的方法")


class Child(parent):
    print("你大爷的fuck")


P = parent()
P.hello()

