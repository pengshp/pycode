#!/usr/bin/env python3

from newspaper import Article

url='http://finance.sina.com.cn/stock/usstock/c/2017-12-29/doc-ifypyuve2261163.shtml'

article=Article(url, language='zh')

article.download()

print(article.html)
article.parse()
text=article.text.encode('utf8')
title=article.title.encode('utf8')
print(text)
print(title)
