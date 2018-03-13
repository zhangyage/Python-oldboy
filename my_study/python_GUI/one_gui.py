#!/usr/bin/env python
# -*- coding:utf-8 -*-


import Tkinter
from Tkinter import *

a = Tkinter.Tk()               #实例化
a.wm_title("这是一个测试窗口")     #创建窗口标题
b=Tkinter.Label(a,text="Hello! 大家好！") #定制窗口内容
b.pack()               #绑定
a.mainloop()           #死循环  要不窗口就一闪而过