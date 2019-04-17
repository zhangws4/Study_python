#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/4 10:28
#@Author  :一剑霜寒 
#@FileName: pa.py

#@Software: PyCharm Community Edition


import urllib.request

response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html =html.decode("utf-8")
print(html)