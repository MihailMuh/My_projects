import pygame
import random
from scriptspy import loading, shoots, system_size

pygame.init()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, bosses2, speed_enem2, count_bosses2):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = loading.meteor
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.x = random.randrange(50, system_size.x - 70)
        self.rect.y = random.randrange(-100, -30)
        self.speed_enem2 = speed_enem2
        self.count_bosses2 = count_bosses2
        self.bosses2 = bosses2
        self.speedy = random.randrange(self.speed_enem2 // 2 + 1 + self.count_bosses2 // 3,
                                       self.speed_enem2 * 3 + self.count_bosses2 // 2)
        self.rot = 0
        self.rot_speed = random.randrange(-17, 17)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > system_size.y + 60:
            if not self.bosses2:
                self.rect.x = random.randrange(50, system_size.x - 70)
                self.rect.y = random.randrange(-100, -30)
                self.speedy = random.randrange(self.speed_enem2 // 2 + 1 + self.count_bosses2 // 3,
                                               self.speed_enem2 * 3 + self.count_bosses2 // 2)
                self.rot_speed = random.randrange(-17, 17)
            else:
                self.kill()


