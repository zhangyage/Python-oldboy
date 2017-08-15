#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
消息发布者
'''
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.75.132'))
channel = connection.channel()
channel.queue_declare(queue='cc')  #如果有cc的队列，掠过；如果没有，创建cc的队列

channel.basic_publish(exchange='',routing_key='cc',body='hello!world!!!')
print("[x] sent 'hello,world!'") 
connection.close()