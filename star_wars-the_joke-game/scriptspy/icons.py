import pygame
from scriptspy import loading

pygame.init()


class Icon_sh(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.shotgun
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.shotgun, (40, 20))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 465
        self.rect.centerx = 233


class Icon_sh_big(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.shotgun
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.shotgun, (80, 40))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 438
        self.rect.centerx = 215


class Icon_ju(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.rifle
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.rifle, (42, 30))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 553
        self.rect.centerx = 307


class Icon_ju_big(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.rifle
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.rifle, (84, 60))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 520
        self.rect.centerx = 285
