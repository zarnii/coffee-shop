import pygame

class Build():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/build.png')
		self.rect = self.image.get_rect(center = (1280//2,720//2))
		self.screen_rect = screen.get_rect()

	def draw(self):
		'''рисование постройки'''
		self.screen.blit(self.image, self.rect)


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
	

class ContextMenu():
	def __init__(self, screen, width, height, x, y, color, alpha):
		self.screen = screen
		self.width = width
		self.height = height
		self.color = color
		self.x = x 
		self.y = y 
		self.alpha = alpha

		self.contexmenu = pygame.Surface((self.width, self.height))
		self.contexmenu.fill(color)
		self.contexmenu.set_alpha(alpha)

	def draw(self):
		self.screen.blit(self.contexmenu, (self.x, self.y))

class Coffee():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/coffee.png')
		self.rect = self.image.get_rect(center = (1280//2,720//2))
		self.screen_rect = screen.get_rect()

	def draw(self):
		'''рисование постройки'''
		self.screen.blit(self.image, self.rect)
		