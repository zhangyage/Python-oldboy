#!/usr/bin/env python
# -*- coding:utf-8 -*-

import global_settings   #先导入设置环境变量的模块
import generic


class cpu(generic.BaseService):   #继承
    def __init__(self):
        super(cpu,self).__init__()  #继承父类的构造函数
        self.name = 'linux cpu'
        self.interval = 30
        self.plugin_name = 'get cpu_status'
        self.triggers = {
            'idle':{'func':avg,
                    'minute':15,
                    'operator':'lt',
                    'waring':20,
                    'critical':5,
                    'data_type':'percentage' 
                   },
            'iowait':{
                    'func':hit,
                    'minute':10,
                    'operator':'gt',
                    'threshold':3,           #报警命中的次数 阈值
                    'waring':50,            #命中超过50% 3次报警 
                    'critical':80,
                    'data_type':'percentage' 
                   },
            }

class memory(generic.BaseService):   #继承
    def __init__(self):
        super(memory,self).__init__()  #继承父类的构造函数
        self.name = 'linux memory'
        self.interval = 60
        self.plugin_name = 'get memory_info'  
        self.triggers = {
            'idle':{'func':avg,
                    'minute':15,
                    'operator':'gt',
                    'waring':20,
                    'critical':5,
                    'data_type':'percentage' 
                   }
            } 
        
if __name__ == '__main__':
    pass
            
    