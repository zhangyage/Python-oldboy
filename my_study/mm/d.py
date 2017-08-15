#!/usr/bin/env python
# -*- coding:utf-8 -*-

info={'name':'ccorz',
      'job':'IT',
      'company':'ali',
      'age':'18',
      'map':{'china':'beijing','american':'huafu'}

}

print(info)
print(info.items())

for key,val in info.items():
    print key,val