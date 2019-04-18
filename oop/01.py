#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/17 11:39
#@Author  :一剑霜寒 
#@FileName: 01.py
#@Software: PyCharm Community Edition

"""
定义一个学生类
"""
import numpy
class Student():
    pass
mingyu = Student()
class PythonStudent():
   # 用 None 给不确定的值赋值
    name = None
    age = 18
    course ="Python"

    def doHomework(self):
       print("我在做作业")
       #推荐末尾使用 return
       return None
#这个过程叫做类的实例化， 月月是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传入参数
yueyue.doHomework()
print(PythonStudent.__dict__)