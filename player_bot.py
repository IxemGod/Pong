import pygame
from balle import *

class Player_Bot(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.img = pygame.image.load("asset/player.jpg")
		self.image = pygame.transform.scale(self.img, (5, 10))
		self.rect = self.image.get_rect()
		self.rect.x = 795
		self.rect.y = 0
		self.balle = Balle()



	def move_from_balle(self,coox):
		self.rect.y = coox - 20