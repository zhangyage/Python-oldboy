#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
__new__   __init__
'''


class Programer(object):
    
    def __new__(self, *args, **kwargs):
        print 'call __new__ method!'
        print args
        return object.__new__(self, *args, **kwargs)
    
    def __init__(self,name,age):
        print 'call __init__ method!'
        self.name = name
        self.age = age
        
if __name__ == '__main__':
    programer = Programer('zhang',25)
    print programer.__dict__