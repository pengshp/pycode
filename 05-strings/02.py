#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# find 返回找到字符串的第一个索引值
aStr = "hello python and itchastpython"
n1 = aStr.find("python")
print(n1)

# rfind 从右向左找

# index 找不到返回异常

name = "python and itchatpython"
# count 计数
# count("py",3,23)

# replace替换replace("old","new",num)num--替换次数
print(name.replace("py", "PY"))

# split分隔,返回列表，默认空格作为分隔符
print(name.split())
