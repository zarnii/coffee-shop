import models
import pygame
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
	'чай' : 150
	'молочный коктель': 200
	}
	coffee = models.Coffee(screen, 0, 5000, 3000, coffeemenu)

	#Button: x, y, image, scale
	start_img = pygame.image.load('images/start_btn.png').convert_alpha()
	start_button = models.Button(10, 530, start_img, 0.5)

	exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()
	exit_button = models.Button(1145, 10, exit_img, 0.5)

	table_img = pygame.image.load('images/table_btn.png').convert_alpha()
	table_button = models.Button(1145, 100, table_img, 0.44)

	#ContextMenu: screen, width, height, x, y, color, alpha
	bottomcontextmenu = models.ContextMenu(screen, 1280, 500, 0, 520, (16,16,16), 250)
	leftcontextmenu = models.ContextMenu(screen, 150, 720, 1130, 0, (16,16,16), 250)


	def infomenu():
		font1 = pygame.font.Font('font/F77 Minecraft.ttf', 20)
		level = font1.render(f'Уровень {coffee.level}', True, (255,255,255))
		budget = font1.render(f'Бюджет {coffee.budget}', True, (255,255,255))

		screen.blit(level, (10, 20))
		screen.blit(budget, (10, 50))




	startwindow = True

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if startwindow == True:
			screen.blit(bg, [0,0])
			coffee.draw_outside(screen)
			bottomcontextmenu.draw()
			start_button.draw(screen)
			

		if start_button.press():
			startwindow = False
			coffee.draw_insaide(screen)
			leftcontextmenu.draw()
			exit_button.draw(screen)
			table_button.draw(screen)
			infomenu()
			

		if exit_button.press():
			startwindow = False
			screen.blit(bg, [0,0])
			coffee.draw_outside(screen)
			bottomcontextmenu.draw()
			start_button.draw(screen)

		if table_button.press():
			if coffee.level < 4 and coffee.upgrade() == True:
				coffee.level += 1
				coffee.draw_insaide(screen)
				leftcontextmenu.draw()
				exit_button.draw(screen)
				table_button.draw(screen)
				infomenu()

			
		
		
		pygame.display.flip()

		#pygame.display.update()

		

if __name__ == '__main__':
	main()