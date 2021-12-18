import pygame
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.img = pygame.image.load("asset/player.jpg")
		self.image = pygame.transform.scale(self.img, (5, 10))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 250
		self.pas = 0
	def move_down(self):
		if self.rect.y <= 580 and self.pas == 3:
			self.rect.y += 1
			self.pas = 0
	def move_up(self):
		if self.rect.y >= 10 and self.pas ==  3:
			self.pas = 0
			self.rect.y -= 1