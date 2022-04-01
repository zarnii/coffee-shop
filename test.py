class Person:
	def __init__(self, age):
		self.age = age

class Worker(Person):
	def __init__(self, age, salary):
		Person.__init__(self, age)
		self.salary = salary

a = Worker(45, 45000)
print(a.age, a.salary)