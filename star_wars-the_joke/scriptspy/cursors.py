import pygame
from scriptspy import loading

pygame.init()


class Cursor(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        if self.img == '1':
            self.image = loading.img_aim1
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '2':
            self.image = loading.img_aim2
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '3':
            self.image = loading.img_aim3
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '4':
            self.image = loading.img_aim4
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '5':
            self.image = loading.img_aim5
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '6':
            self.image = loading.img_aim6
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '7':
            self.image = loading.img_aim7
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.img == '8':
            self.image = loading.img_aim8
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = -1000
        self.rect.bottom = -1000

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]
        self.rect.bottom = pos[1] + 20
