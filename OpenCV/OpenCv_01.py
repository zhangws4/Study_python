#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/24 15:01
#@Author  :一剑霜寒 
#@FileName: OpenCv_01.py

#@Software: PyCharm Community Edition


import cv2

#i=cv2.imread("F:\\OpenCv\\image\\lenacolor.png",cv2.IMREAD_UNCHANGED)
i=cv2.imread("F:\\OpenCv\\WeChat\\grill.png")

cv2.imshow("original",i)
i[100:150,100:150]=[255,255,0]
cv2.imshow("result",i)
cv2.waitKey(0)
cv2.destroyAllWindows()

