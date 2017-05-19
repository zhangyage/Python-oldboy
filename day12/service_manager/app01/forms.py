#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django import forms


class Alogin(forms.Form):
    username = forms.CharField(error_messages={'required':'用户名不能为空','invalid':'用户名格式错误'})
    email = forms.EmailField(error_messages={'required':'邮箱不能为空','invalid':'邮箱格式错误'})
    #制定为邮箱格式
    #这个是优化定义的错误信息输出中文  对应的报错默认是英文的   我们可以找CharField-->Field中可以找到默认的key值
    