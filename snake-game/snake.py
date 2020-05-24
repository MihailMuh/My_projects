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

x = 1280
y = 680
FPS = 20
snake = []
filename = 'score_snake.txt'
score = 0


white = ((255, 255, 255))
blue = ((0, 0, 255))
green = ((0, 255, 0))
red = ((255, 0, 0))
black = ((0, 0, 0))
orange = ((255, 100, 10))
yellow = ((255, 255, 0))

font_name = pygame.font.match_font('Arial')


class Head():
    def __init__(self):
        self.snake_body = [[400, 200], [370, 200], [340, 200], [310, 200], [280, 200], [250, 200], [220, 200]]
        self.head = [400, 200]
        self.direction = 'RIGHT'

    def update(self, surface):
        self.boom()
        if self.direction == 'DOWN':
            self.head[1] += 30
        if self.direction == 'UP':
            self.head[1] -= 30
        if self.direction == 'LEFT':
            self.head[0] -= 30
        if self.direction == 'RIGHT':
            self.head[0] += 30

        self.snake_body.insert(0, list(self.head))
        self.snake_body.pop()

        for i in range(len(self.snake_body)):
            if self.snake_body[i] == self.head:
                pygame.draw.rect(surface, red, pygame.Rect(self.snake_body[i][0], self.snake_body[i][1], 25, 25))
            else:
                pygame.draw.rect(surface, green, pygame.Rect(self.snake_body[i][0], self.snake_body[i][1], 25, 25))

    def right(self):
        if self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def left(self):
        if self.direction != 'RIGHT':
            self.direction = 'LEFT'

    def up(self):
        if self.direction != 'DOWN':
            self.direction = 'UP'

    def down(self):
        if self.direction != 'UP':
            self.direction = 'DOWN'

    def boom(self):
        if self.head[0] >= x - 65:
            score_file = open(filename, 'w')
            score_file.write(str(max(score, max_score)))
            score_file.close()
            sys.exit()
        if self.head[0] <= 35:
            score_file = open(filename, 'w')
            score_file.write(str(max(score, max_score)))
            score_file.close()
            sys.exit()
        if self.head[1] >= y - 65:
            score_file = open(filename, 'w')
            score_file.write(str(max(score, max_score)))
            score_file.close()
            sys.exit()
        if self.head[1] <= 45:
            score_file = open(filename, 'w')
            score_file.write(str(max(score, max_score)))
            score_file.close()
            sys.exit()
        for i in self.snake_body[1:]:
            if (i[0] == self.head[0]) and (i[1] == self.head[1]):
                score_file = open(filename, 'w')
                score_file.write(str(max(score, max_score)))
                score_file.close()
                sys.exit()

    def grow(self):
        self.snake_body.append([self.snake_body[-1][0], self.snake_body[-1][1]])


class Food():
    def __init__(self):
        self.placement = [random.randrange(40, x - 85, 30), random.randrange(50, y - 89, 30)]

    def update(self, surface):
        pygame.draw.rect(surface, yellow, pygame.Rect(self.placement[0], self.placement[1], 25, 25))

    def rollback(self):
        self.placement = [random.randrange(40, x - 85, 30), random.randrange(50, y - 89, 30)]


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def trying():
    try:
        with open('score_snake.txt', 'a+') as f:
            if os.stat('score_snake.txt').st_size == 0:
                f.write('0')
    except FileNotFoundError:
        print('файла не существует')


trying()
score_file = open(filename, 'r')
max_score = int(score_file.read())
score_file.close()


def game():
    global score
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    snake = Head()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score_file = open(filename, 'w')
                score_file.write(str(max(score, max_score)))
                score_file.close()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    score_file = open(filename, 'w')
                    score_file.write(str(max(score, max_score)))
                    score_file.close()
                    return
                if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                    snake.up()
                if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                    snake.down()
                if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                    snake.left()
                if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                    snake.right()

        screen.fill(black)
        pygame.draw.rect(screen, blue, (30, 40, x-65, y-79), 10)
        snake.update(screen)
        food.update(screen)
        if (snake.head[0] == food.placement[0]) and (snake.head[1] == food.placement[1]):
            food.rollback()
            snake.grow()
            score += 1
        draw_text(screen, 'score: ' + str(score), 35, 200, 100)
        draw_text(screen, 'MAX score: ' + str(max_score), 35, x - 200, 100)
        if score <= 10:
            time.sleep(0.1 - score / 100)
            clock.tick(FPS)
        else:
            clock.tick(FPS + (score // 10) * 2)
        pygame.display.flip()


def windows():
    global x, y
    window = Tk()
    x = window.winfo_screenwidth()
    y = window.winfo_screenheight()
    window.destroy()


windows()
game()
