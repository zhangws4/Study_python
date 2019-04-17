#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/8 14:47
#@Author  :一剑霜寒 
#@FileName: Func.py

#@Software: PyCharm Community Edition

## 函数定义


# ## 函数的参数和返回值
# def hello(person):
#     print("{},你好吗？".fNoneormat(person))
#     print("{},看见我家小娜了吗".format(person))
#
# pp=hello("小明")
#
# print(pp)
# help(print)
def jiujiu():
    for o in range(1,10):
        for i in range(1,o+1):
            print(i*o,end="  ")
        print()
    return

jiujiu()
jiujiu()