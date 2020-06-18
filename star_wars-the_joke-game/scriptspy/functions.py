import pygame

pygame.init()


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
