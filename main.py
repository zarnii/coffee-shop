import random
import models
import pygame
import media
import sys


def main():
	pygame.init()
	#pygame.FULLSCREEN
	screen = pygame.display.set_mode((1280,720))
	pygame.display.set_caption('test game')
	bg = pygame.image.load('images/bg.png').convert()


	#Build: screen
	#build = models.Build(screen)
	coffeemenu = {
	'кофе' : 250,
	'чай' : 150,
	'молочный коктель': 200
	}
	#Coffee: level, budget, upgradeprice, menu, employeecount
	coffee = models.Coffee(screen, 0, 5000, 3000, coffeemenu, 0)
	#Employee: screen, name, age, salary, count

	w = models.Employee(screen,random.choice(media.mennamelist), random.randint(16,65), random.randint(100, 400), 0)

	#Button: x, y, image, scale
	enter_img = pygame.image.load('images/enter_btn.png').convert_alpha()
	enter_button = models.Button(10, 530, enter_img, 0.5)

	exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()
	exit_button = models.Button(1145, 10, exit_img, 0.5)

	table_img = pygame.image.load('images/table_btn.png').convert_alpha()
	table_button = models.Button(1145, 110, table_img, 0.44)

	letin_img = pygame.image.load('images/letin_btn.png').convert_alpha()
	letin_button = models.Button(1145, 210, letin_img, 0.44)

	hire_img = pygame.image.load('images/hire_btn.png').convert_alpha()
	hire_button = models.Button(1145, 310, hire_img, 0.44)

	#ContextMenu: screen, width, height, x, y, color, alpha
	bottomcontextmenu = models.ContextMenu(screen, 1280, 500, 0, 520, (16,16,16), 250)
	leftcontextmenu = models.ContextMenu(screen, 150, 720, 1130, 0, (16,16,16), 250)

	'''font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
	text = font1.render(f'Уровень {coffee.level}', True, (255,255,255))
	alertmenu = models.AlertMenu(screen, 500, 100, 500, 50, (16,16,16), 250, text)'''


	def infomenu():
		font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
		level = font1.render(f'Уровень {coffee.level}', True, (255,255,255))
		budget = font1.render(f'Бюджет {coffee.budget}', True, (255,255,255))
		upgradeprice = font1.render(f'Цена улучшения {coffee.upgradeprice}', True, (255,255,255))
		menu = font1.render(f'Меню', True, (255,255,255))

		menu_coffe = font1.render(f'Кофе { coffeemenu.get("кофе") }', True, (255,255,255))
		menu_tea = font1.render(f'Чай {coffeemenu.get("чай")}', True, (255,255,255))
		menu_milk = font1.render(f'Молочный коктель {coffeemenu.get("молочный коктель")}', True, (255,255,255))

		screen.blit(level, (10, 20))
		screen.blit(budget, (10, 50))
		screen.blit(upgradeprice, (10, 80))

		screen.blit(menu, (10, 130))
		screen.blit(menu_coffe, (10, 160))
		screen.blit(menu_tea, (10, 190))
		screen.blit(menu_milk, (10, 220))		

	def in_main_menu():
		screen.blit(bg, [0,0])
		coffee.draw_outside(screen)
		bottomcontextmenu.draw()
		enter_button.draw(screen)
		return True

	def in_coffee():
		coffee.draw_insaide(screen)
		leftcontextmenu.draw()
		exit_button.draw(screen)
		table_button.draw(screen)
		letin_button.draw(screen)
		hire_button.draw(screen)
		w.draw(screen)

		infomenu()
		#alertmenu.draw()
		return False

	def order():
		#Visitor: name, age, money
		if coffee.level != 0 and w.count != 0:
			v = models.Visitor(random.choice(media.mennamelist), random.randint(16,65), random.randint(100, 400))
			makeorder = v.make_order(coffeemenu, coffee.budget)
			coffee.budget = makeorder[0]

			font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
			text = font1.render(makeorder[1], True, (255,255,255))

			in_coffee()
			screen.blit(text, (320, 180))
		elif coffee.level == 0:
			font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
			text = font1.render('Вы не можете впустить посетителей, потому что у вас нет столов!', True, (255,255,255))
			alertmenu = models.AlertMenu(screen, 890, 100, 170, 720//2, (16,16,16), 250, text)
			alertmenu.draw()
		elif w.count == 0:
			font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
			text = font1.render('Вы не можете впустить посетителей, потому что у вас нет работников!', True, (255,255,255))
			alertmenu = models.AlertMenu(screen, 935, 100, 170, 720//2, (16,16,16), 250, text)
			alertmenu.draw()

	def hire_employee():
		#Employee: screen, name, age, salary, count

		font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
		if w.count == 1:
			text = font1.render(f'У вас уже есть работник!', True, (255,255,255))
		else:
			text = font1.render(f'Вы наняли работника {w.name}', True, (255,255,255))
		w.count += 1

		in_coffee()
		screen.blit(text, (320, 180))


	startwindow = True

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if startwindow == True:
			in_main_menu()
			

		if enter_button.press():
			startwindow = in_coffee()
			

		if exit_button.press():
			startwindow = in_main_menu()

		if table_button.press():
			if coffee.level == 4:
				in_coffee()
				font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
				text = font1.render(f'Максимальный уровень заведения!', True, (255,255,255))
				screen.blit(text, (320, 180))
			elif coffee.level < 4 and coffee.upgrade() == True:
				coffee.level += 1
				in_coffee()
			elif coffee.upgrade() == False:
				in_coffee()
				font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
				text = font1.render(f'Недостаточно денег для улучшения!', True, (255,255,255))
				screen.blit(text, (320, 180))				


		if letin_button.press():
			order()

		if hire_button.press():
			hire_employee()
				
		

		#pygame.display.flip()
		pygame.display.update()

		

if __name__ == '__main__':
	main()