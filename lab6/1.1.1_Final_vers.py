import pygame as p
import numpy as np
from pygame.draw import *
from random import randint

p.init()
FPS = 1000
c = 0
points = 0
screen = p.display.set_mode((1200, 700))

font = p.font.Font(None, 40)
m = 0
n = 0
f = 0
RED = (255, 0, 0)
white = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r, color):
    col = COLORS[color]
    circle(screen, col, (int(x), int(y)), int(r))


def new_triangle(x, y, r, f, color):
    col = COLORS[color]
    polygon(screen, col, [(int(x - r * np.sin(f)), int(y - r * np.cos(f))),
                          (int(x + r * np.cos(np.pi / 6 - f)), int(y + r * np.sin(np.pi / 6 - f))),
                          (int(x - r * np.cos(np.pi / 6 + f)), int(y + r * np.sin(np.pi / 6 + f)))])


def score(pos, x, y, r):
    x1 = pos[0]
    y1 = pos[1]
    if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
        return 1
    else:
        return 0


def score_tr(pos, x, y, r, f):
    x0 = pos[0]
    y0 = pos[1]
    x1 = int(x - r * np.sin(f))
    y1 = int(y - r * np.cos(f))
    x2 = int(x + r * np.cos(np.pi / 6 - f))
    y2 = int(y + r * np.sin(np.pi / 6 - f))
    x3 = int(x - r * np.cos(np.pi / 6 + f))
    y3 = int(y + r * np.sin(np.pi / 6 + f))
    if (y0 - y3) * (x2 - x3) - (x0 - x3) * (y2 - y3) < 0 and (y0 - y2) * (x1 - x2) - (x0 - x2) * (
            y1 - y2) < 0 and (y0 - y1) * (x3 - x1) - (x0 - x1) * (y3 - y1) < 0:
        return 3
    else:
        return 0


def Random():
    x0 = randint(100, 700)
    y0 = randint(100, 500)
    r0 = randint(30, 50)
    vx0 = randint(-120, 120)
    vy0 = randint(-120, 120)
    color0 = randint(0, 5)
    return ([x0, y0, r0, vx0, vy0, color0])


p.display.update()
clock = p.time.Clock()
finished = False

balls = []
for i in range(10):
    random = Random()
    x = random[0]
    y = random[1]
    r = random[2]
    vx = random[3]
    vy = random[4]
    color = random[5]
    balls.append([x, y, r, vx, vy, color])

triangles = []
for i in range(4):
    random = Random()
    x = random[0]
    y = random[1]
    r = random[2]
    vx = random[3]
    vy = random[4]
    color = random[5]
    triangles.append([x, y, r, vx, vy, color])

while not finished:
    clock.tick(FPS)
    dt = clock.tick(FPS) / 100
    text = font.render("Очки: " + str(points), True, white)
    screen.blit(text, [20, 20])
    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True
            print(points)

        elif event.type == p.MOUSEBUTTONDOWN:
            push = 1
            for j in balls:
                c = score(event.pos, j[0], j[1], j[2])
                points += c
                if c == 1:
                    random = Random()
                    j[0] = random[0]
                    j[1] = random[1]
                    j[2] = random[2]
                    j[3] = random[3]
                    j[4] = random[4]
                    j[5] = random[5]
            for j in triangles:
                c = score_tr(event.pos, j[0], j[1], j[2], f)
                points += c
                if c == 3:
                    random = Random()
                    j[0] = random[0]
                    j[1] = random[1]
                    j[2] = random[2]
                    j[3] = random[3]
                    j[4] = random[4]
                    j[5] = random[5]

    for j in balls:
        if j[0] - j[2] < 0 or j[0] + j[2] > 1200:
            j[3] *= -1
        if j[1] - j[2] < 0 or j[1] + j[2] > 700:
            j[4] *= -1
        j[0] += j[3] * dt
        j[1] += j[4] * dt
        new_ball(j[0], j[1], j[2], j[5])
    for j in triangles:
        R = int(j[2] * np.cos(np.pi / 6) * 2 / 3 + 1)
        if j[0] - R < 0 or j[0] + R > 1200:
            j[3] *= -1
        if j[1] - R < 0 or j[1] + R > 700:
            j[4] *= -1
        j[0] += j[3] * dt
        j[1] += j[4] * dt
        f += np.pi / 300
        new_triangle(j[0], j[1], j[2], f, j[5])
    p.display.update()
    screen.fill(BLACK)
p.quit()
