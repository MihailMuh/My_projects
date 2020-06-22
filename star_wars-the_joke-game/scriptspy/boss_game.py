import pygame
from scriptspy import loading, shoots, system_size

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(5000)


class Boss(pygame.sprite.Sprite):
    def __init__(self, jelly2, putin2, virus2, vaders2, death2, sprites2, all_sprites2, drobs_boss2):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 150
        self.jelly2 = jelly2
        self.putin2 = putin2
        self.virus2 = virus2
        self.vaders2 = vaders2
        self.death2 = death2
        self.sprites2 = sprites2
        self.all_sprites2 = all_sprites2
        self.drobs_boss2 = drobs_boss2
        if self.jelly2:
            self.image = loading.img_vader4
            self.image = pygame.transform.scale(loading.img_vader4, (260, 200))
        elif self.putin2:
            self.radius = 160
            self.image = loading.img_putin
            self.image = pygame.transform.scale(loading.img_putin, (200, 220))
            self.image.set_colorkey((0, 0, 0))
        elif self.virus2:
            self.image = loading.img_boss_virus
            self.image = pygame.transform.scale(loading.img_boss_virus, (250, 250))
        elif self.vaders2:
            self.image = loading.boss
            self.image = pygame.transform.scale(loading.boss, (200, 200))
        elif self.death2:
            self.image = loading.img_death
            self.image = pygame.transform.scale(loading.img_death, (195, 250))
            self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        if self.sprites2:
            pygame.draw.circle(self.image, (0, 0, 100), self.rect.center, self.radius)
        self.rect.x = system_size.x // 2 - 100
        self.rect.y = -300
        self.speedy = 2
        self.speedx = 10
        self.shoot_time = 1500
        self.last_shot = pygame.time.get_ticks()

    def shotgun_boss(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            drob = shoots.Drob_boss('drob', self.rect.centerx + 35, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob2', self.rect.centerx + 35, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob3', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            loading.laser_sound.play()

    def hard(self):
        self.speedx = 12
        self.shoot_time = 600

    def update(self):
        self.shotgun_boss()
        self.rect.y += self.speedy
        if self.rect.y == 50:
            self.speedy = 0
            self.rect.x -= self.speedx
            if self.rect.right < 0:
                self.rect.left = system_size.x + 200


class Dead(pygame.sprite.Sprite):
    def __init__(self, sprites2, all_sprites2, drobs_boss2):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 150
        self.sprites2 = sprites2
        self.all_sprites2 = all_sprites2
        self.drobs_boss2 = drobs_boss2
        self.image = loading.img_dead_boss
        self.image = pygame.transform.scale(self.image, (200, 200))
        # self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        if self.sprites2:
            pygame.draw.circle(self.image, (0, 0, 100), self.rect.center, self.radius)
        self.rect.x = system_size.x // 2 - 100
        self.rect.y = -300
        self.speedy = 2
        self.speedx = 10
        self.shoot_time = 1500
        self.last_shot = pygame.time.get_ticks()

    def shotgun_boss(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            drob = shoots.Drob_boss('drob', self.rect.centerx + 25, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob2', self.rect.centerx + 15, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob3', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob4', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob5', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob6', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob7', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob8', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            drob = shoots.Drob_boss('drob9', self.rect.centerx + 22, self.rect.bottom - 70)
            self.all_sprites2.add(drob)
            self.drobs_boss2.add(drob)
            loading.laser_sound.play()

    def hard(self):
        self.speedx = 14
        self.shoot_time = 1000

    def update(self):
        self.shotgun_boss()
        self.rect.y += self.speedy
        if self.rect.y == 50:
            self.speedy = 0
            self.rect.x -= self.speedx
            if self.rect.right < 0:
                self.rect.left = system_size.x + 200
