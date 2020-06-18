import pygame
import os
import random
from scriptspy import system_size

pygame.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')
health = pygame.image.load(os.path.join(img_folder, 'health.png'))
fly_sh = pygame.image.load(os.path.join(img_folder, 'buckshot.png'))


class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = health
        self.image = pygame.transform.scale(health, (50, 50))
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.x = random.randrange(100, system_size.x - 170)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > system_size.y + 60:
            self.kill()


class Fly_sh(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 30
        self.image = fly_sh
        self.image = pygame.transform.scale(fly_sh, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, system_size.x - 170)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > system_size.y + 60:
            self.kill()