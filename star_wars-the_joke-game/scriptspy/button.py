import pygame
import os

pygame.init()
pygame.mixer.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')
snd_folder = os.path.join(folder, 'sounds')

button_press = pygame.image.load(os.path.join(img_folder, 'button_press.png'))
button_notpress = pygame.image.load(os.path.join(img_folder, 'button_notpress.png'))
spacebar_snd = pygame.mixer.Sound(os.path.join(snd_folder, 'spacebar.wav'))
spacebar_snd.set_volume(0.30)


class Buttonpy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, monitor, text, function=None, image=button_notpress, image2=button_press):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.scale(image, (width, height))
        self.height = height
        self.width = width
        self.monitor = monitor
        self.function = function
        self.text = text
        self.image2 = image2
        self.image_orig = image

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.rect.x < mouse[0] < self.rect.x + self.width) and (self.rect.y < mouse[1] < self.rect.y + self.height):
            self.image = self.image2
            self.image = pygame.transform.scale(self.image2, (self.width, self.height))
            if click[0] == 1:
                pygame.time.delay(200)
                spacebar_snd.play()
                pygame.time.delay(200)
                if self.function is not None:
                    self.function()
        else:
            self.image = self.image_orig
            self.image = pygame.transform.scale(self.image_orig, (self.width, self.height))

    def change(self, x=None, y=None, width=None, heigth=None, text=None, function=None):
        self.rect.x = x
        self.rect.y = y
        self.height = heigth
        self.width = width
        self.text = text
        self.function = function

