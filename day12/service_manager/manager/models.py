# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=50)
    
    
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    CreateDate = models.DateTimeField(auto_now = True)
    user_type = models.ForeignKey('UserType')


class UserGroup(models.Model):
    GroupName = models.CharField(max_length=50)
    user = models.ManyToManyField('UserInfo')
    
    
class Asset(models.Model):
    hostname = models.CharField(max_length=255)
    ip = models.IPAddressField()
    user_group = models.ForeignKey('UserGroup') 
    
    def __unicode__(self):
        temp = u'当前Asset对象中包含(%s,%s)' %(self.hostname,self.ip)
        return temp
    #使用__unicode__可以定制对象的显示格式