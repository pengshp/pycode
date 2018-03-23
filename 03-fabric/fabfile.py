#!/bin/env python3
#Fabric自动化运维
#fabfile.py

from fabric.api import *
from fabric.tasks import Task
#设置环境变量
env.hosts=['']
env.user='root'

#判断路径是否存在
def exits(path):
	with settings(warn_only=True):
		return local('test -e %s' %path)

@task(name='ip')
def ip_address():
	"""
	显示本机网络
	"""
	local('ifconfig')

class Who(Task):
	"""显示主机名"""
	name='who'
	def run(self):
		local('whoami')

instance=Who() #实例化
		