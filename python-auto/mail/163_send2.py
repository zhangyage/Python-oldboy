#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
import string

HOST="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址  
SUBJECT = "test email from python"                   #定义邮件的主题
#TO = "2213561999@qq.com"                             #定义收件收件人
TO = "zhangyage@yazhoujuejin.com"
FROM="zhangyage2015@163.com"                         #定义发件人
password="zhang19910610"                             #密码  
text = "python rules them all!"
#定义和组装邮件的主题内容
BODY = string.join(("From:%s" % FROM,
                   "TO:%s" % TO,
                   "Subject:%s" % SUBJECT,
                   "",
                   text
                   ),'\r\n')

server = smtplib.SMTP()     #创建一个SMTP对象
server.connect(HOST, "25")  #通过connect方法链接smtp主机
server.starttls()           #启动发圈传输模式
server.login("zhangyage2015@163.com", password)   #邮箱校验
server.sendmail(FROM, [TO], BODY)                 #邮件发送
server.quit()                                     #端口smtp链接
