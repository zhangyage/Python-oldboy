#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
输入魔术方法进行字符串转换
'''



class Programer(object):   
    def __init__(self,name,age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __str__(self):
        return '%s is %s years old' % (self.name,self.age)

    def __dir__(self):
        return self.__dict__.keys()
        
if __name__ == '__main__':
    p1 = Programer('zhang',25)
    print p1
    print dir(p1)

'''
zhang is 25 years old
['age', 'name']
'''