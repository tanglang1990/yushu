import uuid
import random

import pymysql
from pymysql.cursors import DictCursor

'''
    pip install pymysql
'''
connParam = {'host': '127.0.0.1', 'port': 3306, 'user': 'root',
             'password': '123456', 'db': 'demo01'}


# # 普通查询 返回元组
# conn = pymysql.connect(**connParam)  # 创建连接
# cur = conn.cursor()  # 游标
# cur.execute("SELECT id,username, age FROM user")  # 执行
# a = cur.fetchone() # 取出第一条
# print(a)
# a = cur.fetchall() # 取出所有
# print(a)
# a = cur.fetchmany(2) # 取出指定条数
# print(a)
# for r in cur:  # 遍历结果
#     print(r)
# cur.close()  # 关闭游标
# conn.close()  # 关闭连接


# # 字典查询，返回字典
# connParam['cursorclass'] = DictCursor
#
# conn = pymysql.connect(**connParam)
# cur = conn.cursor()  # 游标
# cur.execute("SELECT id,username, age FROM user")
# for r in cur:
#     print(r)
#     print(r['id'])
# cur.close()
# conn.close()


# # 创建连接
# conn = pymysql.connect(**connParam)
# # 创建游标
# cursor = conn.cursor()
# # 执行SQL，并返回收影响行数
# effect_row = cursor.execute("UPDATE user SET username =  CONCAT(username, '1') ")
# print(effect_row)
# effect_row = cursor.execute("update user set username = 'ten1' where id=%s", (1,))
# print(effect_row)
# effect_row = cursor.executemany("insert into user (username, age)values(%s,%s)",
#                                 [('abc123', '18'), ('abc1123', '18')])
# print(effect_row)
# # 提交，不然无法保存新建或者修改的数据
# conn.commit()
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()


# # 获取新创建数据自增ID
# conn = pymysql.connect(**connParam)
# cursor = conn.cursor()
# cursor.execute("insert into user (username, age)values(%s,%s)", (f"腾老师{random.randint(1, 100)}", '18'))
# # 获取最新自增ID
# new_id = cursor.lastrowid
# print(new_id)
# conn.commit()
# cursor.close()
# conn.close()
