#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
购物车程序，根据自己的工资水准选择不同的商品购买
'''
import pickle
#导入pickle模块，序列化列表存储到文件

product_info={'apple':10,'banana':20,'orange':30,'pear':40,'watermelon':50}
#定制商品详情

while True:
    try:
        money = int(raw_input('please input your money:'))
    except ValueError:
        print "输入错误，这里只能输入你的金额，记得一定要是数字哦！"
    else:
        break
        
                
f = file('list.txt','w')
lists = []
while True:     
    print '''
balance: %s
------------------------
|      product list    |
------------------------
|product    |   price  |                  
------------------------
apple           10
banana          20
orange          30
pear            40
watermelon      50
------------------------
''' % (money)
    product = raw_input('what do you want,please input:')
    money = money - product_info[product]
    if money >= 0:
        lists.append(product)
        choice = raw_input("Do you want to continue,please input y|n:")
        if choice == 'y':
            continue
        else:
            break
    else: 
        print "wanning! -not sufficient funds！"
        break
    
pickle.dump(lists, f, True)   
f.close()
f2=file('list.txt','rb')
#以读的方式打开文件
t=pickle.load(f2)
print "你已经购买的商品有：" , t
f2.close()


