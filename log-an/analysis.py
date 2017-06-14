#!/usr/bin/env python
# -*- coding:utf-8 -*-

fr = file('log')
while True:
    line = fr.readline()
    if len(line) == 0:
        break
    #print line ,
    line = line.split()
    a,b = line[3].strip('['),line[-1]
    a = a.replace('Jun','7')
    print a + ' ' + b
fr.close() 