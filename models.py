import pygame
import random
import time


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age



#Размеры кнопки определяются автоматически
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
	
	def press(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action



class Menu:
	def __init__(self, screen, width, height, x, y, color, alpha):
		self.screen = screen
		self.width = width
		self.height = height
		self.color = color
		self.x = x 
		self.y = y 
		self.alpha = alpha



class ContextMenu(Menu):
	def __init__(self,screen, width, height, x, y, color, alpha):
		Menu.__init__(self, screen, width, height, x, y, color, alpha)

		self.contexmenu = pygame.Surface((self.width, self.height))
		self.contexmenu.fill(color)
		self.contexmenu.set_alpha(alpha)

	def draw(self):
		self.screen.blit(self.contexmenu, (self.x, self.y))



class AlertMenu(Menu):
	def __init__(self, screen, width, height, x, y, color, alpha, text):
		Menu.__init__(self, screen, width, height, x, y, color, alpha)
		self.text = text

		self.alertmenu = pygame.Surface((self.width, self.height))
		self.alertmenu.fill(color)
		self.alertmenu.set_alpha(alpha)
		self.alertmenu.blit(text, (0,0))


	def draw(self):
		self.screen.blit(self.alertmenu, (self.x, self.y))



class Coffee():
	def __init__(self, screen, level, budget, upgradeprice, menu, employeecount):
		self.screen = screen
		self.level = level
		self.budget = budget
		self.upgradeprice = upgradeprice
		self.menu = menu
		#self.image = pygame.image.load('images/coffee.png')
		#self.rect = self.image.get_rect(center = (1280//2,720//2))
		#self.screen_rect = screen.get_rect()

	def upgrade(self):
		if self.budget > self.upgradeprice:
			self.budget -= self.upgradeprice
			self.upgradeprice += 7000
			return True

		

	def draw_outside(self, screen):
		'''рисование постройки'''
		self.image = pygame.image.load('images/build.png')
		self.rect = self.image.get_rect(center = (1280//2,720//2))
		self.screen_rect = screen.get_rect()
		self.screen.blit(self.image, self.rect)

	def draw_insaide(self, screen):
		'''рисование постройки'''
		if self.level == 0:
			self.image = pygame.image.load('images/coffee.png')
			self.rect = self.image.get_rect(center = (1280//2,720//2))
			self.screen_rect = screen.get_rect()
			self.screen.blit(self.image, self.rect)
		elif self.level == 1:
			self.image = pygame.image.load('images/coffee_1.png')
			self.rect = self.image.get_rect(center = (1280//2,720//2))
			self.screen_rect = screen.get_rect()
			self.screen.blit(self.image, self.rect)
		elif self.level == 2:
			self.image = pygame.image.load('images/coffee_2.png')
			self.rect = self.image.get_rect(center = (1280//2,720//2))
			self.screen_rect = screen.get_rect()
			self.screen.blit(self.image, self.rect)
		elif self.level == 3:
			self.image = pygame.image.load('images/coffee_3.png')
			self.rect = self.image.get_rect(center = (1280//2,720//2))
			self.screen_rect = screen.get_rect()
			self.screen.blit(self.image, self.rect)
		elif self.level == 4:
			self.image = pygame.image.load('images/coffee_4.png')
			self.rect = self.image.get_rect(center = (1280//2,720//2))
			self.screen_rect = screen.get_rect()
			self.screen.blit(self.image, self.rect)



class Visitor(Person):
	def __init__(self, name, age, money):
		Person.__init__(self, name, age)
		self.money = money

	def make_order(self, menu, budget):
		order = random.choice(list(menu.keys()))
		price = menu.get(order)
		if self.money >= price:
			budget += price
			print(f'{budget}')
			print(f'{self.name} заказал {order} по цене {price}')
			print(f'{budget}\n')
			return budget
		else:
			print(f'Не хватило денег для {order}')
			return budget

		

class Employee(Person):
	count = 0
	def __init__(self, name, age, salary, count):
		Person.__init__(self, name, age)
		self.salary = salary
		count += 1

		