import pygame
from scriptspy import loading

pygame.init()


class Buttonpy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, monitor, text, function=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.button_notpress
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.scale(loading.button_notpress, (width, height))
        self.height = height
        self.width = width
        self.monitor = monitor
        self.function = function
        self.text = text

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.rect.x < mouse[0] < self.rect.x + self.width) and (self.rect.y < mouse[1] < self.rect.y + self.height):
            self.image = loading.button_press
            self.image = pygame.transform.scale(loading.button_press, (self.width, self.height))
            if click[0] == 1:
                loading.spacebar_snd.play()
                pygame.time.delay(200)
                if self.function is not None:
                    self.function()
        else:
            self.image = loading.button_notpress
            self.image = pygame.transform.scale(loading.button_notpress, (self.width, self.height))

    def change(self, x=None, y=None, width=None, height=None, text=None, function=None):
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.width = width
        self.text = text
        self.function = function
