#encoding: utf-8
class fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self): #实例本身就是迭代对象，故返回自己
		return self       
	def next(self):
		self.a ,self.b = self.b, self.a + self.b
		if self.a > 100000:  #退出循环的条件
			raise stopiteration();
		return self.a  #返回下一个值
for n in fib():
	print n
