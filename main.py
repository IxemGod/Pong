import pygame
from game import Game
import os
import time
def aceuil():
	os.system("clear")
	print("Le jeux va démarer dans 3...")
	time.sleep(1)
	os.system("clear")
	print("Le jeux va démarer dans 2...")
	time.sleep(1)
	os.system("clear")
	print("Le jeux va démarer dans 1...")
	time.sleep(1)
if __name__ == '__main__':
	aceuil()
	pygame.init()
	myGame = Game()
	myGame.run()