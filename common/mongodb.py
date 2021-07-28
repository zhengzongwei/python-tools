#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

"""
################################################################
# description: MongoDB 数据库的读写操作
# author: zhengzongwei@foxmail.com
################################################################
"""


class MongoDB(object):
    def __init__(self, ip, port, db):
        self.ip = ip if ip else "localhost"
        self.port = port if port else 27017
        uri = 'mongodb://%s:%s/' % (self.ip, self.port)
        self.client = pymongo.MongoClient(uri)
        print(self.client)

    def __del__(self):
        self.client.close()
