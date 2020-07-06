import pygame
from scriptspy import loading

pygame.init()


class Inventar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.inventar
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.inventar, (40, 180))
        self.rect.bottom = 350
        self.rect.centerx = 25