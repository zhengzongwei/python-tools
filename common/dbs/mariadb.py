#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mariadb

"""
################################################################
# description: MariaDB 数据库的读写操作
# author: zhengzongwei@foxmail.com
################################################################
"""


class Mariadb(object):

    def __init__(self, host, user, password, dbname):
        schema = {
            'user': user,
            'password': password,
            'host': host,
            'port': 3306,
            'database': dbname
        }
        try:

            self.conn = mariadb.connect(**schema)
        except mariadb.Error as e:
            # TODO (zhengzongwei@foxmail.com) 使用日志记录相关错误
            print(f"Error connecting to MariaDB Platform: {e}")
            quit()
        else:
            if self.conn is not None:
                self.cur = self.conn.cursor()

    def execute_sql(self, sql):
        if self.cur is not None:
            try:
                self.cur.execute(sql)
            except mariadb.Error as e:
                # TODO (zhengzongwei@foxmail.com) 使用日志记录相关错误
                print(f"Error connecting to MariaDB Platform: {e}")
                quit()
            return self.cur

    def fetch_all(self, sql):
        if self.cur is not None:
            try:
                self.execute_sql(sql)
                db_data = self.cur.fetachall()
            except mariadb.Error as e:
                # TODO (zhengzongwei@foxmail.com) 使用日志记录相关错误
                print(f"Error connecting to MariaDB Platform: {e}")
                quit()
            else:
                return db_data

    # def fetch_one(self,sql):
    #     if self.cur is not None:
    #         try:
    #             self.execute_sql(sql)
    #             db_data = self.cur.fetachone()
    #         except mariadb.Error as e:
    #             # TODO (zhengzongwei@foxmail.com) 使用日志记录相关错误
    #             print(f"Error connecting to MariaDB Platform: {e}")
    #             quit()
    #         else:
    #             return db_data

    def update(self, sql):

        if self.cur is not None:
            try:
                self.execute_sql(sql)
                self.conn.commit()
            except mariadb.Error as e:
                self.conn.rollback()
                print(f"Update data Failed, rollback")
                return False
        return True

    def __del__(self):
        self.cur.close()
        self.conn.close()
