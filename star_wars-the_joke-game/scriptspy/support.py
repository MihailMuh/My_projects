import pygame
import os
import random
from tkinter import *

pygame.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')
health = pygame.image.load(os.path.join(img_folder, 'health.png'))
fly_sh = pygame.image.load(os.path.join(img_folder, 'buckshot.png'))

x, y = 1920, 1080


def windows():
    global x, y
    window = Tk()
    x = window.winfo_screenwidth()
    y = window.winfo_screenheight()
    window.destroy()


windows()


class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = health
        self.image = pygame.transform.scale(health, (50, 50))
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.x = random.randrange(100, x - 170)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > y + 60:
            self.kill()


class Fly_sh(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 30
        self.image = fly_sh
        self.image = pygame.transform.scale(fly_sh, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, x - 170)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > y + 60:
            self.kill()