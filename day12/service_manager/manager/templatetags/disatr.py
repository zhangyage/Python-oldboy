#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.template.base import resolve_variable


register = template.Library()

@register.simple_tag
#上面的这一部分是我们在自定义templatetags中必须写的
def mymethod(v1):
    dict1 = {1:u'亚洲掘金',2:u'石时代',3:u'陨石地带',4:u'岩时代'}
    result = dict1[v1]
    return result
 