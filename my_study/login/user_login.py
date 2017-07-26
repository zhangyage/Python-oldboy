#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
判断用户登录   user_list保留用户账号信息  user_lock保留锁定用户信息
'''

import time 
import getpass
import os

user_name = raw_input("请输入你的名字:")

#打开user_lock 和 user_list文件并且给予读写权限
user_list = open('user_list','r+')
user_lock = open('user_lock','r+')

#设置一个日志文件，open如果，用追加模式
log_file = open('login.log','a+')

#设置一个退出的表示
break_flag = 0
time_now = time.strftime('%Y-%m-%d %H:%M:%S')

#核实一下输入的用户是否是锁定用户
for line in user_lock:
    #strip()是将输入两端的空格去除
    lock_name = line.strip()
    #判断输入的用户是否存在于锁定文件中
    if lock_name == user_name:
        print ("您输入的用户已经被锁定，请联系管理员")
        log_file.write('\n%s:被锁定用户：%s尝试登陆！'%(time_now,user_name))
        #修改退出标识符的值,以便区分既在user_list,又在user_lock的用户
        break_flag =1
        break
    
account={}
for line in user_list:
    account[line.strip().split(':')[0]]=line.strip().split(':')[1]
    print account
    
    # break_flag==0用来区分在user_list,user_lock中同时存在的用户,
    # 如果没有此标识符,上面遍历锁用户文件也会执行以下程序
    if user_name in account and break_flag == 0:
        #设置计数器
        count = 0
        #设置循环次数
        while count < 3:
            password = raw_input("请输入%s的密码"%user_name)
            #判断密码是否匹配：
            if password == account[user_name]:
                print ('欢迎登陆系统。。。')
                log_file.write('\n%s:用户：%s登陆成功！'%(time_now,user_name))
                break
            else:
                count+=1
                print ('%s的密码错误,请重新输入,您还有%s次机会'% (user_name,3-count))
        else:
            print('用户%s已经被锁定,请联系管理员!'%user_name)
            # 将密码输入超过3此的用户名添加进user_lock,写入日志文件
            user_lock.write('\n%s'%user_name)
            log_file.write('\n%s:%s is locked!'%(time.strftime('%Y-%m-%d %H:%M:%S'),user_name))
            
    if user_name not in account:
        regis_or_quit = raw_input('''\033[1;44;33m没有用户%s,是否注册此用户?\033[0m
                                     \033[1;44;33m输入"y"继续注册,输入"q"退出:\033[0m'''%user_name)
        if regis_or_quit.lower() == 'q':
            print ('Bye...')
            break
        elif regis_or_quit.lower() == 'y':
            #直接使用user_name注册,第一次输入密码密码,如果不想显示明文密码可用getpass.getpass('...')
            regis_pass=raw_input('请输入%s的密码:'%user_name)
            #允许两次确认密码,设置循环2次,故也无需设置计数器
            for i in range(2):
                #确认注册密码,防止用户忘记密码
                regis_pass_again=raw_input('请确认注册用户%s的密码:'%user_name)
                # 校验注册密码
                if regis_pass_again==regis_pass:
                    # 校验密码成功,将user_name regis_pass两个变量的值写入user_list文件,并提醒用户注册成功
                    user_list.write('\n%s:%s'%(user_name,regis_pass))
                    log_file.write('\n%s:%s注册成功'%(time_now,user_name))
                    print('用户%s注册成功.....'%user_name)
                    # 退出循环
                    break
                #校验注册密码失败,进入下一次循环
                else:
                    print('\033[1;33;44m密码与上次不一致.......\033[0m')
            #密码确认超过两次,注册失败    
            else:
                print('用户%s注册失败'%user_name)
        #输入不为y或者q,其他字符串或者回车 空格时,程序显示退出
        else:
            print('输入不符合规范,程序已退出.....')
user_list.close()
user_lock.close()
log_file.close()
    
                       
   
        
    