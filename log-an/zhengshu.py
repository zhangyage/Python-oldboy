#!/usr/bin/env python
# -*- coding:utf-8 -*-

num = raw_input('please input a num:')

def isPrime(n):    
    if n <= 1:    
        return False   
    if n == 2:    
        return True   
    if n % 2 == 0:    
        return False   
    i = 3   
    while i * i <= n:    
        if n % i == 0:    
            return False   
        i += 2   
    return True 


if num.isdigit():
    print True
    isPrime(num)
else:
    print "this is a float!"
    
    
