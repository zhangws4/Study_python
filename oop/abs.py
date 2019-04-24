#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/23 13:52
#@Author  :一剑霜寒 
#@FileName: abs.py

#@Software: PyCharm Community Edition


import abc


# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass

    # 定义静态抽象方法
    @abc.abstractclassmethod
    def play():
        pass

