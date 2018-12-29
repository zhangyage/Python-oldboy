#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
要求，交互实现控制循环的次数
'''

print_num = int(raw_input('请输入你要循环到那个数字：'))
count = 0
while True:
    count +=1
    print 'loop:',count
    if count == print_num:
        print "已经到达指定位置:",count
        choice = raw_input("你是否继续进行循环，请输入(y/n):")
        if choice == 'y':
            print_num = int(raw_input('请输入你要循环到那个数字：'))
                
            if print_num <= count:
                print_num = int(raw_input("这个位置已经过去了，建议您输入一个更大的数字："))           
        else:
            break

else:
    print "循环结束了"       



            
            
