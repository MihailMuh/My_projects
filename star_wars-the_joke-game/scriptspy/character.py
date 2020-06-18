import pygame
import random
from scriptspy import shoots, loading, system_size

pygame.init()


class Npc(pygame.sprite.Sprite):
    def __init__(self, group, bul):
        pygame.sprite.Sprite.__init__(self)
        self.image = loading.img_npc
        self.image = pygame.transform.scale(loading.img_npc, (130, 150))
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.centerx = system_size.x // 2
        self.rect.bottom = system_size.y // 2 + system_size.y // 3
        self.shoot_time = 120
        self.last_shot = pygame.time.get_ticks()
        self.shotgun_time = 2150
        self.last_shotgun = pygame.time.get_ticks()
        self.speedx = 15
        self.speedy = 3
        self.group = group
        self.bul = bul

        self.right = random.randint(0, 1)
        if self.right == 1:
            self.left = 0
        else:
            self.left = 1
        self.top = random.randint(0, 1)
        if self.top == 1:
            self.down = 0
        else:
            self.down = 1

    def update(self):
        self.shoot()
        if self.rect.x >= system_size.x - 140:
            self.right = 1
            self.left = 0
        if self.rect.x <= 10:
            self.right = 0
            self.left = 1
        if self.rect.y > system_size.y - 210:
            self.top = 0
            self.down = 1
        if self.rect.y < 0:
            self.top = 1
            self.down = 0

        if self.right == 1:
            self.rect.x -= self.speedx
        elif self.left == 1:
            self.rect.x += self.speedx
        if self.top == 1:
            self.rect.y += self.speedy
        elif self.down == 1:
            self.rect.y -= self.speedy

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            bullet = shoots.Bullet(self.rect.centerx + 12, self.rect.bottom - 87)
            bullet2 = shoots.Bullet(self.rect.centerx + 23, self.rect.bottom - 87)
            self.group.add(bullet)
            self.bul.add(bullet)
            self.group.add(bullet2)
            self.bul.add(bullet2)
            loading.laser_sound.play()
