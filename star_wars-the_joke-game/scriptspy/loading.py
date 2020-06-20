import pygame
import os
from PIL import ImageTk, Image
from scriptspy import system_size

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(5000)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

img_npc = pygame.image.load(os.path.join(img_folder, 'ship.png'))
img_vader4 = pygame.image.load(os.path.join(img_folder, 'vader4.png'))
img_putin = pygame.image.load(os.path.join(img_folder, 'putin.png'))
img_virus = pygame.image.load(os.path.join(img_folder, 'virus.png'))
meteor = pygame.image.load(os.path.join(img_folder, 'meteor.png'))
ful_heart = pygame.image.load(os.path.join(img_folder, 'ful_heart.png'))
half_heart = pygame.image.load(os.path.join(img_folder, 'half_heart.png'))
non_heart = pygame.image.load(os.path.join(img_folder, 'non_heart.png'))
health = pygame.image.load(os.path.join(img_folder, 'health.png'))
fly_sh = pygame.image.load(os.path.join(img_folder, 'buckshot.png'))
button_press = pygame.image.load(os.path.join(img_folder, 'button_press.png'))
button_notpress = pygame.image.load(os.path.join(img_folder, 'button_notpress.png'))
img_death = pygame.image.load(os.path.join(img_folder, 'skull.png'))
img_boss_virus = pygame.image.load(os.path.join(img_folder, 'boss_virus.png'))
boss = pygame.image.load(os.path.join(img_folder, 'boss_1.png'))

laser_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'laser.wav'))
laser_sound.set_volume(0.05)
shotgun_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'shotgun.wav'))
shotgun_sound.set_volume(0.2)
boom_snd = pygame.mixer.Sound(os.path.join(snd_folder, 'boom1.wav'))
boom_snd.set_volume(0.035)
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
img_skull = Image.open(os.path.join(img_folder, 'skull.png'))
img_skull = img_skull.resize((55, 70), Image.ANTIALIAS)
img_skull2 = Image.open(os.path.join(img_folder, 'skull.png'))
img_skull2 = img_skull2.resize((65, 80), Image.ANTIALIAS)
img_ram = Image.open(os.path.join(img_folder, 'ram.jpg'))
img_ram = img_ram.resize((system_size.x, system_size.y), Image.ANTIALIAS)

vader_images = []
vader_list = ['vader.png', 'vader2.png', 'vader3.png']
for img in vader_list:
    vader_images.append(pygame.image.load(os.path.join(img_folder, img)))

reload_sounds = []
reload_list = ['reload0.wav', 'reload1.wav', 'reload2.wav']
for snd in reload_list:
    reload_sounds.append(pygame.mixer.Sound(os.path.join(snd_folder, snd)))
