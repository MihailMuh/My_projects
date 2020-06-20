import pygame
from scriptspy import loading

pygame.init()


class Heart(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = img
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img, (70, 70))
        self.image.set_colorkey((255, 255, 255))
        self.rect.bottom = y
        self.rect.centerx = x

    def change(self, form, x, y):
        self.image = form
        if form == loading.non_heart:
            self.image = pygame.transform.scale(form, (70, 70))
            self.rect.bottom = y - 2
            self.rect.centerx = x
        elif form == loading.ful_heart:
            self.image = pygame.transform.scale(form, (70, 70))
            self.rect.bottom = y
            self.rect.centerx = x
        elif form == loading.half_heart:
            self.image = pygame.transform.scale(form, (70, 70))
            self.rect.bottom = y + 1
            self.rect.centerx = x
