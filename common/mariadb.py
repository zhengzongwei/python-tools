import mariadb
import sys
import logging


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
            # TODO 使用日志记录相关错误
            print(f"Error connecting to MariaDB Platform: {e}")
            quit()
        else:
            self.cur = self.conn.cursor()

    def execute_sql(self, sql):
        try:
            self.cur.execute(sql)
        except mariadb.Error as e:
            # TODO 使用日志记录相关错误
            print(f"Error connecting to MariaDB Platform: {e}")
            quit()
        return self.cur.fetchall()

    def __del__(self):
        self.cur.close()
        self.conn.close()





