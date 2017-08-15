#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
接收端
'''
import pika
from pika.amqp_object import Properties

#创建一个连接对象，对象中绑定了rabbitmq的IP
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.75.132'))
#创建一个频道对象
channel = connection.channel()
#频道中声明制定queue,如果有cc的队列，掠过；如果没有，创建cc的队列
channel.queue_declare(queue='cc')

#定义回调函数
def callback(ch,method,Properties,body):
    print ('[x] Recieved %r'%body)
    #channel.close()
#no_ack=Fales:表示消费完以后不主动把状态通知rabbitmq,callback:回调函数,queue:指定队列
channel.basic_consume(callback, queue='cc', no_ack=True)

print ('[*] Waiting for msg')  

channel.start_consuming()  