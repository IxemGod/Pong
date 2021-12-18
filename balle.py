import pygame
import random


class Balle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("asset/balle.png")
        self.rect =self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 2
        self.ordonne = 1
        self.Dernier_touch=True
        self.pas = 0
        self.running = True

    def forward(self):
        self.pas += 1
        if self.pas == 5:
            self.pas = 0
            if self.Dernier_touch:
                self.rect.x+=1
            else:
                self.rect.x-=1

            if self.rect.x >= 780:
                self.running = False
            if self.rect.x <= 0:
                self.running = False

            if self.rect.y <= 0:
                self.ordonne = random.randint(1,2)
            elif self.rect.y >= 580:
                self.ordonne = random.randint(1,2)
                self.ordonne = self.ordonne*(-1)

            self.rect = self.image.get_rect(center = self.rect.center)
            self.rect.y+=self.ordonne

