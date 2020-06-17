import pygame
import os

pygame.init()

folder = os.path.dirname(__file__)
img_folder = os.path.join(folder, 'images')

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['hu'] = []
for i in range(8):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img_hu = pygame.transform.scale(img, (300, 280))
    explosion_anim['hu'].append(img_hu)
    img_lg = pygame.transform.scale(img, (145, 125))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (50, 50))
    explosion_anim['sm'].append(img_sm)

explosion_anim2 = {}
explosion_anim2['lg'] = []
explosion_anim2['sm'] = []
explosion_anim2['hu'] = []
for i in range(12):
    filename2 = 'Explosion0{}.png'.format(i)
    img2 = pygame.image.load(os.path.join(img_folder, filename2))
    img_hu2 = pygame.transform.scale(img2, (300, 280))
    explosion_anim2['hu'].append(img_hu2)
    img_lg2 = pygame.transform.scale(img2, (145, 125))
    explosion_anim2['lg'].append(img_lg2)
    img_sm2 = pygame.transform.scale(img2, (70, 55))
    explosion_anim2['sm'].append(img_sm2)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size, type=1):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.type = type
        if self.type == 1:
            self.image = explosion_anim[self.size][0]
        elif self.type == 2:
            self.image = explosion_anim2[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.type == 1:
                if self.frame == len(explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
            elif self.type == 2:
                if self.frame == len(explosion_anim2[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim2[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
