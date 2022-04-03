import time
'''import random

menu = {
	'чай': 120,
	'кофе': 200
}

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age



class Visitor(Person):
	def __init__(self, name, age, money):
		Person.__init__(self, name, age)
		self.money = money

	def make_order(self, menu):
		order = random.choice(list(menu.keys()))
		price = menu.get(order)
		if self.money >= price:
			self.budget += price
			print(f'Был заказан {order} по цене {price}')
		else:
			print(f'Не хватило денег для {order}')

#print(random.choice(list(menu.keys())))

v = Visitor('Иван', 34, 150)
v.make_order(menu)'''


timing = time.time()
while True:
    if time.time() - timing > 10.0:
        timing = time.time()
        print("10 seconds")
        