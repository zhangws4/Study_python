#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/3 16:37
#@Author  :一剑霜寒 
#@FileName: 10.1.py

#@Software: PyCharm Community Edition

import  easygui as g
import  sys

while 1:
    g.msgbox("Hi~ o(*￣▽￣*)ブ，欢迎进入第一个界面小游戏^_^")
    msg="请问你希望再鱼C工作室学习到什么知识呢？"
    title= "小游戏互动"
    choices=["谈恋爱","编程","OOXX","琴棋书画"]
    choice = g.choicebox(msg,title,choices)

    g.msgbox("你的选择是：" + str(choice),"结果")
    msg = "你希望重新开始小游戏吗"
    title = "请选择"

if g.ccbox(msg,title):
    pass
else:
    sys.exit(0)