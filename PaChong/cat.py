#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/4 10:50
#@Author  :一剑霜寒 
#@FileName: cat.py

#@Software: PyCharm Community Edition


import  urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()

with open('cat_200_300.jpg','wb') as f:
    f.write(cat_img)