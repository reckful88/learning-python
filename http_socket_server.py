#encoding: utf-8
'''
用socket与服务器交互通信
客户端输入：
nc 127.0.0.1 8686
'''


import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #此条可以让地址重用
#监听端口：
s.bind(('127.0.0.1', 8686))
s.listen(5)		#最多可以监听5个
print 'Waiting for connection...'
#接收一个新连接：
sock, addr = s.accept()
sock.send('Welcome! \n')
while True:
	data = sock.recv(1024)     #recv1024字节，就是空间
	time.sleep(1)		#sleep设置的是反应回话速度
	if data.strip() == 'exit':
		close = True
		break
	sock.send('Hello, %s! \n' % data.strip())   #strip默认去掉换行符和空格之类的。。
if close:
	sock.close()
	print 'Connection from %s:%s closed.' % addr


