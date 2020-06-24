import pygame
from pygame.math import Vector2
import math
from scriptspy import loading, system_size
pygame.init()


class Drob(pygame.sprite.Sprite):
    def __init__(self, shape, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 5
        self.image = loading.img_bullet
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.img_bullet, (20, 40))
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
        pygame.sprite.Sprite.__init__(self)
        self.radius = 10
        self.image = loading.img_bullet
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.img_bullet, (15, 40))
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
        self.image = loading.img_bullet
        self.radius = 5
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(loading.img_bullet, (20, 40))
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
        elif self.shape == 'drob4':
            self.speedx = -12
            self.image = pygame.transform.rotate(self.image, 45)
        elif self.shape == 'drob5':
            self.speedx = 12
            self.image = pygame.transform.rotate(self.image, -45)
        elif self.shape == 'drob6':
            self.speedx = -16
            self.image = pygame.transform.rotate(self.image, 60)
        elif self.shape == 'drob7':
            self.speedx = 16
            self.image = pygame.transform.rotate(self.image, -60)
        elif self.shape == 'drob8':
            self.speedx = -4
            self.image = pygame.transform.rotate(self.image, 15)
        elif self.shape == 'drob9':
            self.speedx = 4
            self.image = pygame.transform.rotate(self.image, -15)
        elif self.shape == 'drob':
            self.speedx = 0

    def update(self):
        self.rect.y -= self.speedy
        self.rect.x -= self.speedx
        if self.rect.bottom < 0:
            self.kill()


class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self, shape, pos, angle):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.shape = shape
        self.image = loading.img_bullet_enemy
        self.image = pygame.transform.scale(self.image, (17, 50))
        if self.shape == 'drob2':
            self.angle = angle - 30
        elif self.shape == 'drob3':
            self.angle = angle + 30
        elif self.shape == 'drob':
            self.angle = angle
        self.image = pygame.transform.rotate(self.image, int(-self.angle+90))
        self.rect = self.image.get_rect(center=pos)
        offset = Vector2(10, 0).rotate(self.angle)
        self.pos = Vector2(self.pos) + offset
        self.velocity = Vector2(1, 0).rotate(self.angle) * 9

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos
        if (self.pos[0] < -400) or (self.pos[0] > system_size.x + 400) or (self.pos[1] > system_size.y + 400):
            self.kill()
