import pygame as p
from pygame.draw import *
from random import randint

p.init()
FPS = 2
c = 0
points = 0
screen = p.display.set_mode((1200, 900))

font = p.font.Font(None, 40)
m = 0
n = 0
RED = (255, 0, 0)
white = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r):
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    print(x, y, r)


def score(pos, x, y, r):
    x1 = pos[0]
    y1 = pos[1]
    if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
        return 1
    else:
        return 0


p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    text = font.render("Очки: " + str(points), True, white)
    screen.blit(text, [20, 20])
    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True
            print(points)

        elif event.type == p.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
            points += score(event.pos, x, y, r)
            print(points)
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    new_ball(x, y, r)
    p.display.update()
    screen.fill(BLACK)

p.quit()
