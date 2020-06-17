import pygame
import os

pygame.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')
img_bullet = pygame.image.load(os.path.join(img_folder, 'bullet.png'))


class Drob(pygame.sprite.Sprite):
    def __init__(self, shape, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 5
        self.image = img_bullet
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet, (20, 40))
        self.rect.bottom = y
        self.rect.centerx = x
        self.shape = shape
        self.speedy = -17
        if self.shape == 'drob2':
            self.speedx = -11
            self.image = pygame.transform.rotate(self.image, 30)
        elif self.shape == 'drob3':
            self.speedx = 11
            self.image = pygame.transform.rotate(self.image, -30)
        elif self.shape == 'drob4':
            self.speedx = -5
            self.image = pygame.transform.rotate(self.image, 15)
        elif self.shape == 'drob5':
            self.speedx = 5
            self.image = pygame.transform.rotate(self.image, -15)
        elif self.shape == 'drob':
            self.speedx = 0

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 10
        self.image = img_bullet
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet, (15, 40))
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -35

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Drob_boss(pygame.sprite.Sprite):
    def __init__(self, shape, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_bullet
        self.radius = 5
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet, (20, 40))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -12
        self.shape = shape
        if self.shape == 'drob2':
            self.speedx = -8
            self.image = pygame.transform.rotate(self.image, 30)
        elif self.shape == 'drob3':
            self.speedx = 8
            self.image = pygame.transform.rotate(self.image, -30)
        elif self.shape == 'drob':
            self.speedx = 0

    def update(self):
        self.rect.y -= self.speedy
        self.rect.x -= self.speedx
        if self.rect.bottom < 0:
            self.kill()