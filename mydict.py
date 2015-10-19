class Dict(dict):

	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self,key,value):
		self[key] = value

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], 'value')


if __name__ == '__main__':
	unittest.main()
