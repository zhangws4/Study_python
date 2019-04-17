#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/3 17:03
#@Author  :一剑霜寒 
#@FileName: 11.2.py

#@Software: PyCharm Community Edition


class Turtle:
    #Python 中的类名约定以大写字母开头
    #特征的描述称为属性，再代码的层面来看就是变量
    color = 'green'
    wwight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
    #方法实际就是函数，通过调用这些函数来完成某些写工作
    def climb(self):
        print("我正在努力的向前爬着")
    def run(self):
        print("我正在飞快的向前跑")
    def bite(self):
        print("咬死你咬死你")
    def eat(self):
        print("有的吃真满足")
    def sleep(self):
        print("困了，睡了，睡了")

tt = Turtle()
tt.bite()
tt.climb()
tt.run()