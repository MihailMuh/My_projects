import pygame
import math
from scriptspy import loading

pygame.init()
hardmode = False
godmode = False
newgunner = 0
for_file = []


def draw_health_bar_boss(surf, x, y, pct, who=30):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 300
    BAR_HEIGHT = 30
    fill = (pct / who) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, ((255, 0, 0)), fill_rect)
    pygame.draw.rect(surf, ((255, 255, 255)), outline_rect, 2)


def hardgame(games):
    global hardmode
    hardmode = True
    return hardmode, games()


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


def rect_distance(rect1, rect2):
    x1, y1 = rect1.topleft
    x1b, y1b = rect1.bottomright
    x2, y2 = rect2.topleft
    x2b, y2b = rect2.bottomright
    left = x2b < x1
    right = x1b < x2
    top = y2b < y1
    bottom = y1b < y2
    if bottom and left:
        return math.hypot(x2b-x1, y2-y1b)
    elif left and top:
        return math.hypot(x2b-x1, y2b-y1)
    elif top and right:
        return math.hypot(x2-x1b, y2b-y1)
    elif right and bottom:
        return math.hypot(x2-x1b, y2-y1b)
    elif left:
        return x1 - x2b
    elif right:
        return x2 - x1b
    elif top:
        return y1 - y2b
    elif bottom:
        return y2 - y1b
    else:
        return 0.


def newplayer():
    global newgunner
    with open('scriptspy\papers\gunner.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            list = lines[0].split(' ')
            for i in list:
                if i != '':
                    for_file.append(int(i))
        if 2 in for_file:
            newgunner = 2
        elif 1 in for_file:
            newgunner = 1
        elif len(for_file) == 0:
            newgunner = 0
    return newgunner


def spawnsplayer():
    with open('scriptspy\papers\gunner.txt', 'a') as file:
        if (newgunner != 2) and (newgunner != 1) and ((loading.weekday == 'Tuesday') or (loading.weekday == 'Friday')):
            file.write('1 ')


def unlockplayer():
    with open('scriptspy\papers\gunner.txt', 'a') as file:
        file.write('2 ')
