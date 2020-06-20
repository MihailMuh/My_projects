import pygame

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