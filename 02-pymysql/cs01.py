#!/usr/bin/env python3
# Python 操作MySQL数据库

import pymysql

# 数据库连接
db = pymysql.connect("192.168.10.88", "py", "123", "study")

# 创建一个游标对象
cursor = db.cursor()

# 执行SQL语句
cursor.execute("show tables")

# 插入数据
sql = """INSERT INTO Person (id,name,age) VALUES(1,'Jack',19)"""

try:
    cursor.execute(sql)  # 执行SQL语句
    db.commit()  # 提交数据库执行
except:
    db.rollback()  # 若错误则回滚

# 关闭数据库连接
db.close()
