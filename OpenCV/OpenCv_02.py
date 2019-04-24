#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/24 15:33
#@Author  :一剑霜寒 
#@FileName: OpenCv_02.py

#@Software: PyCharm Community Edition

import cv2

i=cv2.imread("F:\\OpenCv\\image\\lenacolor.png",cv2.IMREAD_UNCHANGED)
#i=cv2.imread("F:\\OpenCv\\WeChat\\grill.jpg")

cv2.imshow("original",i)
i[1:10,1:10]=[0,0,0]
cv2.imshow("result",i)
cv2.waitKey(0)
cv2.destroyAllWindows()



