#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging

#打开日志文件，没有会创建，level是记录日志的级别设置的info
logging.basicConfig(filename='log_test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(pathname)s %(module)s %(lineno)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
#会直接在前台打印
logging.debug('This message should go to the log file')
logging.warning("user attemped")
logging.critical("server is down")