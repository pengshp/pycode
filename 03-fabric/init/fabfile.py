#!/usr/bin/env python3

from fabric.api import *

env.hosts=['192.168.22.154','192.168.22.153','192.168.22.155','192.168.22.156']
env.user='root'

@task
def init_build():
	'''安装编译环境'''
	#build='gcc gcc-c++ make'
	run('yum install -y gcc gcc-c++ make')

@task
def zshconfig():
	'''配置zsh'''
	put('zshconfig.tar.gz')
	run('tar -xf zshconfig.tar.gz')
	run('rm zshconfig.tar.gz')

@task
def reboot():
	'''重启服务器'''
	run('reboot')

@task
def passwd():
	"修改root密码"
	run('echo "123456" |passwd --stdin root')

@task
def configvim():
	"配置vim"
	run('echo "set tabstop=4" >> /ect/vim/vimrc')
	run('echo "set softtabstop=4" >> /ect/vim/vimrc')
	run('echo "set shiftwidthk=4" >> /ect/vim/vimrc')



