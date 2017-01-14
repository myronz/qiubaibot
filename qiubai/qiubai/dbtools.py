# -*- coding: utf-8 -*-

import pymysql.cursors

class Dbtools(object):
    def __init__(self, host, user, password, db, charset = 'utf8mb4'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
       
        #获取数据库资源  connection
        try:
            connection = pymysql.connect(
                            host = host,
                            user = user,
                            password = password,
                            db = db,
                            charset = charset
                        )
        except Exception as e:
            print('*********** Error **********')
            print(e[0])
            print(e[1])
            print('*********** Error **********')
        self.connection = connection


    #执行数据（增删改）
    def execute(self, sql):
        try:
            cursor = self.connection.cursor()
            result = cursor.execute(sql)
            self.connection.commit()
            return result
        except Exception as e:
            print('*********** Error **********')
            print(e[0])
            print(e[1])
            print('*********** Error **********')
            self.connection.rollback()
        finally:
            if self.connection is not None:
                self.connection.close()

    #查询数据
    def select(self, sql):
        try:
            with self.connection.cursor() as cursor:
                # 执行查询
                cursor.execute(sql)

                # 获取查询结果
                result = cursor.fetchall()
                self.connection.commit()
                return result
        except Exception as e:
            print('*********** Error **********')
            print(e[0])
            print(e[1])
            print('*********** Error **********')
            self.connection.rollback()
        finally:
            if self.connection is not None:
                self.connection.close()

    #关闭资源
    def close(self):
        self.connection.close()