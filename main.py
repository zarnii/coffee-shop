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
	build = models.Build(screen)
	coffee = models.Coffee(screen)

	#Button: x, y, image, scale
	start_img = pygame.image.load('images/start_btn.png').convert_alpha()
	start_button = models.Button(10, 530, start_img, 0.5)

	exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()
	exit_button = models.Button(1145, 10, exit_img, 0.5)

	#ContextMenu: screen, width, height, x, y, color, alpha
	firstcontextmenu = models.ContextMenu(screen, 1280, 500, 0, 520, (16,16,16), 250)
	secondcontextmenu = models.ContextMenu(screen, 150, 720, 1130, 0, (16,16,16), 250)
	startwindow = True


	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if startwindow == True:
			screen.blit(bg, [0,0])
			build.draw()
			firstcontextmenu.draw()
			start_button.draw(screen)

		if start_button.press():
			startwindow = False
			coffee.draw()
			secondcontextmenu.draw()
			exit_button.draw(screen)

		if exit_button.press():
			startwindow = False
			screen.blit(bg, [0,0])
			build.draw()
			firstcontextmenu.draw()
			start_button.draw(screen)
			
		
		
		pygame.display.flip()

		#pygame.display.update()

		

if __name__ == '__main__':
	main()