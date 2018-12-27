#!/usr/bin/env python
# -*- coding:utf-8 -*-

products = [['iphone', 6888],['MacPro', 14800],['coffee',31],['mi6',2499],['Book',80],['Book2',799]]
shop_cart = []


while True:
    print '-----------商品列表-----------'
    for i in range(len(products)):
        print i,'.',products[i][0] , products[i][1]
        
    choice = raw_input('请输入你要选择的商品编码号：' )
    if choice.isdigit():
    # choice.isdigit() 判断是否是数字
        if -1<int(choice) and int(choice)<len(products):
        #判断您输入的数字是否在索引范围内
            shop_cart.append(products[int(choice)])
        else:
            print('商品不存在')
    else:
        print ('----------您购买的商品如下：------------')
        for i in range(len(shop_cart)):
            print i,'.',shop_cart[i][0] , shop_cart[i][1]
        break
        
    

    