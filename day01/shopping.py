#!/usr/bin/env python
# -*- coding:utf-8 -*-

products = [['iphone', 6888],['MacPro', 14800],['coffee',31],['mi6',2499],['Book',80],['Book2',799]]
while true:
    print '-----------商品列表-----------'
    for i in range(len(products)):
        print i,'.',products[i][0] , products[i][1]
        
    choice = int(raw_input('请输入你要选择的商品编码号' ))   
        
    

    