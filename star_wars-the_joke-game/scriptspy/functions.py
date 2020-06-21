import pygame
import math

pygame.init()
hardmode = False
godmode = False


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
    else:  # rectangles intersect
        return 0.
