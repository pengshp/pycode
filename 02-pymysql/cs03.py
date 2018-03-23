#!/usr/bin/env python3
# Python 操作MySQL数据库
# 增、删、改

import pymysql

# 数据库连接
db = pymysql.connect("192.168.10.88", "py", "123", "study")

# 创建一个游标对象
cursor = db.cursor()

# 执行SQL语句
cursor.execute("show tables")

# 操作数据
sql_insert = "insert into Person (id,name,age) values(4,'Kev',12)"
sql_update = "update Person set age=13 where id=2"
sql_delete = "delete from Person where id = 3"

try:
    cursor.execute(sql_insert)  # 执行SQL语句
    print(cursor.rowcount)  # 上一条语句对几行数据造成影响
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    db.commit()  # 提交数据库执行,提交事务
except Exception as e:
    print(e)
    db.rollback()  # 若错误则事务回滚

cursor.close()
# 关闭数据库连接
db.close()
