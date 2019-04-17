#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/27 11:02
#@Author  :一剑霜寒 
#@FileName: p2_1.py

#@Software: PyCharm Community Edition

# 三元 操作 符号 a = x if x < y else y


"""  第一个游戏  """
import random

secret = random.randint(1,10)
temp = input("不妨猜一下小甲鱼现在的心情是想的那一个数字呢：")
guess = int(temp)

while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("你是小甲鱼肚子里面的小蛔虫吗")
        print("猜对了也没有奖励 哈哈！")
    else:
        if guess > secret :
            print("哥哥 大了 大了····")
        else:
            print("嘿！ 小了 ---")
            print("游戏结束不玩了。。。")



