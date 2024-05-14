#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/1 15:02                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import redis

from utils.logger import Logger

LOG = Logger("redis").getLogger()
class RedisClient(object):
    def __init__(self, username=None, password=None, host='localhost', port=6379, db=0):
        try:
            self.redis_conn = redis.Redis(username=username, password=password, host=host, port=port, db=db)
            LOG.info("redis client connected")
            # 尝试执行一个简单的操作来验证连接
            if not self.redis_conn.ping():
                LOG.error("Failed to ping Redis server: Connection is not healthy")
                return
        except redis.AuthenticationError:
            LOG.error(f"Redis authentication")
        except Exception as e:
            LOG.error("Failed to connect to Redis: %s" % str(e))

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
