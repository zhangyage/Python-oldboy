#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
异常学习
1、输入：abc/123
报错            ImportError: No module named abc
2、输入：account/123
报错            AttributeError: 'module' object has no attribute '123'

except ImportError,e                  #单异常
except (ImportError,AttributeError)   #多异常
except Exception,e:                   #Exception代表其他的一切错误  大Boss
finally:                              #最终一定会执行的，不管是否有异常
'''

#实例二   传输URl返回不同的结果
data = raw_input('请输入地址:')
#url格式  account/login

arry = data.split('/')
try:
    userspance = __import__('backend.'+arry[0])
    model = getattr(userspance, arry[0])
    func = getattr(model, arry[1]) 
    func()
except (ImportError,AttributeError),e:                #e就是我们我们错误的对象本身      当有多重异常时可以使用(ImportError,AttributeError)表示
    print e        
    print '访问的页面不存在，跳转首页'

except Exception,e:      #Exception代表其他的一切错误
    print 2,e
    print '其他错误出现，跳转首页'
    
else:                   #正确输入的情况下执行            account/login
    print '正常没有事情啊'
    
finally:                #最后执行，不过你输入的对与错
    print '不管有没有异常都执行'


