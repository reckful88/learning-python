#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng


'''
在python3中, socket编程和网络传输的时候,必须是 bytes(二进制),不能用字符串

decode() 可以把 bytes 转成 str
encode() 可以把 str 转成 bytes
'''

msg = '我爱北京'
print(msg)
print(msg.encode()) # b开头的就是二进制, str to bytes
msg = (b'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac'.decode('utf-8')) # bytes to str
print(msg)