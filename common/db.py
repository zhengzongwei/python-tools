import mariadb
import logging

module_logger = logging.getLogger("mariadb")


class MariaDB(object):
    def __init__(self, user, password, host, port=3306, charset="utf8"):
        conn_params = {
            "user": user,
            "password": password,
            "host": host,
            "port": port,
            "connect_timeout": 5
        }
        self.conn = None
        self.cursor = None
        try:

            self.conn = mariadb.connect(**conn_params)
            # 显示提交事务
            # self.conn.autocommit(False)
            # self.conn.character_set(charset)
            self.cursor = self.conn.cursor()
        except mariadb.Error as e:
            self.close()
            module_logger.error("MariaDB Error %s" % e)

    def __del__(self):
        self.close()

    def get_db_version(self):

        (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION) = self.conn.get_server_version()
        version_info = "%d.%d.%d" % (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)
        return version_info

    def selectDb(self, db):
        try:
            self.conn.select_db(db)
        except mariadb.Error as e:
            module_logger.error("MariaDB Error %s" % e)

    def query(self, sql):
        try:
            rows = self.cursor.execute(sql)
            return rows
        except MariaDB.Error as e:
            module_logger.error("MariaDB execute sql [%s],err=%s" % (sql, e))

    def showAllDbs(self):
        dbs = []
        sql = "show databases;"
        self.query(sql)
        result = self.fetchAll()
        for info in result:
            dbs.append(*info)
        return tuple(dbs)

        # return rows

    def fetchOne(self):
        result = self.cursor.fetchone()
        return result

    def fetchAll(self):
        result = self.cursor.fetchall()
        # desc = self.cursor.description
        return result

        # for inv in result: 
        #     _d = {} 
        #     for i in range(0,len(inv)): 
        #         _d[desc[i][0]] = str(inv[i]) 
        #         d.append(_d) 
        # return d 

    def insert(self, table_name, data):
        pass

    def update(self, table_name, data, condition):
        pass

    def delete(self, table_name, condition):
        pass

    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
            print("[close] MariaDB close cursor")
        if self.conn is not None:
            self.conn.close()
            print("[close] MariaDB close conn")
        print("[close] MariaDB close")


if __name__ == '__main__':
    db_user = 'root'
    db_password = 'zhengzongwei'
    db_host = '192.168.0.185'
    mariadb = MariaDB(db_user, db_password, db_host)
    print(mariadb.showAllDbs())
    # mariadb.fetchOne()
