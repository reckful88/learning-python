#encoding: utf-8
'''
先计算的是1-120的阶乘，
然后数末尾有多少个0，
方法是先反转字符串，
从头开始数，等于0就加1，
当不是0的时候就跳出循环
'''


sums = 1
for x in range(1,121):
	sums = sums * x
print sums
z = str(sums)[::-1]
cnt = 0
for i in z:
	if i == '0':
		cnt = cnt + 1
	else:
		break
print cnt
