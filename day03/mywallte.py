#!/usr/bin/env python
# -*- coding:utf-8 -*-

import calendar
print calendar.monthrange(2017, 6)
#calendar.monthrange(year, month)：判断由year和month组成月份，返回该月第一天为周几和该月总共有多少天
#这个判断中0是周一

#help(calendar)