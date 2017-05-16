#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField(required=True,error_messages={'invalid':u'邮箱格式错误'})
    typeid = forms.IntegerField()