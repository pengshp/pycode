#!/usr/bin/env python3
# 远程Nginx配置
#

from fabric.api import *
from fabtools import nginx
from fabtools import require

env.hosts=['192.168.22.156']
env.user='root'

@task(name='nginx')
def setup_nginx():
	'''远程Nginx部署'''
	require.nginx.server()
	CONFIG_TEMP='''
	server {
		listen      %(port)d;
		server_name %(server_name) %(server_alias)s;
		root        %(docroot)s;
	}
	'''
	require.nginx.site('localhost',
						template_contents=CONFIG_TEMP,
						port=80,
						server_alias='www.sks.com',
						docroot='/var/www')
	require.nginx.enable("localhost")
	require.nginx.disable("default")

	require.service.restart('nginx')
