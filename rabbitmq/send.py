#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/26 15:51                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('openeuler.dev.com'))
channel = conn.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
conn.close()