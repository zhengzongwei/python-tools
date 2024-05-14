#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import toml

"""
################################################################
# description: MongoDB 数据库的读写操作
# author: zhengzongwei@foxmail.com
################################################################
"""


class MongoException(object):
    pass


class MongoBase(object):
    def __init__(self, ip=None, port=None, username=None, password=None, **kwargs):
        self.ip = ip if ip else "localhost"
        self.port = port if port else 27017
        self.client = pymongo.MongoClient(ip, port, username=username, password=password, **kwargs)

    def createUser(self):
        pass

    def show_dbs(self):
        dbs_names = self.client.list_database_names()
        return dbs_names

    def __del__(self):
        try:
            self.client.close()
        except Exception as e:
            pass


class MongoOperation(object):

    @staticmethod
    def insert_one(collection, data):
        result = collection.insert_one(data)
        return result.inserted_id

    @staticmethod
    def insert_many(collection, data_list):
        result = collection.insert_many(data_list)
        return result.inserted_ids

    @staticmethod
    def find_one(collection, data, data_field={}):
        if len(data_field):
            result = collection.find_one(data, data_field)
        else:
            result = collection.find_one(data)
        return result

    @staticmethod
    def find_many(collection, data, data_field={}):
        if len(data_field):
            result = collection.find(data, data_field)
        else:
            result = collection.find(data)
        return result

    @staticmethod
    def update_one(collection, data):
        result = collection.update_one(collection, data)
        return result

    @staticmethod
    def update_many(collection, data):
        result = collection.update_many(collection, data)
        return result

    @staticmethod
    def delete_one(collection, data):
        result = collection.delete_one(data)
        return result

    @staticmethod
    def delete_many(collection, data):
        result = collection.delete_many(data)
        return result

    @staticmethod
    def repalce_one(collection, data):
        result = collection.repalce_one(collection, data)
        return result



class Mongo(MongoOperation):
    def __init__(self):
        mongo_config = self.get_mongo_config()
        self.mongo = MongoBase(
            ip=mongo_config['ip'],
            port=mongo_config['port'],
            username=mongo_config['username'],
            password=mongo_config['password'],
        )
        self.collection = self.mongo.client[mongo_config['db_name']]['test']

    @staticmethod
    def get_mongo_config():
        config_file = "./config.toml"

        mongo_config = toml.load(config_file)
        return mongo_config['mongo_huawei']

    def insert_one(self, data):
        # self.collection.insert_one(data)
        return super().insert_one(self.collection, data)

    def find_one(self, data, data_field={}):
        if len(data_field):
            result = self.collection.find_one(data, data_field)
        else:
            result = self.collection.find_one(data)
        return result

if __name__ == '__main__':
    # Mongo().insert_one({'data': ['a', 'bb']})
    print(Mongo().find_one({"level": 'error'}))
