import pygame
import os

pygame.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')

shotgun = pygame.image.load(os.path.join(img_folder, 'shotgun.png'))
rifle = pygame.image.load(os.path.join(img_folder, 'rifle.png'))


class Icon_sh(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shotgun
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(shotgun, (40, 20))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 465
        self.rect.centerx = 233


class Icon_sh_big(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shotgun
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(shotgun, (80, 40))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 438
        self.rect.centerx = 215


class Icon_ju(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = rifle
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(rifle, (42, 30))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 553
        self.rect.centerx = 307


class Icon_ju_big(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = rifle
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(rifle, (84, 60))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 520
        self.rect.centerx = 285