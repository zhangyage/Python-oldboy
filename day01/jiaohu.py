#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
name = raw_input('Please input your name:')
age = raw_input('your age:')

#print 'name:'+ name + 'age' + age
print("name:{0},age:{1}".format(name,age))
'''
name = raw_input('Please input your name:')
age = int(raw_input('your age:'))
job = raw_input('your job:')
Salary = raw_input('your salary:')

if age > 40:
    msg = "you are old"
else:
    msg = "you are young"
print '''
--------------------------------------------------
Personal information of %s:
    Name:%s
     Age:%s
     Job:%s
  Salary:%s  
--------------------------------------------------
msg:%s
--------------------------------------------------
'''%(name,name,age,job,Salary,msg)
