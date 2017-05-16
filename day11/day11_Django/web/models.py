# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=50)


#创建表   继承models.Model  但是首先需要执行配置文件我们需要在那个数据库创建我们的表
#这种创建方式叫做codefirst
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    
    password = models.CharField(max_length=50)
    
    email = models.CharField(max_length=50)
    
    Gender = models.BooleanField(default=False)
    
    Age = models.IntegerField(default=22)
    
    memo = models.TextField(default='zhangyage')
    
    CreateDate = models.DateTimeField(auto_now = True)

    typeId = models.ForeignKey('UserType')
    #关联外键是两个表之间建立关系     UserType  一对多
    
class Group(models.Model):
    Name = models.CharField(max_length=50)
    
class User(models.Model):
    Name = models.CharField(max_length=50)
    
    Email = models.CharField(max_length=50)
    
    group_relation = models.ManyToManyField('Group')
    #创建关联关系，多对多的关心中间会生成一个婊记录关系
    
class Args(models.Model):
    name = models.CharField(max_length=50,null=True)
    #制定字段是否可以为空
    not_name = models.CharField(max_length=50,null=False)
    

class Asset(models.Model):
    hostname = models.CharField(max_length=50,null=False)
    
    create_date = models.DateTimeField(auto_now_add = True)
    #auto_now_add = True\auto_now = True自动复制
    update_date = models.DateTimeField(auto_now = True)
    
class User_Info_Temp(models.Model):
    GENDER_CHOICE = (
        ('1',u'普通用户'),
        ('2',u'管理员'),
        ('3',u'超级管理员'),
        )
    UserType = models.CharField(max_length=2,choices=GENDER_CHOICE)
    #设置一个字典类型的字段