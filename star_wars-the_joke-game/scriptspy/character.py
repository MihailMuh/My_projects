import pygame
import random
import math
from scriptspy import shoots, loading, system_size

pygame.init()


class Npc(pygame.sprite.Sprite):
    def __init__(self, group, bul, sprites2):
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
        self.sprites2 = sprites2
        if self.sprites2:
            pygame.draw.circle(self.image, (0, 0, 100), self.rect.center, self.radius)

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


class Gunner(pygame.sprite.Sprite):
    def __init__(self, all_sprites2, bullets2):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 50
        self.all_sprites2 = all_sprites2
        self.bullets2 = bullets2

        self.original_image = loading.img_gunner
        self.original_image = pygame.transform.scale(loading.img_gunner, (130, 180))
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.rect.centerx = system_size.x // 2
        self.rect.bottom = system_size.y // 2 + system_size.y // 3
        self.position = pygame.math.Vector2(self.rect.centerx, self.rect.bottom)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.bottom))
        self.speedx = 0
        self.speedy = 0
        self.angle = 0
        self.shoot_time = 85
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.rotate()
            self.last_shot = now
            for i in range(random.randint(1, 4)):
                bullet = shoots.Bull((self.position.x, self.position.y), self.angle)
                self.all_sprites2.add(bullet)
                self.bullets2.add(bullet)
            loading.laser_sound.play()

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        self.angle = -((180 / math.pi) * -math.atan2(rel_y, rel_x))

    def update(self):
        mouse_position = pygame.math.Vector2(*pygame.mouse.get_pos())
        relative_mouse_position = mouse_position - self.position
        y_axis = pygame.math.Vector2(0, -1)
        angle = -y_axis.angle_to(relative_mouse_position)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = self.position.x, self.position.y

        key = pygame.key.get_pressed()
        pressed = pygame.mouse.get_pressed()
        if key[pygame.K_d]:
            self.position.x += 10
        if key[pygame.K_a]:
            self.position.x -= 10
        if key[pygame.K_w]:
            self.position.y -= 10
        if key[pygame.K_s]:
            self.position.y += 10
        if pressed[0]:
            self.shoot()

        if self.position.x > system_size.x - 110:
            self.position.x = system_size.x - 110
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.center = self.position.x, self.position.y

        if self.position.x < 110:
            self.position.x = 110
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.center = self.position.x, self.position.y

        if self.position.y > system_size.y - 200:
            self.position.y = system_size.y - 200
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.center = self.position.x, self.position.y

        if self.position.y < 160:
            self.position.y = 160
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.center = self.position.x, self.position.y


class Player(pygame.sprite.Sprite):
    def __init__(self, sprites2, key_btn2, mouse_btn2, ju2, sh2, equip2, all_sprites2, bullets2, drobs2):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 40
        self.sprites2 = sprites2
        self.key_btn2 = key_btn2
        self.mouse_btn2 = mouse_btn2
        self.ju2 = ju2
        self.sh2 = sh2
        self.equip2 = equip2
        self.all_sprites2 = all_sprites2
        self.bullets2 = bullets2
        self.drobs2 = drobs2

        self.image = loading.img_npc
        self.image = pygame.transform.scale(loading.img_npc, (130, 150))
        self.rect = self.image.get_rect()
        if self.sprites2:
            pygame.draw.circle(self.image, (0, 0, 100), self.rect.center, self.radius)

        self.rect.centerx = system_size.x // 2
        self.rect.bottom = system_size.y // 2 + system_size.y // 3
        self.speedx = 0
        self.speedy = 0
        self.shoot_time = 120
        self.last_shot = pygame.time.get_ticks()
        self.shotgun_time = 800
        self.last_shotgun = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        if self.key_btn2 == 1 and self.mouse_btn2 == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.speedx = 30
            if key[pygame.K_a]:
                self.speedx = -30
            if key[pygame.K_w]:
                self.speedy = -30
            if key[pygame.K_s]:
                self.speedy = 30
            if self.ju2 == 1 and self.sh2 == 0:
                if key[pygame.K_SPACE]:
                    self.shoot()
            elif self.sh2 == 1 and self.equip2 == 1 and self.ju2 == 0:
                if key[pygame.K_SPACE]:
                    self.shotgun()
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        elif self.key_btn2 == 0 and self.mouse_btn2 == 1:
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()
            if self.ju2 == 1 and self.sh2 == 0:
                if pressed[0]:
                    self.shoot()
            elif self.sh2 == 1 and self.equip2 == 1 and self.ju2 == 0:
                if pressed[0]:
                    self.shotgun()
            self.rect.x = pos[0] - 62
            self.rect.y = pos[1] - 80
        if self.rect.left > system_size.x - 110:
            self.rect.right = system_size.x - 10
        if self.rect.right < 110:
            self.rect.left = 10
        if self.rect.top > system_size.y - 200:
            self.rect.top = system_size.y - 200
        if self.rect.bottom < 160:
            self.rect.bottom = 160

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            bullet = shoots.Bullet(self.rect.centerx + 12, self.rect.bottom - 87)
            bullet2 = shoots.Bullet(self.rect.centerx + 23, self.rect.bottom - 87)
            self.all_sprites2.add(bullet)
            self.bullets2.add(bullet)
            self.all_sprites2.add(bullet2)
            self.bullets2.add(bullet2)
            loading.laser_sound.play()

    def shotgun(self):
        now_sh = pygame.time.get_ticks()
        if now_sh - self.last_shotgun > self.shotgun_time:
            self.last_shotgun = now_sh
            drob = shoots.Drob('drob', self.rect.centerx + 15, self.rect.bottom - 85)
            self.all_sprites2.add(drob)
            self.drobs2.add(drob)
            drob = shoots.Drob('drob2', self.rect.centerx - 5, self.rect.bottom - 85)
            self.all_sprites2.add(drob)
            self.drobs2.add(drob)
            drob = shoots.Drob('drob3', self.rect.centerx + 20, self.rect.bottom - 85)
            self.all_sprites2.add(drob)
            self.drobs2.add(drob)
            drob = shoots.Drob('drob4', self.rect.centerx + 3, self.rect.bottom - 85)
            self.all_sprites2.add(drob)
            self.drobs2.add(drob)
            drob = shoots.Drob('drob5', self.rect.centerx + 17, self.rect.bottom - 85)
            self.all_sprites2.add(drob)
            self.drobs2.add(drob)
            loading.shotgun_sound.play(0)
