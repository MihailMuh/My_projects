import pygame
import os

pygame.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')
inventar = pygame.image.load(os.path.join(img_folder, 'invent.jpg'))


class Inventar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = inventar
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(inventar, (40, 180))
        self.rect.bottom = 350
        self.rect.centerx = 25