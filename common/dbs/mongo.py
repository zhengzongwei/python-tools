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


class MongoBase(object):
    def __init__(self):
        self.db_name: str = ''
        self.collection_name: str = ''
        mongo_config = self.get_mongo_config()
        self.ip: str = mongo_config['ip'] if mongo_config['ip'] else "localhost"
        self.port: int = mongo_config['port'] if mongo_config['port'] else 27017

        self.db_name = mongo_config['db_name']
        self.client = pymongo.MongoClient(mongo_config['ip'],
                                          mongo_config['port'],
                                          username=mongo_config['username'],
                                          password=mongo_config['password'])

    @staticmethod
    def get_mongo_config():
        config_file = "./config.toml"
        mongo_config = toml.load(config_file)
        return mongo_config['mongo_huawei']

    def create_user(self):
        pass

    def create_collection(self):
        pass

    def check_db_exists(self) -> bool:
        if self.db_name not in self.client.list_database_names():
            return False
        return True

    def check_collection_exists(self) -> bool:
        if self.collection_name not in self.client[self.db_name].list_collection_names():
            return False
        return True

    def show_dbs(self):
        dbs_names = self.client.list_database_names()
        return dbs_names

    def show_collection(self):
        pass

    def __del__(self):
        try:
            self.client.close()
        except Exception as e:
            pass


class Mongo(MongoBase):
    def __init__(self, collection_name):
        # self.mongo = MongoBase()
        super().__init__()
        self.collection = self.client[self.db_name][collection_name]

    def insert_one(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id

    def insert_many(self, data_list):
        result = self.collection.insert_many(data_list)
        return result.inserted_ids

    def find_one(self, data, field=None):
        result = self.collection.find_one(data, field)
        return result

    def find_many(self, data, field=None):
        if field is None:
            result = self.collection.find(data)
        else:
            result = self.collection.find(data, field)
        return result

    def update_one(self, data):
        result = self.collection.update_one(self.collection, data)
        return result

    def update_many(self, data):
        result = self.collection.update_many(self.collection, data)
        return result

    def delete_one(self, data):
        result = self.collection.delete_one(data)
        return result

    def delete_many(self, data):
        result = self.collection.delete_many(data)
        return result

    def replace_one(self, data):
        result = self.collection.repalce_one(self.collection, data)
        return result

    def __del__(self):
        try:
            self.collection.close()
        except Exception as e:
            pass


if __name__ == '__main__':
    mongo = Mongo('test')
    mongo.insert_one({"auth": "测试", "oo": "test"})
    # mongo.insert_many([{
    #     "log_level": "error",
    #     "log_message": "数据库错误"
    # }, {
    #     "log_level": "info",
    #     "log_message": "数据库已连接"
    # }
    # ])
    # print(mongo.find_one({"oo": 'test'}, {'log_level': 'info'}))
