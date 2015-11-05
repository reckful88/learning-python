# -*- coding: utf-8 -*-
import os
import sys
import sqlalchemy
import re
#用户登录
class conference(object):
	def __init__(self):
		self.User = [{'Number':'1','Name':'提莫','Uid':'0001','sex':'men','phone':'18604510001','passwd':'123456'},
			   {'Number':'2','Name':'麦林','Uid':'0002','sex':'woman','phone':'18604510002','passwd':'654321'},
			   {'Number':'3','Name':'露露','Uid':'0003','sex':'woman','phone':'18604510003','passwd':'666666'}]
		self.attribute = {'Number':'编号','Name':'姓名','Uid':'身份证号','sex':'性别','phone':'手机号','passwd':'密码'}
	def run(self):
		print 'welcome to Conference management system!!!'
	logins = raw_input('请输入您的身份证号:')
	def login(self):
		for logins in self.User:
			if logins in self.User:
				has_logins == True
			if has_logins == True:
				print '登陆成功'
			else:
				print '用户不存在',exit()
#发布会议
import socket
import time
class release(conference):
	def __init__(self):
		pass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #此条可以让地址重用
#监听端口：
s.bind(('127.0.0.1', 8686))
s.listen(5)             #最多可以监听5个
print 'Waiting for connection...'
#接收一个新连接：
sock, addr = s.accept()
sock.send('Welcome! \n')
while True:
        data = sock.recv(1024)     #recv1024字节，就是空间
        time.sleep(1)           #sleep设置的是反应回话速度
        if data.strip() == 'exit':
                close = True
                break
        sock.send('Hello, %s! \n' % data.strip())   #strip默认去掉换行符和空格之类的。。
if close:
        sock.close()
        print 'Connection from %s:%s closed.' % addr

