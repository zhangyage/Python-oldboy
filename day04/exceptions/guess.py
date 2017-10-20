#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

num = random.randint(0,100)

while True:
    try:
        guess = int(raw_input("Enter 1~100:"))
    except ValueError,e:   #当guess输入时判断输入的是否是数字
        print "Enter 1~100"
        continue
    if guess > num:
        print "guess Bigger:",guess
    elif guess < num:
        print "guess Smaller:",guess
    else:
        print "Guess Ok,Game Over!" 
        break
    print "\n"