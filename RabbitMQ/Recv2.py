#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
接收端
acknowledgment 消息不丢失

no-ack ＝ False，如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中
'''
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.75.132'))
channel = connection.channel()
channel.queue_declare(queue='cc')

#定义回调函数
def callback(ch,method,Properties,body):
    print ('[x] Recieved %r'%body)
    #channel.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)
#no_ack=Fales:表示消费完以后不主动把状态通知rabbitmq,callback:回调函数,queue:指定队列
channel.basic_consume(callback, queue='cc', no_ack=False)

print ('[*] Waiting for msg')  

channel.start_consuming()  