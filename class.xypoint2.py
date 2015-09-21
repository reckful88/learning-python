class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def distance(self, other_point):
		dis = (self.x – other.x)**2 + (self.y – other.y) ** 2
		return genhao(dis)


a = Point(3,4)
b = Point(4,5)
dis = a.distance(b)
