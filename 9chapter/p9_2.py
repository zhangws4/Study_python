
#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/7 10:50
#@Author  :一剑霜寒 
#@FileName: p9_2.py

#@Software: PyCharm Community Edition

# try:
#     sum = 1 +'1'
#     f=open("我是一个不存在的文档.txt")
#     print(f.read())
#     f.close()
# except OSError as reason:
#     print("文件出错了T_T\n错误的原因是：" + str(reason))
# except TypeError as reason:
#     print("类型错误了\n错误的原因是：" + str(reason))



try:

    f =open("D:\\gooldata\\中谷Python学习视频.txt")
    print(f.read())
    sum = 1 + '1'
    f.close()
except:
    print("出错了")
finally:
    f.close()