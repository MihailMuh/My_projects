import pygame
import random
from scriptspy import loading, shoots, system_size

pygame.init()


class Imperia(pygame.sprite.Sprite):
    def __init__(self, jelly2, putin2, virus2, vaders2, death2, sprites2, bosses2, speed_enem2, count_bosses2):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 25
        self.jelly2 = jelly2
        self.putin2 = putin2
        self.virus2 = virus2
        self.vaders2 = vaders2
        self.death2 = death2
        self.sprites2 = sprites2
        self.bosses2 = bosses2
        self.speed_enem2 = speed_enem2
        self.count_bosses2 = count_bosses2
        if self.jelly2:
            self.image_orig = loading.img_vader4
            self.image = loading.img_vader4
            self.image = pygame.transform.scale(loading.img_vader4, (75, 60))
        elif self.putin2:
            self.image_orig = loading.img_putin
            self.image = loading.img_putin
            self.image = pygame.transform.scale(loading.img_putin, (68, 75))
            self.image.set_colorkey((0, 0, 0))
        elif self.virus2:
            self.image_orig = loading.img_virus
            self.image_orig = pygame.transform.scale(loading.img_virus, (65, 90))
            self.image = self.image_orig.copy()
        elif self.vaders2:
            self.image_orig = random.choice(loading.vader_images)
            self.image = random.choice(loading.vader_images)
        elif self.death2:
            self.image_orig = loading.img_death
            self.image = loading.img_death
            self.image = pygame.transform.scale(loading.img_death, (68, 88))
            self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        if self.sprites2:
            pygame.draw.circle(self.image, (0, 0, 100), self.rect.center, self.radius)
        self.rect.x = random.randrange(50, system_size.x - 70)
        self.rect.y = random.randrange(-100, -30)
        self.speedy_imp = random.randrange(self.speed_enem2+self.count_bosses2//3,
                                           self.speed_enem2 * 3+self.count_bosses2//2)
        self.speedx_imp = random.randrange(-self.speed_enem2 * 2-self.count_bosses2//3,
                                           self.speed_enem2+self.count_bosses2//3)
        self.rot_speed = random.randrange(-20, 20)
        self.last_update = pygame.time.get_ticks()
        self.rot = 0

    def rotate(self):
        if self.virus2:
            now = pygame.time.get_ticks()
            if now - self.last_update > 50:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center
        else:
            pass

    def update(self):
        if self.virus2:
            self.rotate()
        self.rect.y += self.speedy_imp
        self.rect.x += self.speedx_imp
        if (self.rect.top > system_size.y + 70) or (self.rect.left > system_size.x + 50) or (self.rect.right < 0):
            if not self.bosses2:
                self.rect.x = random.randrange(50, system_size.x - 70)
                self.rect.y = random.randrange(-100, -30)
                self.speedy_imp = random.randrange(self.speed_enem2 + self.count_bosses2 // 3,
                                                   self.speed_enem2 * 3 + self.count_bosses2 // 2)
                self.speedx_imp = random.randrange(-self.speed_enem2 * 2 - self.count_bosses2 // 3,
                                                   self.speed_enem2 + self.count_bosses2 // 3)
                self.rot_speed = random.randrange(-20, 20)
            else:
                self.kill()

