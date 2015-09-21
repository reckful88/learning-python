#encoding: utf-8
class reverse(object):
	def __init__(self, a_str):
		self.xstr = a_str
		self.len = len(a_str)
	def __iter__(self):
		return self
	def next(self):
		if self.len == 0:
			raise stopiteration()
		self.len = self.len -1
		return self.xstr[self.len]


for i in reverse('abc'):
	print i
