#!/usr/bin/env python3
# Python 操作MySQL数据库

import pymysql

# 数据库连接
db = pymysql.connect("192.168.10.88", "py", "123", "study")

# 创建一个游标对象
cursor = db.cursor()

# 执行SQL语句
cursor.execute("show tables")

# sql语句
sql = "select * from Person"

try:
    cursor.execute(sql)  # 执行SQL语句
    rs = cursor.fetchall()  # 返回所有的数据
    print(rs)
    print(rs[0][2])  # 获取数据
    db.commit()  # 提交数据库执行
except:
    db.rollback()  # 若错误则回滚

cursor.close()
# 关闭数据库连接
db.close()
