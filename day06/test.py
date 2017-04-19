#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


file_size = os.stat('ftp_server.py').st_size
#file_size = os.path.getsize('ftp_server.py')
print file_size