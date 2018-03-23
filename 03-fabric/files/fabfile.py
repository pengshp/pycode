#!/usr/bin/env python3
#Fabric文件操作
#

from fabric.api import *
from fabtools import require

env.hosts=['192.168.22.154']
env.user='root'

@task(name='files')
def remote_files():
	dirs=[
		'static',
		'templates'
	]
	require.files.directory(dirs) #新建多个目录
	require.directory('myapp') #新建一个目录
	
	with cd('myapp'):
		put('app.py','myapp/app.py') #上传文件
		require.file('application.cfg',contents='TESTING=True')
		tmp=require.files.temporary_directory()
		local('tar -zcf myapp.tar.gz myapp')
		tmp_file=path.join(tmp,'myapp.tar.gz')
		put(tmp_file)
		run('tar -zxf %s' %tmp_file)
		run('rm -rf myapp.tar.gz')