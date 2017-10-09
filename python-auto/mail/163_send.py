#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
import string
from email.mime.text import MIMEText 

HOST="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址  
SUBJECT = u"官网流量报表"                   #定义邮件的主题
#TO = "2213561999@qq.com"                             #定义收件收件人
TO = "zhangyage@yazhoujuejin.com"
FROM="zhangyage2015@163.com"                         #定义发件人
password="zhang19910610"                             #密码  
#定义和组装邮件的主题内容
msg = MIMEText('''
    <table width="800" border="0" cellpadding="4" cellspacing="0">
        <tr>
             <td bgcolor="#999999" height="20" style="font-size:14px">官网数据   <a href="www.baidu.com">更过</a></td>
        </tr>
    </table>''',"html","utf-8"
    )

msg['Subject'] = SUBJECT  #邮件的主题
msg['From'] = FROM        #发件人邮件的头部可见
msg['To'] = TO
try:
    server = smtplib.SMTP()     #创建一个SMTP对象
    server.connect(HOST, "25")  #通过connect方法链接smtp主机
    server.starttls()           #启动发圈传输模式
    server.login("zhangyage2015@163.com", password)   #邮箱校验
    server.sendmail(FROM, [TO], msg.as_string())                 #邮件发送
    server.quit()                                     #端口smtp链接
    print "邮件发送成功！"
except Exception,e:
    print "失败" +str(e)
