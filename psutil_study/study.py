#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil

#查看系统全部进程   会打印出系统的pid号
#print psutil.pids()

p = psutil.Process(2324)
print p.name()   #进程名
print p.username()  #进程启动者用户名
print p.exe()    #进程的bin路径
print p.cwd()    #进程的工作目录绝对路径
print p.status() #进程状态
print p.create_time()  #进程创建时间
print p.cpu_times()    #进程的cpu时间信息,包括user,system两个cpu信息
print p.memory_percent()  #进程内存利用率
print p.io_counters()     #进程的IO信息,包括读写IO数字及参数
print p.num_threads()     #进程开启的线程数
