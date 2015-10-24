#encoding: utf-8
#导入socket库：
import socket
#创建一个socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立链接：
s.connect(('www.baidu.com', 80))
#发送数据：
print s.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#接收数据：
buffer = []
while True:
	#每次最多接收1k字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
print data
#关闭链接：
s.close()
#把接收的数据写入文件：
with open('baidu.html', 'wb') as f:
	f.write(html)
#现在只需要在浏览器中打开这个baidu.html文件，就可以看到baidu的首页了。
