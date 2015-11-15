class Aanimal(object):
	def run(self):
		print 'Animal is running...'
a=Aanimal()
a.run()
class Dog(Aanimal):
	def run(self):
		print 'HEY im a dog'

class Cat(Aanimal):
	pass

dog = Dog()
dog.run()

cat = Cat()
cat.run

print type(a)

print isinstance(dog,Aanimal)
print isinstance(dog,Dog)
print isinstance(cat,Dog)

def run_twice(Animal):
	Animal.run()
	Animal.run()
print run_twice(a)

