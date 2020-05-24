import pygame
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
import random
import os
import sys
from PIL import ImageTk, Image
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(5000)

x = 1370
y = 800

white = ((255, 255, 255))
blue = ((0, 0, 255))
green = ((0, 255, 0))
red = ((255, 0, 0))
black = ((0, 0, 0))
orange = ((255, 100, 10))
yellow = ((255, 255, 0))
blue_green = ((0, 255, 170))
marroon = ((205, 0, 0))
lime = ((180, 255, 100))
pink = ((255, 100, 180))
purple = ((240, 0, 255))
gray = ((127, 127, 127))
magenta = ((255, 0, 230))
brown = ((100, 40, 0))
forest_green = ((0, 50, 0))
navy_blue = ((0, 0, 100))
rust = ((210, 150, 75))
dandilion_yellow = ((255, 200, 0))
highlighter = ((255, 255, 100))
sky_blue = ((0, 255, 255))
light_gray = ((200, 200, 200))
dark_gray = ((30, 30, 30))
tan = ((230, 220, 170))
coffee_brown = ((200, 190, 140))
moon_glow = ((235, 245, 255))

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

img_npc = pygame.image.load(os.path.join(img_folder, 'ship.png'))
img_bullet = pygame.image.load(os.path.join(img_folder, 'bullet.png'))
img_bullet_sh = pygame.image.load(os.path.join(img_folder, 'bullet.png'))
img_vader4 = pygame.image.load(os.path.join(img_folder, 'vader4.png'))
img_putin = pygame.image.load(os.path.join(img_folder, 'putin.png'))
img_virus = pygame.image.load(os.path.join(img_folder, 'virus.png'))
inventar = pygame.image.load(os.path.join(img_folder, 'invent.jpg'))
shotgun = pygame.image.load(os.path.join(img_folder, 'shotgun.png'))
rifle = pygame.image.load(os.path.join(img_folder, 'rifle.png'))
meteor = pygame.image.load(os.path.join(img_folder, 'meteor.png'))
ful_heart = pygame.image.load(os.path.join(img_folder, 'ful_heart.png'))
half_heart = pygame.image.load(os.path.join(img_folder, 'half_heart.png'))
non_heart = pygame.image.load(os.path.join(img_folder, 'non_heart.png'))
health = pygame.image.load(os.path.join(img_folder, 'health.png'))
fly_sh = pygame.image.load(os.path.join(img_folder, 'buckshot.png'))
button_press = pygame.image.load(os.path.join(img_folder, 'button_press.png'))
button_notpress = pygame.image.load(os.path.join(img_folder, 'button_notpress.png'))
menu_img = pygame.image.load(os.path.join(img_folder, 'menu.png'))
img_death = pygame.image.load(os.path.join(img_folder, 'skull.png'))
img_boss_virus = pygame.image.load(os.path.join(img_folder, 'boss_virus.png'))
boss = pygame.image.load(os.path.join(img_folder, 'boss_1.png'))

laser_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'laser.wav'))
laser_sound.set_volume(0.05)
shotgun_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'shotgun.wav'))
shotgun_sound.set_volume(0.2)
boom_snd = pygame.mixer.Sound(os.path.join(snd_folder, 'boom1.wav'))
boom_snd.set_volume(0.02)
metal = pygame.mixer.Sound(os.path.join(snd_folder, 'metal.wav'))
metal.set_volume(0.1)
heal_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'heal.wav'))
heal_sound.set_volume(0.22)
menu_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'menu.wav'))
menu_sound.set_volume(0.30)
ready = pygame.mixer.Sound(os.path.join(snd_folder, 'ready.wav'))
ready.set_volume(0.35)
pause_snd = pygame.mixer.Sound(os.path.join(snd_folder, 'pause.wav'))
pause_snd.set_volume(1)
win = pygame.mixer.Sound(os.path.join(snd_folder, 'win.wav'))
win.set_volume(0.45)
spacebar_snd = pygame.mixer.Sound(os.path.join(snd_folder, 'spacebar.wav'))
spacebar_snd.set_volume(0.30)

vader_images = []
vader_list = ['vader.png', 'vader2.png', 'vader3.png']
for img in vader_list:
    vader_images.append(pygame.image.load(os.path.join(img_folder, img)))

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['hu'] = []
for i in range(8):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    # img.set_colorkey((255, 255, 255))
    # img.set_colorkey((0, 0, 0))
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
    # img.set_colorkey((255, 255, 255))
    # img.set_colorkey((0, 0, 0))
    img_hu2 = pygame.transform.scale(img2, (300, 280))
    explosion_anim2['hu'].append(img_hu2)
    img_lg2 = pygame.transform.scale(img2, (145, 125))
    explosion_anim2['lg'].append(img_lg2)
    img_sm2 = pygame.transform.scale(img2, (70, 55))
    explosion_anim2['sm'].append(img_sm2)

reload_sounds = []
reload_list = ['reload0.wav', 'reload1.wav', 'reload2.wav']
for snd in reload_list:
    reload_sounds.append(pygame.mixer.Sound(os.path.join(snd_folder, snd)))

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
drobs = pygame.sprite.Group()
powerups = pygame.sprite.Group()
shotgun_fly = pygame.sprite.Group()
drobs_boss = pygame.sprite.Group()
bosses = pygame.sprite.Group()
vaders_group = pygame.sprite.Group()

hits = 0
score = 0
godmode = False
FPS = 25
s = 0
health_boss = 30
sprites = False
mob_b = False
putin = False
virus = False
vaders = True
death = False
for_file = []
root = None
key_btn = 0
mouse_btn = 1
count_bosses = 0
font_name = pygame.font.match_font('Segoe Script')
sh = 0
ju = 1
equip = 0
speed_enem = 4
gameovers = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 10
        self.image = img_bullet
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet, (15, 40))
        if sprites:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -35

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Drob_boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = img_bullet_sh
        self.radius = 5
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, 180)
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -13

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Drob2_boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = img_bullet_sh
        self.radius = 5
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, 210)
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -13
        self.speedx = -8

    def update(self):

        self.rect.y -= self.speedy
        self.rect.x -= self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Drob3_boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = img_bullet_sh
        self.radius = 5
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, -210)
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -13
        self.speedx = 8

    def update(self):
        self.rect.y -= self.speedy
        self.rect.x -= self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 150
        if mob_b:
            self.image = img_vader4
            self.image = pygame.transform.scale(img_vader4, (260, 200))
        elif putin:
            self.radius = 160
            self.image = img_putin
            self.image = pygame.transform.scale(img_putin, (200, 220))
            self.image.set_colorkey((0, 0, 0))
        elif virus:
            self.image = img_boss_virus
            self.image = pygame.transform.scale(img_boss_virus, (250, 250))
        elif vaders:
            self.image = boss
            self.image = pygame.transform.scale(boss, (200, 200))
        elif death:
            self.image = img_death
            self.image = pygame.transform.scale(img_death, (195, 250))
            self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        if sprites:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.x = x // 2 - 100
        self.rect.y = -300
        self.speedy = 2
        self.speedx = 10
        self.shoot_time = 1500
        self.last_shot = pygame.time.get_ticks()

    def shotgun_boss(self):
        global all_sprites
        global drobs_boss

        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            drob1 = Drob_boss(self.rect.centerx + 35, self.rect.bottom - 70)
            drob2 = Drob2_boss(self.rect.centerx + 35, self.rect.bottom - 70)
            drob3 = Drob3_boss(self.rect.centerx + 22, self.rect.bottom - 70)
            laser_sound.play()
            all_sprites.add(drob1)
            drobs_boss.add(drob1)
            all_sprites.add(drob2)
            drobs_boss.add(drob2)
            all_sprites.add(drob3)
            drobs_boss.add(drob3)

    def update(self):
        self.shotgun_boss()
        self.rect.y += self.speedy
        if self.rect.y == 50:
            self.speedy = 0
            self.rect.x -= self.speedx
            if self.rect.right < 0:
                self.rect.left = x + 200


class Boss_hard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 150
        if mob_b:
            self.image = img_vader4
            self.image = pygame.transform.scale(img_vader4, (260, 200))
        elif putin:
            self.radius = 160
            self.image = img_putin
            self.image = pygame.transform.scale(img_putin, (200, 220))
            self.image.set_colorkey((0, 0, 0))
        elif virus:
            self.image = img_boss_virus
            self.image = pygame.transform.scale(img_boss_virus, (250, 250))
        elif vaders:
            self.image = boss
            self.image = pygame.transform.scale(boss, (200, 200))
        elif death:
            self.image = img_death
            self.image = pygame.transform.scale(img_death, (195, 250))
            self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        if sprites:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.x = x // 2 - 100
        self.rect.y = -300
        self.speedy = 2
        self.speedx = 12
        self.shoot_time = 600
        self.last_shot = pygame.time.get_ticks()

    def shotgun_boss(self):
        global all_sprites
        global drobs_boss

        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            drob1 = Drob_boss(self.rect.centerx + 35, self.rect.bottom - 70)
            drob2 = Drob2_boss(self.rect.centerx + 35, self.rect.bottom - 70)
            drob3 = Drob3_boss(self.rect.centerx + 22, self.rect.bottom - 70)
            laser_sound.play()
            all_sprites.add(drob1)
            drobs_boss.add(drob1)
            all_sprites.add(drob2)
            drobs_boss.add(drob2)
            all_sprites.add(drob3)
            drobs_boss.add(drob3)

    def update(self):
        self.shotgun_boss()
        self.rect.y += self.speedy
        if self.rect.y == 50:
            self.speedy = 0
            self.rect.x -= self.speedx
            if self.rect.right < 0:
                self.rect.left = x + 200


def draw_health_bar_boss(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 300
    BAR_HEIGHT = 30
    fill = (pct / health_boss) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, red, fill_rect)
    pygame.draw.rect(surf, white, outline_rect, 2)


class Imperia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 25
        if mob_b:
            self.image_orig = img_vader4
            self.image = img_vader4
            self.image = pygame.transform.scale(img_vader4, (75, 60))
        elif putin:
            self.image_orig = img_putin
            self.image = img_putin
            self.image = pygame.transform.scale(img_putin, (68, 75))
            self.image.set_colorkey((0, 0, 0))
        elif virus:
            self.image_orig = img_virus
            self.image_orig = pygame.transform.scale(img_virus, (65, 90))
            self.image = self.image_orig.copy()
        elif vaders:
            self.image_orig = random.choice(vader_images)
            self.image = random.choice(vader_images)
        elif death:
            self.image_orig = img_death
            self.image = img_death
            self.image = pygame.transform.scale(img_death, (68, 88))
            self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randrange(50, x - 70)
        self.rect.y = random.randrange(-100, -30)
        self.speedy_imp = random.randrange(speed_enem+count_bosses//3, speed_enem * 3+count_bosses//2)
        self.speedx_imp = random.randrange(-speed_enem * 2-count_bosses//3, speed_enem+count_bosses//3)
        self.rot_speed = random.randrange(-20, 20)
        self.last_update = pygame.time.get_ticks()
        self.rot = 0

    def rotate(self):
        if virus == True:
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
        if virus == True:
            self.rotate()
        self.rect.y += self.speedy_imp
        self.rect.x += self.speedx_imp
        if (self.rect.top > y + 70) or (self.rect.left > x + 50) or (self.rect.right < 0):
            if not bosses:
                self.rect.x = random.randrange(50, x - 70)
                self.rect.y = random.randrange(-100, -30)
                self.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                self.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                self.rot_speed = random.randrange(-20, 20)
            else:
                self.kill()


class Inventar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = inventar
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(inventar, (40, 180))
        self.rect.bottom = 350
        self.rect.centerx = 25


class Drob(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 5
        self.image = img_bullet_sh
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -17

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Drob2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 5
        self.image = img_bullet_sh
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, 30)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -17
        self.speedx = -11

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Drob3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 5
        self.image = img_bullet_sh
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, -30)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -17
        self.speedx = 11

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Drob4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 5
        self.image = img_bullet_sh
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, 15)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -17
        self.speedx = -5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Drob5(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.radius = 5
        self.image = img_bullet_sh
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(img_bullet_sh, (20, 40))
        self.image = pygame.transform.rotate(self.image, -15)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -17
        self.speedx = 5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Icon_sh(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = shotgun
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(shotgun, (40, 20))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 465
        self.rect.centerx = 233


class Icon_sh_big(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = shotgun
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(shotgun, (80, 40))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 438
        self.rect.centerx = 215


class Icon_ju(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = rifle
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(rifle, (42, 30))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 553
        self.rect.centerx = 307


class Icon_ju_big(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = rifle
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(rifle, (84, 60))
        self.image = pygame.transform.rotate(self.image, 36)
        self.rect.bottom = 520
        self.rect.centerx = 285


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = meteor
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = 25
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randrange(50, x - 70)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = random.randrange(speed_enem//2+1+count_bosses//3, speed_enem*3+count_bosses//2)
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
        if self.rect.top > y + 60:
            if not bosses:
                self.rect.x = random.randrange(50, x - 70)
                self.rect.y = random.randrange(-100, -30)
                self.speedy = random.randrange(speed_enem // 2 + 1 + count_bosses // 3,
                                               speed_enem * 3 + count_bosses // 2)
                self.rot_speed = random.randrange(-10, 10)
            else:
                self.kill()


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
        if form == non_heart:
            self.image = pygame.transform.scale(form, (70, 70))
            self.rect.bottom = y - 2
            self.rect.centerx = x
        elif form == ful_heart:
            self.image = pygame.transform.scale(form, (70, 70))
            self.rect.bottom = y
            self.rect.centerx = x
        elif form == half_heart:
            self.image = pygame.transform.scale(form, (70, 70))
            self.rect.bottom = y + 1
            self.rect.centerx = x


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
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
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Explosion2(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
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
            if self.frame == len(explosion_anim2[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim2[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = health
        self.image = pygame.transform.scale(health, (50, 50))
        self.rect = self.image.get_rect()
        self.radius = 30
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randrange(100, x - 170)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > y + 60:
            self.kill()


class Fly_sh(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 30
        self.image = fly_sh
        self.image = pygame.transform.scale(fly_sh, (70, 70))
        self.rect = self.image.get_rect()
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randrange(100, x - 170)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > y + 60:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = img_npc
        self.image = pygame.transform.scale(img_npc, (130, 150))
        self.rect = self.image.get_rect()
        self.radius = 40
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.centerx = x // 2
        self.rect.bottom = y // 2 + y // 3
        self.speedx = 0
        self.speedy = 0
        self.shoot_time = 120
        self.last_shot = pygame.time.get_ticks()
        self.shotgun_time = 2150
        self.last_shotgun = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        if key_btn == 1 and mouse_btn == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.speedx = 30
            if key[pygame.K_a]:
                self.speedx = -30
            if key[pygame.K_w]:
                self.speedy = -30
            if key[pygame.K_s]:
                self.speedy = 30
            if ju == 1 and sh == 0:
                if key[pygame.K_SPACE]:
                    self.shoot()
            elif sh == 1 and equip == 1 and ju == 0:
                if key[pygame.K_SPACE]:
                    self.shotgun()
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        elif key_btn == 0 and mouse_btn == 1:
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()
            if ju == 1 and sh == 0:
                if pressed[0]:
                    self.shoot()
            elif sh == 1 and equip == 1 and ju == 0:
                if pressed[0]:
                    self.shotgun()
            self.rect.x = pos[0] - 50
            self.rect.y = pos[1] - 80
        if self.rect.left > x - 110:
            self.rect.right = x - 10
        if self.rect.right < 110:
            self.rect.left = 10
        if self.rect.top > y - 200:
            self.rect.top = y - 200
        if self.rect.bottom < 160:
            self.rect.bottom = 160

    def shoot(self):
        global all_sprites
        global bullets
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx + 12, self.rect.bottom - 87)
            bullet2 = Bullet(self.rect.centerx + 23, self.rect.bottom - 87)
            all_sprites.add(bullet)
            bullets.add(bullet)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            laser_sound.play()

    def shotgun(self):
        global all_sprites
        global drobs

        now_sh = pygame.time.get_ticks()
        if now_sh - self.last_shotgun > self.shotgun_time:
            self.last_shotgun = now_sh
            drob = Drob(self.rect.centerx + 15, self.rect.bottom - 85)
            drob2 = Drob2(self.rect.centerx - 5, self.rect.bottom - 85)
            drob3 = Drob3(self.rect.centerx + 20, self.rect.bottom - 85)
            drob4 = Drob4(self.rect.centerx + 3, self.rect.bottom - 85)
            drob5 = Drob5(self.rect.centerx + 17, self.rect.bottom - 85)
            shotgun_sound.play(0)
            all_sprites.add(drob)
            drobs.add(drob)
            all_sprites.add(drob2)
            drobs.add(drob2)
            all_sprites.add(drob3)
            drobs.add(drob3)
            all_sprites.add(drob4)
            drobs.add(drob4)
            all_sprites.add(drob5)
            drobs.add(drob5)


class Buttonpy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, monitor, text, function=None, image=button_notpress, image2=button_press):
        pygame.sprite.Sprite.__init__(self)  # it should be here
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
                spacebar()
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


class Npc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it should be here
        self.image = img_npc
        self.image = pygame.transform.scale(img_npc, (130, 150))
        self.rect = self.image.get_rect()
        self.radius = 40
        if sprites == True:
            pygame.draw.circle(self.image, (0, 0, 0), self.rect.center, self.radius)
        self.rect.centerx = x // 2
        self.rect.bottom = y // 2 + y // 3
        self.shoot_time = 120
        self.last_shot = pygame.time.get_ticks()
        self.shotgun_time = 2150
        self.last_shotgun = pygame.time.get_ticks()
        self.speedx = 15
        self.speedy = 3

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
        if self.rect.x >= x - 140:
            self.right = 1
            self.left = 0
        if self.rect.x <= 10:
            self.right = 0
            self.left = 1
        if self.rect.y > y - 210:
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
        global all_sprites
        global bullets
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_time:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx + 12, self.rect.bottom - 87)
            bullet2 = Bullet(self.rect.centerx + 23, self.rect.bottom - 87)
            all_sprites.add(bullet)
            bullets.add(bullet)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            laser_sound.play()

    def shotgun(self):
        global all_sprites
        global drobs

        now_sh = pygame.time.get_ticks()
        if now_sh - self.last_shotgun > self.shotgun_time:
            self.last_shotgun = now_sh
            drob = Drob(self.rect.centerx + 15, self.rect.bottom - 85)
            drob2 = Drob2(self.rect.centerx - 5, self.rect.bottom - 85)
            drob3 = Drob3(self.rect.centerx + 20, self.rect.bottom - 85)
            drob4 = Drob4(self.rect.centerx + 3, self.rect.bottom - 85)
            drob5 = Drob5(self.rect.centerx + 17, self.rect.bottom - 85)
            shotgun_sound.play(0)
            all_sprites.add(drob)
            drobs.add(drob)
            all_sprites.add(drob2)
            drobs.add(drob2)
            all_sprites.add(drob3)
            drobs.add(drob3)
            all_sprites.add(drob4)
            drobs.add(drob4)
            all_sprites.add(drob5)
            drobs.add(drob5)


count2 = 1


def god():
    global count2
    global godmode
    count2 += 1
    if count2 % 2 == 0:
        godmode = True
    else:
        godmode = False
    return count2, godmode


def game_without_meteors():
    global font_name
    global menu_sound
    global health_boss
    global ju, sh, equip
    global all_sprites, drobs, bullets, drobs_boss, bosses
    global score, count_bosses
    global waiting

    def pause():
        global waiting
        waiting = False
        btn_start.kill()
        btn_quit.kill()
        btn_menu.kill()
        return waiting

    pygame.mixer.music.load(os.path.join(snd_folder, 'pirate.mp3'))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    menu_sound.stop()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-50),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)

    gameover_bg = pygame.image.load(os.path.join(img_folder, 'gameover.jpg'))
    gameover_bg = pygame.transform.scale(gameover_bg, (x, y))
    gameover_rect = gameover_bg.get_rect()

    background4 = pygame.image.load(os.path.join(img_folder, 'background4.png'))
    background4 = pygame.transform.scale(background4, (x, y))
    background4_rect = background4.get_rect()

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']
    for img in background_list:
        if img == 'background1.jpg':
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x+200, y))
            background_images.append(bd)
        else:
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x, y))
            background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    all_sprites = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    shotgun_fly = pygame.sprite.Group()
    vaders_group = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    drobs_boss = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    drobs = pygame.sprite.Group()
    hearts = pygame.sprite.Group()
    buttons = pygame.sprite.Group()

    player = Player()
    inv = Inventar()
    shotgun = Icon_sh()
    shotgun_big = Icon_sh_big()
    rifle = Icon_ju()
    rifle_big = Icon_ju_big()
    heart1 = Heart(ful_heart, 165, 310)
    heart2 = Heart(ful_heart, 165 + 75, 310)
    heart3 = Heart(ful_heart, 165 + 150, 310)
    heart4 = Heart(ful_heart, 165 + 225, 310)
    heart5 = Heart(ful_heart, 165 + 300, 310)
    hearts.add(heart1)
    hearts.add(heart2)
    hearts.add(heart3)
    hearts.add(heart4)
    hearts.add(heart5)

    clock = pygame.time.Clock()
    count_bosses = 0
    hits = 0
    sh = 0
    ju = 1
    equip = 0
    heal = False
    sh_fly = False
    score = 0
    gameover = False
    health_boss2 = health_boss
    enemy = 25
    boss_time = 50000
    last_boss = pygame.time.get_ticks()
    waiting = False

    all_sprites.add(player)

    for i in range(enemy):
        imp = Imperia()
        all_sprites.add(imp)
        vaders_group.add(imp)

    all_sprites.add(inv)
    all_sprites.add(rifle_big)
    all_sprites.add(heart1)
    all_sprites.add(heart2)
    all_sprites.add(heart3)
    all_sprites.add(heart4)
    all_sprites.add(heart5)
    all_sprites.add(hearts)

    ready.play()
    for i in [3, 2, 1, 0]:
        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        best_score(screen, 30, x - 200, 40)
        if i == 0:
            draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
        else:
            draw_text(screen, str(i), 500, x // 2, 70)
        pygame.display.flip()
        time.sleep(1)

    pygame.event.clear()
    while True:
        clock.tick(FPS)
        nowboss = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_score()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    pause_snd.play(-1)

                    btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                    btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                    btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                    buttons.add(btn_quit)
                    buttons.add(btn_menu)
                    buttons.add(btn_start)

                    waiting = True
                    while waiting:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    waiting = False
                        buttons.update()
                        buttons.draw(screen)
                        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2, btn_quit.rect.y)
                        draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2, btn_menu.rect.y)
                        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2, btn_start.rect.y)
                        pygame.display.flip()
                        pygame.display.update()

                    pause_snd.stop()
                    pygame.mixer.music.unpause()

                elif event.key == pygame.K_g:
                    god()

                if key_btn == 1 and mouse_btn == 0:
                    if event.key == pygame.K_2:
                        if equip == 1:
                            if sh != 1:
                                random.choice(reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)
                    elif event.key == pygame.K_1:
                        if equip == 1:
                            if ju != 1:
                                random.choice(reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_btn == 1 and key_btn == 0:
                    if event.button == 4:
                        if equip == 1:
                            if ju != 1:
                                random.choice(reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)
                    elif event.button == 5:
                        if equip == 1:
                            if sh != 1:
                                random.choice(reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)

        if (nowboss - last_boss > boss_time) and not bosses:
            last_boss = nowboss
            health_boss += 10
            health_boss2 = health_boss
            boss = Boss()
            all_sprites.add(boss)
            bosses.add(boss)

        if random.random() > 0.999:
            if not powerups:
                heal = Health()
                all_sprites.add(heal)
                powerups.add(heal)

        if score >= 50:
            if random.random() > 0.9:
                if not shotgun_fly and equip != 1:
                    sh_fly = Fly_sh()
                    all_sprites.add(sh_fly)
                    shotgun_fly.add(sh_fly)

        if sh_fly:
            boom_sh_fly = pygame.sprite.spritecollide(player, shotgun_fly, True, pygame.sprite.collide_circle)

        if sh_fly:
            if boom_sh_fly:
                random.choice(reload_sounds).play()
                equip = 1
                ju = 0
                sh = 1
                all_sprites.add(shotgun_big)
                all_sprites.remove(shotgun)
                all_sprites.remove(rifle_big)
                all_sprites.add(rifle)

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True, pygame.sprite.collide_circle)
        boom_sh = pygame.sprite.groupcollide(vaders_group, drobs, False, False, pygame.sprite.collide_circle)
        boom = pygame.sprite.spritecollide(player, vaders_group, False, pygame.sprite.collide_circle)

        if bosses:
            boom_boss = pygame.sprite.groupcollide(bullets, bosses, True, False, pygame.sprite.collide_circle)
            boom_boss_drob = pygame.sprite.groupcollide(drobs, bosses, True, False, pygame.sprite.collide_circle)
            boom_bullet_boss = pygame.sprite.spritecollide(player, drobs_boss, True, pygame.sprite.collide_circle)

            for i in boom_bullet_boss:
                if not godmode:
                    hits += 1
                expl = Explosion2(i.rect.center, 'sm')
                all_sprites.add(expl)

            for i in boom_boss:
                if godmode:
                    health_boss2 -= 100
                elif boss.rect.y < -200:
                    health_boss2 = health_boss
                else:
                    health_boss2 -= 0.5

            for i in boom_boss_drob:
                if godmode:
                    health_boss2 -= 100
                elif boss.rect.y < -200:
                    health_boss2 = health_boss
                else:
                    health_boss2 -= 1.5

            if health_boss2 <= 0:
                boss.kill()
                bosses = pygame.sprite.Group()
                for i in drobs_boss:
                    if random.randint(1, 2) == 1:
                        expl = Explosion(i.rect.center, 'sm')
                        all_sprites.add(expl)
                    else:
                        expl = Explosion2(i.rect.center, 'sm')
                        all_sprites.add(expl)
                    i.kill()
                score += 15
                boom_snd.play()
                expl = Explosion(boss.rect.center, 'hu')
                all_sprites.add(expl)
                count_bosses += 3
                for _ in range(25):
                    imp = Imperia()
                    all_sprites.add(imp)
                    vaders_group.add(imp)

        if heal:
            boom_heal = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
            if boom_heal:
                hits = 0
                heart5.change(ful_heart, 165 + 300, 310)
                heart4.change(ful_heart, 165 + 225, 310)
                heart3.change(ful_heart, 165 + 150, 310)
                heart2.change(ful_heart, 165 + 75, 310)
                heart1.change(ful_heart, 165, 310)
                heal_sound.play()

        for hit in boom_b:
            score += 1
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit.rect.center, 'lg')
                all_sprites.add(expl)
            if not bosses:
                hit.rect.x = random.randrange(50, x - 70)
                hit.rect.y = random.randrange(-100, -30)
                hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit.rot_speed = random.randrange(-20, 20)
            else:
                hit.kill()

        for hit2 in boom_sh:
            score += 1
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            if not bosses:
                hit2.rect.x = random.randrange(50, x - 70)
                hit2.rect.y = random.randrange(-100, -30)
                hit2.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit2.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit2.rot_speed = random.randrange(-20, 20)
            else:
                hit2.kill()

        for hit4 in boom:
            metal.play()
            if not godmode:
                hits += 2
            if random.randint(1, 2) == 1:
                expl = Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            if not bosses:
                hit4.rect.x = random.randrange(50, x - 70)
                hit4.rect.y = random.randrange(-100, -30)
                hit4.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit4.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit4.rot_speed = random.randrange(-20, 20)
            else:
                hit4.kill()

        if gameover == True:
            current_score()
            deathes()

            for i in vaders_group:
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'lg')
                    all_sprites.add(expl)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.update()
                all_sprites.remove(i)
                vaders_group.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            for i in range(1):
                all_sprites.update()
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(player.rect.center, 'hu')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(player.rect.center, 'hu')
                    all_sprites.add(expl)
                all_sprites.update()
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.remove(player)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                all_sprites.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()

            for i in bosses:
                screen.blit(gameover_bg, gameover_rect)
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'hu')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'hu')
                    all_sprites.add(expl)
                all_sprites.update()
                all_sprites.remove(i)
                bosses.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            for i in drobs_boss:
                screen.blit(gameover_bg, gameover_rect)
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'lg')
                    all_sprites.add(expl)
                all_sprites.update()
                all_sprites.remove(i)
                drobs_boss.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            while gameover:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                        elif event.key == pygame.K_TAB:
                            gameover = False
                screen.blit(gameover_bg, gameover_rect)
                draw_text(screen, 'Нажмите "TAB", чтобы продолжить', x // 30, x // 2, y - 300)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                all_sprites.update()
                all_sprites.draw(screen)
                pygame.display.flip()
############################################
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)
            #####################
            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            bosses = pygame.sprite.Group()
            drobs_boss = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            hearts = pygame.sprite.Group()

            player = Player()
            inv = Inventar()
            shotgun = Icon_sh()
            shotgun_big = Icon_sh_big()
            rifle = Icon_ju()
            rifle_big = Icon_ju_big()
            heart1 = Heart(ful_heart, 165, 310)
            heart2 = Heart(ful_heart, 165 + 75, 310)
            heart3 = Heart(ful_heart, 165 + 150, 310)
            heart4 = Heart(ful_heart, 165 + 225, 310)
            heart5 = Heart(ful_heart, 165 + 300, 310)
            hearts.add(heart1)
            hearts.add(heart2)
            hearts.add(heart3)
            hearts.add(heart4)
            hearts.add(heart5)

            clock = pygame.time.Clock()
            health_boss -= (count_bosses // 3) * 10
            count_bosses = 0
            hits = 0
            sh = 0
            ju = 1
            equip = 0
            heal = False
            sh_fly = False
            a = True
            score = 0
            gameover = False
            health_boss2 = health_boss
            enemy = 25

            all_sprites.add(player)

            for i in range(enemy):
                imp = Imperia()
                all_sprites.add(imp)
                vaders_group.add(imp)

            all_sprites.add(inv)
            all_sprites.add(rifle_big)
            all_sprites.add(heart1)
            all_sprites.add(heart2)
            all_sprites.add(heart3)
            all_sprites.add(heart4)
            all_sprites.add(heart5)
            all_sprites.add(hearts)

            ready.play()
            for i in [3, 2, 1, 0]:
                if sprites == True:
                    screen.blit(background4, background4_rect)
                else:
                    screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                if i == 0:
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()
            boss_time = 50000
            last_boss = pygame.time.get_ticks()

        if hits == 1:
            heart5.change(half_heart, 165 + 300, 310)
        elif hits == 2:
            heart5.change(non_heart, 165 + 300, 310)
        elif hits == 3:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(half_heart, 165 + 225, 310)
        elif hits == 4:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
        elif hits == 5:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(half_heart, 165 + 150, 310)
        elif hits == 6:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
        elif hits == 7:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(half_heart, 165 + 75, 310)
        elif hits == 8:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(non_heart, 165 + 75, 310)
        elif hits == 9:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(non_heart, 165 + 75, 310)
            heart1.change(half_heart, 165, 310)
        elif hits >= 10:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(non_heart, 165 + 75, 310)
            heart1.change(non_heart, 165, 310)
            gameover = True

        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        best_score(screen, 30, x - 200, 40)
        if bosses:
            draw_health_bar_boss(screen, 30, 100, health_boss2)
        pygame.display.flip()
    return


def game():
    global font_name
    global menu_sound
    global health_boss
    global ju, sh, equip
    global all_sprites, drobs, bullets, drobs_boss, bosses
    global score, count_bosses
    global waiting

    def pause():
        global waiting
        waiting = False
        btn_start.kill()
        btn_quit.kill()
        return waiting

    pygame.mixer.music.load(os.path.join(snd_folder, 'fight.mp3'))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    menu_sound.stop()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-50),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)

    gameover_bg = pygame.image.load(os.path.join(img_folder, 'gameover.jpg'))
    gameover_bg = pygame.transform.scale(gameover_bg, (x, y))
    gameover_rect = gameover_bg.get_rect()

    background4 = pygame.image.load(os.path.join(img_folder, 'background4.png'))
    background4 = pygame.transform.scale(background4, (x, y))
    background4_rect = background4.get_rect()

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']
    for img in background_list:
        if img == 'background1.jpg':
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x+200, y))
            background_images.append(bd)
        else:
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x, y))
            background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    all_sprites = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    shotgun_fly = pygame.sprite.Group()
    vaders_group = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    drobs_boss = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    drobs = pygame.sprite.Group()
    hearts = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    buttons = pygame.sprite.Group()

    player = Player()
    inv = Inventar()
    shotgun = Icon_sh()
    shotgun_big = Icon_sh_big()
    rifle = Icon_ju()
    rifle_big = Icon_ju_big()
    heart1 = Heart(ful_heart, 165, 310)
    heart2 = Heart(ful_heart, 165 + 75, 310)
    heart3 = Heart(ful_heart, 165 + 150, 310)
    heart4 = Heart(ful_heart, 165 + 225, 310)
    heart5 = Heart(ful_heart, 165 + 300, 310)
    hearts.add(heart1)
    hearts.add(heart2)
    hearts.add(heart3)
    hearts.add(heart4)
    hearts.add(heart5)

    clock = pygame.time.Clock()
    count_bosses = 0
    hits = 0
    sh = 0
    ju = 1
    equip = 0
    heal = False
    sh_fly = False
    a = True
    score = 0
    gameover = False
    health_boss2 = health_boss
    enemy_vaders = 23
    enemy_meteors = 10
    boss_time = 50000
    last_boss = pygame.time.get_ticks()
    waiting = False

    all_sprites.add(player)

    for i in range(enemy_vaders):
        imp = Imperia()
        all_sprites.add(imp)
        vaders_group.add(imp)
    for i in range(enemy_meteors):
        m = Meteor()
        all_sprites.add(m)
        meteors.add(m)

    all_sprites.add(inv)
    all_sprites.add(rifle_big)
    all_sprites.add(heart1)
    all_sprites.add(heart2)
    all_sprites.add(heart3)
    all_sprites.add(heart4)
    all_sprites.add(heart5)
    all_sprites.add(hearts)

    ready.play()
    for i in [3, 2, 1, 0]:
        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        best_score(screen, 30, x - 200, 40)
        if i == 0:
            draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
        else:
            draw_text(screen, str(i), 500, x // 2, 70)
        pygame.display.flip()
        time.sleep(1)

    pygame.event.clear()
    while a:
        clock.tick(FPS)
        nowboss = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_score()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    pause_snd.play(-1)

                    btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                    btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                    btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                    buttons.add(btn_quit)
                    buttons.add(btn_menu)
                    buttons.add(btn_start)

                    waiting = True
                    while waiting:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    waiting = False
                        buttons.update()
                        buttons.draw(screen)
                        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2, btn_quit.rect.y)
                        draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2, btn_menu.rect.y)
                        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2, btn_start.rect.y)
                        pygame.display.flip()
                        pygame.display.update()

                    pause_snd.stop()
                    pygame.mixer.music.unpause()

                elif event.key == pygame.K_g:
                    god()

                if key_btn == 1 and mouse_btn == 0:
                    if event.key == pygame.K_2:
                        if equip == 1:
                            if sh != 1:
                                random.choice(reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)
                    elif event.key == pygame.K_1:
                        if equip == 1:
                            if ju != 1:
                                random.choice(reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_btn == 1 and key_btn == 0:
                    if event.button == 4:
                        if equip == 1:
                            if ju != 1:
                                random.choice(reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)
                    elif event.button == 5:
                        if equip == 1:
                            if sh != 1:
                                random.choice(reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)

        if (nowboss - last_boss > boss_time) and not bosses:
            last_boss = nowboss
            health_boss += 10
            health_boss2 = health_boss
            boss = Boss_hard()
            all_sprites.add(boss)
            bosses.add(boss)

        if random.random() > 0.9995:
            if not powerups:
                heal = Health()
                all_sprites.add(heal)
                powerups.add(heal)

        if score >= 50:
            if random.random() > 0.99:
                if not shotgun_fly and equip != 1:
                    sh_fly = Fly_sh()
                    all_sprites.add(sh_fly)
                    shotgun_fly.add(sh_fly)

        if sh_fly:
            boom_sh_fly = pygame.sprite.spritecollide(player, shotgun_fly, True, pygame.sprite.collide_circle)

        if sh_fly:
            if boom_sh_fly:
                random.choice(reload_sounds).play()
                equip = 1
                ju = 0
                sh = 1
                all_sprites.add(shotgun_big)
                all_sprites.remove(shotgun)
                all_sprites.remove(rifle_big)
                all_sprites.add(rifle)

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True, pygame.sprite.collide_circle)
        boom_sh = pygame.sprite.groupcollide(vaders_group, drobs, False, False)
        boom = pygame.sprite.spritecollide(player, vaders_group, False, pygame.sprite.collide_circle)
        boom_m = pygame.sprite.spritecollide(player, meteors, False, pygame.sprite.collide_circle)

        if bosses:
            boom_boss = pygame.sprite.groupcollide(bullets, bosses, True, False)
            boom_boss_drob = pygame.sprite.groupcollide(drobs, bosses, True, False)
            boom_bullet_boss = pygame.sprite.spritecollide(player, drobs_boss, True, pygame.sprite.collide_circle)

            for i in boom_bullet_boss:
                if not godmode:
                    hits += 1
                expl = Explosion2(i.rect.center, 'sm')
                all_sprites.add(expl)

            for i in boom_boss:
                if godmode:
                    health_boss2 -= 100
                elif boss.rect.y < -200:
                    health_boss2 = health_boss
                else:
                    health_boss2 -= 0.5

            for i in boom_boss_drob:
                if godmode:
                    health_boss2 -= 100
                elif boss.rect.y < -200:
                    health_boss2 = health_boss
                else:
                    health_boss2 -= 1

            if health_boss2 <= 0:
                boss.kill()
                bosses = pygame.sprite.Group()
                for i in drobs_boss:
                    if random.randint(1, 2) == 1:
                        expl = Explosion(i.rect.center, 'sm')
                        all_sprites.add(expl)
                    else:
                        expl = Explosion2(i.rect.center, 'sm')
                        all_sprites.add(expl)
                    i.kill()
                score += 50
                boom_snd.play()
                expl = Explosion(boss.rect.center, 'hu')
                all_sprites.add(expl)
                count_bosses += 3
                for _ in range(enemy_vaders):
                    imp = Imperia()
                    all_sprites.add(imp)
                    vaders_group.add(imp)
                for _ in range(enemy_meteors):
                    m = Meteor()
                    all_sprites.add(m)
                    meteors.add(m)

        if heal:
            boom_heal = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
            if boom_heal:
                hits = 0
                heart5.change(ful_heart, 165 + 300, 310)
                heart4.change(ful_heart, 165 + 225, 310)
                heart3.change(ful_heart, 165 + 150, 310)
                heart2.change(ful_heart, 165 + 75, 310)
                heart1.change(ful_heart, 165, 310)
                heal_sound.play()

        for hit3 in boom_m:
            metal.play()
            if not godmode:
                hits += 1
            if random.randint(1, 2) == 1:
                expl = Explosion(hit3.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit3.rect.center, 'sm')
                all_sprites.add(expl)
            hit3.rect.x = random.randrange(50, x - 70)
            hit3.rect.y = random.randrange(-100, -30)
            hit3.speedy = random.randrange(speed_enem // 2 + 1 + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit3.rot_speed = random.randrange(-10, 10)

        for hit in boom_b:
            score += 1
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit.rect.center, 'lg')
                all_sprites.add(expl)
            if not bosses:
                hit.rect.x = random.randrange(50, x - 70)
                hit.rect.y = random.randrange(-100, -30)
                hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit.rot_speed = random.randrange(-20, 20)
            else:
                hit.kill()

        for hit2 in boom_sh:
            score += 1
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            if not bosses:
                hit2.rect.x = random.randrange(50, x - 70)
                hit2.rect.y = random.randrange(-100, -30)
                hit2.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit2.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit2.rot_speed = random.randrange(-20, 20)
            else:
                hit2.kill()

        for hit4 in boom:
            metal.play()
            if not godmode:
                hits += 2
            if random.randint(1, 2) == 1:
                expl = Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            if not bosses:
                hit4.rect.x = random.randrange(50, x - 70)
                hit4.rect.y = random.randrange(-100, -30)
                hit4.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit4.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit4.rot_speed = random.randrange(-20, 20)
            else:
                hit4.kill()

        if gameover == True:
            current_score()
            deathes()

            for i in vaders_group:
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'lg')
                    all_sprites.add(expl)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.update()
                all_sprites.remove(i)
                vaders_group.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            for i in range(1):
                all_sprites.update()
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(player.rect.center, 'hu')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(player.rect.center, 'hu')
                    all_sprites.add(expl)
                all_sprites.update()
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.remove(player)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                all_sprites.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
            for i in meteors:
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'lg')
                    all_sprites.add(expl)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.update()
                all_sprites.remove(i)
                meteors.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            for i in bosses:
                    screen.blit(gameover_bg, gameover_rect)
                    boom_snd.play()
                    if random.randint(1, 2) == 1:
                        expl = Explosion(i.rect.center, 'hu')
                        all_sprites.add(expl)
                    else:
                        expl = Explosion2(i.rect.center, 'hu')
                        all_sprites.add(expl)
                    all_sprites.update()
                    all_sprites.remove(i)
                    bosses.remove(i)
                    all_sprites.draw(screen)
                    draw_text(screen, 'Счёт:', 30, x // 2, 10)
                    draw_text(screen, str(score), 30, x // 2, 40)
                    draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                    best_score(screen, 30, x - 200, 40)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.mixer.music.pause()
                                pause_snd.play(-1)

                                btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                                btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                                btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                                buttons.add(btn_quit)
                                buttons.add(btn_menu)
                                buttons.add(btn_start)

                                waiting = True
                                while waiting:
                                    clock.tick(10)
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_ESCAPE:
                                                waiting = False
                                    buttons.update()
                                    buttons.draw(screen)
                                    draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                              btn_quit.rect.y)
                                    draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                              btn_menu.rect.y)
                                    draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                              btn_start.rect.y)
                                    pygame.display.flip()
                                    pygame.display.update()

                                pause_snd.stop()
                                pygame.mixer.music.unpause()
                    pygame.display.flip()

            for i in drobs_boss:
                screen.blit(gameover_bg, gameover_rect)
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'lg')
                    all_sprites.add(expl)
                all_sprites.update()
                all_sprites.remove(i)
                drobs_boss.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            while gameover:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if event.key == pygame.K_ESCAPE:
                                pygame.mixer.music.pause()
                                pause_snd.play(-1)

                                btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                                btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                                btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                                buttons.add(btn_quit)
                                buttons.add(btn_menu)
                                buttons.add(btn_start)

                                waiting = True
                                while waiting:
                                    clock.tick(10)
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_ESCAPE:
                                                waiting = False
                                    buttons.update()
                                    buttons.draw(screen)
                                    draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                              btn_quit.rect.y)
                                    draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                              btn_menu.rect.y)
                                    draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                              btn_start.rect.y)
                                    pygame.display.flip()
                                    pygame.display.update()

                                pause_snd.stop()
                                pygame.mixer.music.unpause()
                        elif event.key == pygame.K_TAB:
                            gameover = False
                screen.blit(gameover_bg, gameover_rect)
                draw_text(screen, 'Нажмите "TAB", чтобы продолжить', x // 30, x // 2, y - 300)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                all_sprites.update()
                all_sprites.draw(screen)
                pygame.display.flip()

            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)

            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            bosses = pygame.sprite.Group()
            drobs_boss = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            hearts = pygame.sprite.Group()
            meteors = pygame.sprite.Group()
            buttons = pygame.sprite.Group()

            player = Player()
            inv = Inventar()
            shotgun = Icon_sh()
            shotgun_big = Icon_sh_big()
            rifle = Icon_ju()
            rifle_big = Icon_ju_big()
            heart1 = Heart(ful_heart, 165, 310)
            heart2 = Heart(ful_heart, 165 + 75, 310)
            heart3 = Heart(ful_heart, 165 + 150, 310)
            heart4 = Heart(ful_heart, 165 + 225, 310)
            heart5 = Heart(ful_heart, 165 + 300, 310)
            hearts.add(heart1)
            hearts.add(heart2)
            hearts.add(heart3)
            hearts.add(heart4)
            hearts.add(heart5)

            clock = pygame.time.Clock()
            count_bosses = 0
            hits = 0
            sh = 0
            ju = 1
            equip = 0
            heal = False
            sh_fly = False
            a = True
            score = 0
            gameover = False
            health_boss2 = health_boss
            enemy_vaders = 23
            enemy_meteors = 10
            boss_time = 50000
            last_boss = pygame.time.get_ticks()
            waiting = False

            all_sprites.add(player)

            for i in range(enemy_vaders):
                imp = Imperia()
                all_sprites.add(imp)
                vaders_group.add(imp)
            for i in range(enemy_meteors):
                m = Meteor()
                all_sprites.add(m)
                meteors.add(m)

            all_sprites.add(inv)
            all_sprites.add(rifle_big)
            all_sprites.add(heart1)
            all_sprites.add(heart2)
            all_sprites.add(heart3)
            all_sprites.add(heart4)
            all_sprites.add(heart5)
            all_sprites.add(hearts)

            ready.play()
            for i in [3, 2, 1, 0]:
                if sprites == True:
                    screen.blit(background4, background4_rect)
                else:
                    screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                if i == 0:
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()
            boss_time = 50000
            last_boss = pygame.time.get_ticks()

        if hits == 1:
            heart5.change(half_heart, 165 + 300, 310)
        elif hits == 2:
            heart5.change(non_heart, 165 + 300, 310)
        elif hits == 3:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(half_heart, 165 + 225, 310)
        elif hits == 4:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
        elif hits == 5:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(half_heart, 165 + 150, 310)
        elif hits == 6:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
        elif hits == 7:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(half_heart, 165 + 75, 310)
        elif hits == 8:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(non_heart, 165 + 75, 310)
        elif hits == 9:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(non_heart, 165 + 75, 310)
            heart1.change(half_heart, 165, 310)
        elif hits >= 10:
            heart5.change(non_heart, 165 + 300, 310)
            heart4.change(non_heart, 165 + 225, 310)
            heart3.change(non_heart, 165 + 150, 310)
            heart2.change(non_heart, 165 + 75, 310)
            heart1.change(non_heart, 165, 310)
            gameover = True

        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        best_score(screen, 30, x - 200, 40)
        if bosses:
            draw_health_bar_boss(screen, 30, 100, health_boss2)
        pygame.display.flip()
    return


def kill_or_die():
    global font_name
    global menu_sound
    global ju, sh, equip
    global all_sprites, drobs, bullets
    global waiting

    def pause():
        global waiting
        waiting = False
        btn_start.kill()
        btn_quit.kill()
        return waiting

    menu_sound.stop()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-50),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    gameover_bg = pygame.image.load(os.path.join(img_folder, 'gameover.jpg'))
    gameover_bg = pygame.transform.scale(gameover_bg, (x, y))
    gameover_rect = gameover_bg.get_rect()

    background4 = pygame.image.load(os.path.join(img_folder, 'background4.png'))
    background4 = pygame.transform.scale(background4, (x, y))
    background4_rect = background4.get_rect()

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']
    for img in background_list:
        bd = pygame.image.load(os.path.join(img_folder, img))
        bd = pygame.transform.scale(bd, (x, y))
        background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    all_sprites = pygame.sprite.Group()
    shotgun_fly = pygame.sprite.Group()
    vaders_group = pygame.sprite.Group()
    drobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    buttons = pygame.sprite.Group()

    player = Player()
    inv = Inventar()
    shotgun = Icon_sh()
    shotgun_big = Icon_sh_big()
    rifle = Icon_ju()
    rifle_big = Icon_ju_big()
    all_sprites.add(player)
    for i in range(28):
        imp = Imperia()
        all_sprites.add(imp)
        vaders_group.add(imp)
    sh = 0
    ju = 1
    sh_fly = False
    score = 1400
    a = True
    count = 700
    count_loose = 0
    count_win = 1
    equip = 0
    gameover = False
    waiting = False

    all_sprites.add(inv)
    all_sprites.add(rifle_big)

    ready.play()
    for i in [3, 2, 1, 0]:
        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        best_score(screen, 30, x - 200, 40)
        draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
        if i == 0:
            pygame.mixer.music.load(os.path.join(snd_folder, 'speed.mp3'))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
            draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
        else:
            draw_text(screen, str(i), 500, x // 2, 70)
        pygame.display.flip()
        time.sleep(1)

    pygame.event.clear()
    while a:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_score()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

                    pygame.mixer.music.pause()
                    pause_snd.play(-1)

                    btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                    btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                    btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                    buttons.add(btn_quit)
                    buttons.add(btn_menu)
                    buttons.add(btn_start)

                    waiting = True
                    while waiting:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    waiting = False
                        buttons.update()
                        buttons.draw(screen)
                        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                  btn_quit.rect.y)
                        draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                  btn_menu.rect.y)
                        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                  btn_start.rect.y)
                        pygame.display.flip()
                        pygame.display.update()

                    pause_snd.stop()
                    pygame.mixer.music.unpause()

                elif event.key == pygame.K_g:
                    god()

                if key_btn == 1 and mouse_btn == 0:
                    if event.key == pygame.K_2:
                        if equip == 1:
                            if sh != 1:
                                random.choice(reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)
                    elif event.key == pygame.K_1:
                        if equip == 1:
                            if ju != 1:
                                random.choice(reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_btn == 1 and key_btn == 0:
                    if event.button == 4:
                        if equip == 1:
                            if ju != 1:
                                random.choice(reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)
                    elif event.button == 5:
                        if equip == 1:
                            if sh != 1:
                                random.choice(reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)

        count -= 1
        draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
        pygame.display.flip()

        if gameover == True:
            current_score()
            deathes()

            for i in vaders_group:
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(i.rect.center, 'lg')
                    all_sprites.add(expl)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.update()
                all_sprites.remove(i)
                vaders_group.remove(i)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:

                            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                pygame.display.flip()

            for i in range(1):
                all_sprites.update()
                boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = Explosion(player.rect.center, 'hu')
                    all_sprites.add(expl)
                else:
                    expl = Explosion2(player.rect.center, 'hu')
                    all_sprites.add(expl)
                all_sprites.update()
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.remove(player)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                all_sprites.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:

                            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()

            while gameover:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:

                            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

                            pygame.mixer.music.pause()
                            pause_snd.play(-1)

                            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
                            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            pause_snd.stop()
                            pygame.mixer.music.unpause()
                        elif event.key == pygame.K_TAB:
                            gameover = False
                screen.blit(gameover_bg, gameover_rect)
                draw_text(screen, 'Нажмите "TAB", чтобы продолжить', x // 30, x // 2, y - 300)
                all_sprites.update()
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                pygame.display.flip()

            pygame.mixer.music.stop()

            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            buttons = pygame.sprite.Group()

            player = Player()
            inv = Inventar()
            shotgun = Icon_sh()
            shotgun_big = Icon_sh_big()
            rifle = Icon_ju()
            rifle_big = Icon_ju_big()
            all_sprites.add(player)
            for i in range(28):
                imp = Imperia()
                all_sprites.add(imp)
                vaders_group.add(imp)
            sh = 0
            ju = 1
            sh_fly = False
            score = 0
            a = True
            count = 700
            count_loose = 0
            count_win = 1
            equip = 0
            gameover = False
            waiting = False

            all_sprites.add(inv)
            all_sprites.add(rifle_big)

            ready.play()
            for i in [3, 2, 1, 0]:
                if sprites == True:
                    screen.blit(background4, background4_rect)
                else:
                    screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                if i == 0:
                    pygame.mixer.music.load(os.path.join(snd_folder, 'speed.mp3'))
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()

        if count == 0 and score < 200 * count_win:
            gameover = True

        elif count == 0 and score >= 200 * count_win:
            count_win += 1
            count_loose += 1
            count = 700 - (100 * count_loose)
            pygame.display.flip()

        if count_loose == 7 and score >= 1400:
            pygame.mixer.music.stop()
            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
            draw_text(screen, 'Поздравляем! Вы ВЫИГРАЛИ!!!', x // 23, x // 2, y // 2)
            pygame.display.flip()

            win.play(-1)
            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

            pygame.mixer.music.pause()

            btn_quit = Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
            btn_menu = Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', menushka)
            btn_start = Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Рестарт', pause)
            buttons.add(btn_quit)
            buttons.add(btn_menu)
            buttons.add(btn_start)

            waiting = True
            while waiting:
                clock.tick(10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            waiting = False
                buttons.update()
                buttons.draw(screen)
                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                            btn_quit.rect.y)
                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                            btn_menu.rect.y)
                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                            btn_start.rect.y)
                pygame.display.flip()
                pygame.display.update()

            win.stop()

            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            buttons = pygame.sprite.Group()

            player = Player()
            inv = Inventar()
            shotgun = Icon_sh()
            shotgun_big = Icon_sh_big()
            rifle = Icon_ju()
            rifle_big = Icon_ju_big()
            all_sprites.add(player)
            for i in range(28):
                imp = Imperia()
                all_sprites.add(imp)
                vaders_group.add(imp)
            sh = 0
            ju = 1
            sh_fly = False
            score = 0
            a = True
            count = 700
            count_loose = 0
            count_win = 1
            equip = 0
            gameover = False
            waiting = False

            all_sprites.add(inv)
            all_sprites.add(rifle_big)

            ready.play()
            for i in [3, 2, 1, 0]:
                if sprites == True:
                    screen.blit(background4, background4_rect)
                else:
                    screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                best_score(screen, 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                if i == 0:
                    pygame.mixer.music.load(os.path.join(snd_folder, 'speed.mp3'))
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()

        if score >= 50:
            if random.random() > 0.99:
                if not shotgun_fly and equip != 1:
                    sh_fly = Fly_sh()
                    all_sprites.add(sh_fly)
                    shotgun_fly.add(sh_fly)

        if sh_fly:
            boom_sh_fly = pygame.sprite.spritecollide(player, shotgun_fly, True, pygame.sprite.collide_circle)
            if boom_sh_fly:
                random.choice(reload_sounds).play()
                equip = 1
                ju = 0
                sh = 1
                all_sprites.add(shotgun_big)
                all_sprites.remove(shotgun)
                all_sprites.remove(rifle_big)
                all_sprites.add(rifle)

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True)
        boom_sh = pygame.sprite.groupcollide(vaders_group, drobs, False, False)
        boom = pygame.sprite.spritecollide(player, vaders_group, False, pygame.sprite.collide_circle)

        for hit in boom_b:
            score += 1
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit.rect.center, 'lg')
                all_sprites.add(expl)
            hit.rect.x = random.randrange(50, x - 70)
            hit.rect.y = random.randrange(-100, -30)
            hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit.rot_speed = random.randrange(-20, 20)

        for hit2 in boom_sh:
            score += 1
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            hit2.rect.x = random.randrange(50, x - 70)
            hit2.rect.y = random.randrange(-100, -30)
            hit2.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit2.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit2.rot_speed = random.randrange(-20, 20)

        for hit4 in boom:
            metal.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            hit4.rect.x = random.randrange(50, x - 70)
            hit4.rect.y = random.randrange(-100, -30)
            hit4.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit4.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit4.rot_speed = random.randrange(-20, 20)

        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        best_score(screen, 30, x - 200, 40)
        pygame.display.flip()
    return


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def unlock():
    global s
    with open('score.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            list = lines[0].split(' ')
            for i in list:
                if i != '':
                    s += int(i)


def current_score():
    with open('score.txt', 'a') as file:
        file.write(str(score) + ' ')


def best_score(surf, size, x, y):
    global best_count
    with open('score.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            list = lines[0].split(' ')
            for i in list:
                if i != '':
                    for_file.append(int(i))
    font = pygame.font.Font(font_name, size)
    if lines:
        text_surface = font.render(str(max(for_file)), True, (255, 255, 255))
    else:
        text_surface = font.render(str(0), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def spacebar():
    spacebar_snd.play()


def break_pause():
    global tk
    tk.destroy()


def super_break():
    current_score()
    pygame.quit()
    sys.exit()


count1 = 1


def sprite():
    spacebar()
    global sprites
    global count1
    global button_sprites

    count1 += 1
    if count1 % 2 == 0 and count1 != 0:
        button_sprites['text'] = 'Да'
        sprites = True
    else:
        button_sprites['text'] = 'Нет'
        sprites = False

    return sprites, button_sprites


def keyboard():
    spacebar()
    global mouse_btn
    global key_btn
    key_btn = 1
    mouse_btn = 0
    return key_btn, mouse_btn


def mouse():
    spacebar()
    global mouse_btn
    global key_btn
    key_btn = 0
    mouse_btn = 1
    return key_btn, mouse_btn


def speed():
    global speed_enem
    speed_enem = int(scale1.get())
    return speed_enem


def skins():
    spacebar()
    global mob_b, putin, virus, vaders, death

    if var.get() == 0:
        vaders = False
        mob_b = True
        virus = False
        putin = False
        death = False
    elif var.get() == 1:
        vaders = False
        putin = True
        virus = False
        mob_b = False
        death = False
    elif var.get() == 2:
        vaders = False
        virus = True
        putin = False
        mob_b = False
        death = False
    elif var.get() == 3:
        vaders = True
        mob_b = False
        virus = False
        putin = False
        death = False
    elif var.get() == 4:
        death = True
        vaders = False
        mob_b = False
        virus = False
        putin = False
    return vaders, virus, putin, mob_b, death


def reset():
    global vaders_group, all_sprites
    for i in vaders_group:
        i.kill()
    for i in range(25):
        imp = Imperia()
        all_sprites.add(imp)
        vaders_group.add(imp)


def control():
    spacebar()
    if key_btn == 1:
        messagebox.showinfo('Меню игры STAR WARS - THE JOKE',
                            'УПРАВЛЕНИЕ: \n W - вверх \n S - вниз \n A - влево \n D - вправо \n ПРОБЕЛ - стрелять \n "1" - переключить на первое оружие \n "2" - переключить на второе оружие \n "ESC" - пауза \n Общий счёт в игре: ' + str(
                                s))
    elif mouse_btn == 1:
        messagebox.showinfo('Меню игры STAR WARS - THE JOKE',
                            'УПРАВЛЕНИЕ: \n Передвижение мышкой \n ЛЕВАЯ кнопка мыши - стрелять \n Переключать оружия КОЛЁСИКОМ мыши \n "ESC" - поставить / убрать паузу\n Общий счёт в игре: ' + str(
                                s))
    return


def deathes():
    with open('deathes.txt', 'a') as file:
        file.write('1 ')


def success():
    global gameovers
    for_file = []
    with open('deathes.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            list = lines[0].split(' ')
            for i in list:
                if i != '':
                    for_file.append(int(i))
    if lines:
        gameovers = sum(for_file)
    else:
        gameovers = 0


img1 = Image.open(os.path.join(img_folder, 'vader4.png'))
img1 = img1.resize((80, 70), Image.ANTIALIAS)
putin1 = Image.open(os.path.join(img_folder, 'putin.png'))
putin1 = putin1.resize((70, 80), Image.ANTIALIAS)
virus1 = Image.open(os.path.join(img_folder, 'virus.png'))
virus1 = virus1.resize((80, 105), Image.ANTIALIAS)
img2 = Image.open(os.path.join(img_folder, 'vader.png'))
img2 = img2.resize((75, 75), Image.ANTIALIAS)
img3 = Image.open(os.path.join(img_folder, 'option.png'))
img3 = img3.resize((45, 45), Image.ANTIALIAS)
img_option = Image.open(os.path.join(img_folder, 'option.png'))
img_option = img_option.resize((35, 35), Image.ANTIALIAS)
img_key = Image.open(os.path.join(img_folder, 'keyb.jpeg'))
img_key = img_key.resize((70, 70), Image.ANTIALIAS)
img_mouse = Image.open(os.path.join(img_folder, 'keym.png'))
img_mouse = img_mouse.resize((70, 70), Image.ANTIALIAS)
img_achievement = Image.open(os.path.join(img_folder, 'star.png'))
img_achievement = img_achievement.resize((35, 35), Image.ANTIALIAS)


def achievements():
    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()+10, root.winfo_screenheight()+10))

    def break_root():
        root.destroy()

    img_ram = Image.open(os.path.join(img_folder, 'ram.jpg'))
    img_ram = img_ram.resize((x, y), Image.ANTIALIAS)
    img_ram = ImageTk.PhotoImage(img_ram)

    img_achievement2 = ImageTk.PhotoImage(img_achievement)

    img_skull = Image.open(os.path.join(img_folder, 'skull.png'))
    img_skull = img_skull.resize((55, 70), Image.ANTIALIAS)
    img_skull2 = ImageTk.PhotoImage(img_skull)

    canvas = Canvas(root, width=x+10, height=y+10, bg='black')
    canvas.pack()

    img_ram = Image.open(os.path.join(img_folder, 'ram.jpg'))
    img_ram = img_ram.resize((x, y), Image.ANTIALIAS)
    img_ram = ImageTk.PhotoImage(img_ram, master=root)

    canvas.create_image(x//2, y//2-25, image=img_ram)

    canvas.create_image(17, 20, image=img_achievement2)
    if gameovers >= 50:
        text = canvas.create_text(130, 20, font=("Comic Sans MS", 15), text="Умрите 50 раз", fill="#dceca4")
        text = canvas.create_text(130, 50, font=("Comic Sans MS", 20), text="Получено", fill="#dceca4")
    else:
        text = canvas.create_text(130, 20, font=("Comic Sans MS", 15), text="Умрите " + (str(50 - gameovers)) + ' раз',
                                  fill="#dceca4")
        text = canvas.create_text(130, 50, font=("Comic Sans MS", 15), text="Награда: скин ", fill="#dceca4")
        canvas.create_image(230, 50, image=img_skull2)

    d = Button(text="OK", command=break_root, font=("Comic Sans MS", 30))
    d.place(x=50, y=y-200)
    d['bg'] = '#dceca4'
    d['activebackground'] = 'black'
    d['fg'] = 'black'
    d['activeforeground'] = '#dceca4'

    root.bind('<Return>', break_root)

    root.overrideredirect(1)
    #root.state('zoomed')
    root.attributes("-topmost", True)
    root.update()
    root.deiconify()
    root.mainloop()
    return


def settings():
    global scale1
    global button_sprites
    global var

    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()+10, root.winfo_screenheight()+10))

    def destroy():
        speed()
        skins()
        reset()
        root.destroy()

    img_ram = Image.open(os.path.join(img_folder, 'ram.jpg'))
    img_ram = img_ram.resize((x, y), Image.ANTIALIAS)
    img_ram = ImageTk.PhotoImage(img_ram)

    img_skull = Image.open(os.path.join(img_folder, 'skull.png'))
    img_skull = img_skull.resize((65, 80), Image.ANTIALIAS)
    img_skull2 = ImageTk.PhotoImage(img_skull)

    img_keyb = ImageTk.PhotoImage(img_key)

    img_keym = ImageTk.PhotoImage(img_mouse)

    img_option2 = ImageTk.PhotoImage(img_option)

    img_vader4 = ImageTk.PhotoImage(img1)

    img_putin = ImageTk.PhotoImage(putin1)

    img_virus = ImageTk.PhotoImage(virus1)

    img_vaders = ImageTk.PhotoImage(img2)

    canvas = Canvas(root, width=x+10, height=y+10, bg='black')
    canvas.pack()

    img_ram = Image.open(os.path.join(img_folder, 'ram.jpg'))
    img_ram = img_ram.resize((x, y), Image.ANTIALIAS)
    img_ram = ImageTk.PhotoImage(img_ram, master=root)

    canvas.create_image(x//2, y//2-25, image=img_ram)

    text = canvas.create_text(270, 20, font=("Comic Sans MS", 15), text="Минимальная скорость врагов(по умолчанию 8)", fill="#dceca4")
    scale1 = Scale(canvas, orient=HORIZONTAL, length=700, from_=1, to=25, tickinterval=1, resolution=1, bg='black', fg='#dceca4')
    scale1.place(x=0, y=35)
    canvas.create_image(17, 20, image=img_option2)

    text = canvas.create_text(190, 140, font=("Comic Sans MS", 15), text="Включать прорисовку спрайтов", fill="#dceca4")
    if sprites:
        button_sprites = Button(text="Да", command=sprite)
        button_sprites.place(x=350, y=130)
        button_sprites['bg'] = '#dceca4'
        button_sprites['activebackground'] = 'black'
        button_sprites['fg'] = 'black'
        button_sprites['activeforeground'] = '#dceca4'
    else:
        button_sprites = Button(root, text='Нет', command=sprite)
        button_sprites.place(x=350, y=130)
        button_sprites['bg'] = '#dceca4'
        button_sprites['activebackground'] = 'black'
        button_sprites['fg'] = 'black'
        button_sprites['activeforeground'] = '#dceca4'
    canvas.create_image(17, 140, image=img_option2)

    text = canvas.create_text(160, 220, font=("Comic Sans MS", 15), text="Изображения для врагов", fill="#dceca4")
    canvas.create_image(17, 220, image=img_option2)
    canvas.create_image(60, 280, image=img_vader4)
    canvas.create_image(148, 280, image=img_putin)
    canvas.create_image(238, 280, image=img_virus)
    canvas.create_image(326, 280, image=img_vaders)
    if gameovers >= 50:
        canvas.create_image(420, 280, image=img_skull2)
    var = IntVar()
    var.set(3)
    radio = Radiobutton(root, variable=var, value=0)
    radio.place(x=45, y=325)
    radio = Radiobutton(root, variable=var, value=1)
    radio.place(x=135, y=325)
    radio = Radiobutton(root, variable=var, value=2)
    radio.place(x=225, y=325)
    radio = Radiobutton(root, variable=var, value=3)
    radio.place(x=315, y=325)
    if gameovers >= 50:
        radio = Radiobutton(root, variable=var, value=4)
        radio.place(x=404, y=325)

    text = canvas.create_text(135, 410, font=("Comic Sans MS", 15), text="Способ управления", fill="#dceca4")
    canvas.create_image(17, 410, image=img_option2)
    buttonkey = Button(command=keyboard, image=img_keyb)
    buttonkey.place(x=30, y=460)
    buttonmouse = Button(command=mouse, image=img_keym)
    buttonmouse.place(x=140, y=460)

    text = canvas.create_text(270, 610, font=("Comic Sans MS", 15), text="Здесь можно посмотреть текущее управление", fill="#dceca4")
    canvas.create_image(17, 610, image=img_option2)
    button = Button(text="Здесь", command=control, font=("Comic Sans MS", 10))
    button.place(x=55, y=630)
    button['bg'] = '#dceca4'
    button['activebackground'] = 'black'
    button['fg'] = 'black'
    button['activeforeground'] = '#dceca4'

    d = Button(text="Подтведить эти изменения", command=destroy, font=("Comic Sans MS", 17))
    d.place(x=20, y=y-120)
    d['bg'] = '#dceca4'
    d['activebackground'] = 'black'
    d['fg'] = 'black'
    d['activeforeground'] = '#dceca4'

    root.overrideredirect(1)
    #root.state('zoomed')
    root.attributes("-topmost", True)
    root.update()
    root.deiconify()
    root.mainloop()
    return


def menushka():
    success()
    global font_name
    global all_sprites, drobs, bullets, vaders_group, bosses
    global screen
    pause_snd.play(-1)
    pause_snd.stop()

    menu_sound.play(-1)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-30))

    background4 = pygame.image.load(os.path.join(img_folder, 'background4.png'))
    background4 = pygame.transform.scale(background4, (x, y))
    background4_rect = background4.get_rect()

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']
    for img in background_list:
        if img == 'background1.jpg':
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x+200, y))
            background_images.append(bd)
        else:
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x, y))
            background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    def start():
        def changes():
            btn_start.function = game
        btn_start.change(0, 0, 440)
        btn_start.change(x//2-btn_start.width//2, y - 120, 440, 70, 'Сложный режим')
        btn_option.change(btn_start.rect.x+btn_start.width, y - 120, 440, 70, 'Режим таймера', kill_or_die)
        btn_quit.change(btn_start.rect.x-btn_start.width, y - 120, 440, 70, 'Лёгкий режим', game_without_meteors)
        changes()

    def back():
        btn_quit.change(x // 4, y - 120, 170, 70, 'Выход', super_break)
        btn_start.change(btn_quit.rect.x + btn_quit.width, y - 120, 300, 70, 'Старт', start)
        btn_option.change(btn_quit.rect.x + btn_quit.width + btn_start.width, y - 120, 190, 70, 'Опции', settings)

    vaders_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    bosses = pygame.sprite.Group()

    for i in range(25):
        imp = Imperia()
        all_sprites.add(imp)
        vaders_group.add(imp)

    npc = Npc()

    btn_quit = Buttonpy(x // 4, y - 120, 170, 70, screen, 'Выход', super_break)
    btn_start = Buttonpy(btn_quit.rect.x + btn_quit.width, y - 120, 300, 70, screen, 'Старт', start)
    btn_option = Buttonpy(btn_quit.rect.x + btn_quit.width + btn_start.width, y - 120, 190, 70, screen, 'Опции', settings)

    all_sprites.add(npc)

    all_sprites.add(btn_quit)
    all_sprites.add(btn_start)
    all_sprites.add(btn_option)

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                    return
                if event.key == pygame.K_e:
                    pygame.time.delay(200)
                    back()
                if event.key == pygame.K_q:
                    achievements()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    for i in vaders_group:
                        boom_snd.play()
                        if random.randint(1, 2) == 1:
                            expl = Explosion(i.rect.center, 'lg')
                            all_sprites.add(expl)
                        else:
                            expl = Explosion2(i.rect.center, 'lg')
                            all_sprites.add(expl)
                        i.rect.x = random.randrange(50, x - 70)
                        i.rect.y = random.randrange(-100, -30)
                        i.speedy_imp = random.randrange(speed_enem + count_bosses // 3,
                                                           speed_enem * 3 + count_bosses // 2)
                        i.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3,
                                                           speed_enem + count_bosses // 3)
                        i.rot_speed = random.randrange(-20, 20)
                    boom_snd.play()
                    bullets = pygame.sprite.Group()
                    npc.kill()
                    if random.randint(1, 2) == 1:
                        expl = Explosion(npc.rect.center, 'hu')
                        all_sprites.add(expl)
                    else:
                        expl = Explosion2(npc.rect.center, 'hu')
                        all_sprites.add(expl)
                    npc = Npc()
                    all_sprites.add(npc)

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True, pygame.sprite.collide_circle)
        boom = pygame.sprite.spritecollide(npc, vaders_group, False, pygame.sprite.collide_circle)

        for hit in boom_b:
            boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit.rect.center, 'lg')
                all_sprites.add(expl)
            hit.rect.x = random.randrange(50, x - 70)
            hit.rect.y = random.randrange(-100, -30)
            hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit.rot_speed = random.randrange(-20, 20)

        for hit4 in boom:
            metal.play()
            if random.randint(1, 2) == 1:
                expl = Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = Explosion2(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            hit4.rect.x = random.randrange(50, x - 70)
            hit4.rect.y = random.randrange(-100, -30)
            hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit4.rot_speed = random.randrange(-20, 20)

        if sprites == True:
            screen.blit(background4, background4_rect)
        else:
            screen.blit(random_background, background_rect)

        all_sprites.update()
        all_sprites.draw(screen)

        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x+btn_quit.width//2, btn_quit.rect.y)
        draw_text(screen, btn_start.text, 40, btn_start.rect.x+btn_start.width//2, btn_start.rect.y)
        draw_text(screen, btn_option.text, 40, btn_option.rect.x+btn_option.width//2, btn_option.rect.y)

        draw_text(screen, '"ESC": выход', 20, x-100, 70)
        draw_text(screen, '"E": назад', 20, 100, 70)
        draw_text(screen, '"Q": достижения', 20, 110, 130)

        pygame.display.flip()
        pygame.display.update()
    return


def windows():
    global x, y
    window = Tk()
    x = window.winfo_screenwidth()
    y = window.winfo_screenheight() + 50
    window.destroy()


windows()
menushka()


