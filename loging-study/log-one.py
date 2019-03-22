#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging

#打开日志文件，没有会创建，level是记录日志的级别设置的info
logging.basicConfig(filename='log_test.log',level=logging.INFO)
#会直接在前台打印
logging.warning("user attemped")
logging.critical("server is down")