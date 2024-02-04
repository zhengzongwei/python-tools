#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/1 15:02                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>


import redis


class RedisClient(object):
    def __init__(self, username=None, password=None, host='localhost', port=6379, db=0):
        try:
            self.redis_conn = redis.Redis(username=username, password=password, host=host, port=port, db=db)
        except redis.AuthenticationError:
            print(f"Redis authentication")
        except Exception as e:
            print("Failed to connect to Redis: %s", str(e))

    def set(self, key, value):
        return self.redis_conn.set(key, value)

    def get(self, key):
        return self.redis_conn.get(key)

    def delete(self, key):
        return self.redis_conn.delete(key)

    def exists(self, key):
        return self.redis_conn.exists(key)

    def hset(self, name, key, value):
        return self.redis_conn.hset(name, key, value)

    def hget(self, name, key):
        return self.redis_conn.hget(name, key)

    # Add more methods for other Redis operations as needed


if __name__ == '__main__':
    redis_client = RedisClient('zhengzongwei', 'zhengzongwei', '106.54.39.146')
    redis_client.set("test", "hello world")
