#!/usr/bin/env python3
# 搭建LAMP环境
# 

from fabric.colors import *
from fabric.api import *

env.user='root'
env.hosts=['192.168.22.154']

@task
def webtask():
	"安装Apache，PHP"
	print (red("Install Apache php ...."))
	with settings(warn_only=True):
		run("yum install -y httpd")
		run("yum install -y php php-mysql php-gd php-xml php-mcrypt")
		#run("chkconfig php-fpm on")
		run("chkconfig httpd on")

@task
def dbtask():
	"安装MySQL"
	print(red("Install mysql ..."))
	with settings(warn_only=True):
		run("yum install -y mysql mysql-server")
		run("chkconfig mysqld on")

@task
def reboot():
	"重启系统"
	run("reboot")

@task
def lnmp():
	"安装LAMP"
	execute(webtask)
	execute(dbtask)
	execute(reboot)