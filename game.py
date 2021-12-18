import pygame
from player import Player
from player_bot import Player_Bot
from balle import Balle
class Game():
	def __init__(self):
		self.running = True
		self.screen = pygame.display.set_mode((800,600))
		pygame.display.set_caption("IxemPong")
		self.player = Player()
		self.bot = Player_Bot()
		self.balle = Balle()
		self.gn_background = pygame.image.load('asset/background2.jpg')
		self.background = pygame.transform.scale(self.gn_background, (800, 600))
		self.pressed = {}
	def run(self):
		while self.running:
			if self.balle.running==False:
				self.running= False
			#Charger le background
			self.screen.blit(self.background, (0,0))
			#Charger le joueur
			self.player.image = pygame.transform.scale(self.player.image, (5, 50))
			self.screen.blit(self.player.image, self.player.rect)
			#Charger le bot
			self.bot.image = pygame.transform.scale(self.bot.image, (5, 50))
			self.screen.blit(self.bot.image, (self.bot.rect.x, self.bot.rect.y))
			#Charger la balle
			self.balle.image = pygame.transform.scale(self.balle.image, (20, 20))
			self.screen.blit(self.balle.image, self.balle.rect)
			if self.pressed.get(pygame.K_DOWN):
				self.player.move_down()
			elif self.pressed.get(pygame.K_UP):
				self.player.move_up()
			if self.player.pas == 3:
				self.player.pas = 0
			#Ici on test si  la balle touche la raquette du bot.
			if self.balle.rect.x >= 775 and (self.balle.rect.y >= self.bot.rect.y - 18 and self.balle.rect.y <= self.bot.rect.y + 40): #and (self.balle.rect.y >= self.bot.rect.y and self.balle.rect.y <= self.bot.rect.y + 15)
				self.balle.Dernier_touch = False
			#Ici on test si  la balle touche la raquette du joueur.
			if self.balle.rect.x <= 15 and (self.balle.rect.y >= self.player.rect.y - 18 and self.balle.rect.y <= self.player.rect.y + 40): #and (self.balle.rect.y >= self.bot.rect.y and self.balle.rect.y <= self.bot.rect.y + 15)
				self.balle.Dernier_touch = True
			self.balle.forward()
			cordonneBalle = self.balle.rect
			if self.balle.Dernier_touch and cordonneBalle[0] >= 400:
				self.bot.move_from_balle(cordonneBalle[1])
			#Mettre à jours l'écrant
			pygame.display.flip()
			#Réduit la vitesse de déplacement
			self.player.pas+=1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				#Si une touche est appuyer	
				if event.type == pygame.KEYDOWN:
					self.pressed[event.key] = True
				if event.type == pygame.KEYUP:
					self.pressed[event.key] = False
		pygame.quit()