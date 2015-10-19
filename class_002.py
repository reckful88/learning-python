#######定义一个班级的类，最下面的那个班级，是把学生和老师都加进去了，但别忘记定义学生和老师的姓名#######

class teacher(object):
	def __init__(self,name):
		self.__name = name
	def run(self):
		print 'hello,world'
class student(object):
	def __init__(self,name):
		self.__name = name
class classes(object):
	def __init__(self, student, teacher):
		self.__teacher = teacher
		self.__student = student
	

