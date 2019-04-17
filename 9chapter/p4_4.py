#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/27 18:20
#@Author  :一剑霜寒 
#@FileName: p4_4.py

#@Software: PyCharm Community Edition


bingo = "小甲鱼是帅哥"

answer = input("请输入小甲鱼想听的一句话：")

while True:
    if answer == bingo:
        break
        answer = input("重新输入：")



print("可以呀")