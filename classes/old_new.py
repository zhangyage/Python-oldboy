#!/usr/bin/env python
# -*- coding:utf-8 -*-
import new


#新类和老类的比较

class OldStyle:
    def __init__(self,name,description):
        self.name = name
        self.description = description

class NewStyle(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description

if __name__ == "__main__":
    old = OldStyle('old','old style class')
    print old
    print type(old)
    print dir(old)
    print '-------------------------------'*3
    new = NewStyle('new','new style class')
    print new
    print type(new)
    print dir(new)
    
'''
<__main__.OldStyle instance at 0x0000000002790F48>
<type 'instance'>
['__doc__', '__init__', '__module__', 'description', 'name']
-------------------------------------------------------
<__main__.NewStyle object at 0x000000000278CDA0>
<class '__main__.NewStyle'>
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'description', 'name']
'''