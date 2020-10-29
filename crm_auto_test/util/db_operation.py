

import pymysql

from util.auto_log import AutoLog


class DbOperation:
    def __init__(self, host="106.15.34.49", user="root", password="123456", database="crm", port=3306, charset="utf8"):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.port=port
        self.charset=charset

    def get_conn(self):
        try:
            conn = pymysql.Connection(host=self.host, user=self.user, password=self.password,
                                           database=self.database, port=self.port, charset=self.charset)
            AutoLog.set_messge("database:{} 连接".format(self.database), "info")
            return conn
        except Exception as e:
           AutoLog.set_messge(e, "error")


    def findall(self,sql):
        conn = self.get_conn()
        try:
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute(sql)
            result = cur.fetchall()
            AutoLog.set_messge("sql:{} 执行".format(sql), "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")
            conn.rollback()
        finally:
            cur.close()
            conn.close()
            return result

    def update(self,sql):
        conn = self.get_conn()
        try:
            # sql的执行
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute(sql)
            conn.commit()
            AutoLog.set_messge("sql:{} 执行".format(sql), "info")
        except Exception as e:
            conn.rollback()
            AutoLog.set_messge(e, "error")

        finally:
            cur.close()
            conn.close()


if __name__ == '__main__':
    do=DbOperation()
    print(do.findall("select * from crm.customer_info where customer_name='李四'"))