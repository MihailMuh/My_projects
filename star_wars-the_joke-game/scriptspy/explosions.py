import pygame
from scriptspy import loading

pygame.init()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size, type=1):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.type = type
        if self.type == 1:
            self.image = loading.explosion_anim[self.size][0]
        elif self.type == 2:
            self.image = loading.explosion_anim2[self.size][0]
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
                if self.frame == len(loading.explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = loading.explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
            elif self.type == 2:
                if self.frame == len(loading.explosion_anim2[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = loading.explosion_anim2[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
