import pygame
import numpy as np
import sys
from tkinter import *
import os

game_folder = os.path.dirname(__file__)
snd_folder = os.path.join(game_folder, 'sounds')


class Field:
    def __init__(self, screen, rows, cols, left=0, top=0, cell_size=30):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.left = left
        self.top = top
        self.field = [[0] * cols for _ in range(rows)]

    def render(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.field[x][y]:
                    pygame.draw.rect(self.screen, pygame.Color('red'),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size), 0)
                pygame.draw.rect(self.screen, pygame.Color(70, 70, 70),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def on_click(self, cell):
        y, x = cell
        self.field[x][y] = not self.field[x][y]

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x <= self.cols and 0 <= cell_y <= self.rows:
            return cell_y, cell_x

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Life(Field):
    def __init__(self, screen, rows, cols, left=0, top=0, cell_size=30):
        super().__init__(screen, rows, cols, left, top, cell_size)
        self.field = np.zeros((rows, cols), dtype=np.uint8)

    def next_population(self):
        neighbors = sum([
            np.roll(np.roll(self.field, -1, 1), 1, 0),
            np.roll(np.roll(self.field, 1, 1), -1, 0),
            np.roll(np.roll(self.field, 1, 1), 1, 0),
            np.roll(np.roll(self.field, -1, 1), -1, 0),
            np.roll(self.field, 1, 1),
            np.roll(self.field, -1, 1),
            np.roll(self.field, 1, 0),
            np.roll(self.field, -1, 0)
        ])
        self.field = (neighbors == 3) | (self.field & (neighbors == 2))


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


if __name__ == '__main__':
    window = Tk()
    wx = window.winfo_screenwidth()
    wy = window.winfo_screenheight() + 50
    window.destroy()

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(5000)

    pygame.mixer.music.load(os.path.join(snd_folder, 'chill.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((wx, wy - 50), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)

    board = Life(screen, 50, 50, wx//8, 10, 20)

    running = True
    time_on = False
    FPS = 15
    font_name = pygame.font.match_font('Segoe Script')

    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                time_on = not time_on
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                FPS += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                FPS -= 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        screen.fill((0, 0, 0))
        board.render()
        if time_on:
            board.next_population()
        draw_text(screen, 'FPS: '+str(FPS), 25, wx-60, 10)
        pygame.display.flip()

    pygame.quit()