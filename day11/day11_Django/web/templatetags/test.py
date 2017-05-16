#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.template.base import resolve_variable


register = template.Library()

@register.simple_tag
#上面的这一部分是我们在自定义templatetags中必须写的
def mymethod(v1):
    result = v1*1000
    return result