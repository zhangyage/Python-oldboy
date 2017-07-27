#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psutil
import time
import datetime

'''
CPU
'''
print psutil.cpu_times()

#查看cpu的逻辑信息
print psutil.cpu_times(percpu=True)
#查看cpu的时间比
print psutil.cpu_times().user

#查看cpu的逻辑个数
print psutil.cpu_count()
#查看cpu的物理个数：
print psutil.cpu_count(logical=False)


'''
MEM
'''
#查看内存的总体使用情况
mem =  psutil.virtual_memory()
#查看总内存 使用的内存 空闲的内存
print mem.total
print mem.used
print mem.free
#查看虚拟内存的使用情况
print psutil.swap_memory()

#获取登录用户信息
print  psutil.users()
'''
disk
'''
#获取硬盘的使用率
print psutil.disk_usage('/')
#获取磁盘完整的信息报错读写IO等
print psutil.disk_io_counters()
#获取磁盘的分区信息
print psutil.disk_partitions()
#获取磁盘IO的总个数
print psutil.disk_io_counters()
print "-----------------------------------"
#获取单个分区的IO个数：
print psutil.disk_io_counters(perdisk=True)

'''
network
'''
#获取网卡信息
print psutil.net_if_addrs()
#获取网络的总IO
print psutil.net_io_counters()
#获取单个接口的IO
print psutil.net_io_counters(pernic=True)

#获取开机的时间  默认的格式是linux时间格式
print psutil.boot_time()
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")


