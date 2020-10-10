import pygame as p
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


def click(event):
    print(x, y, r)


def score(pos, x, y, r):
    x1 = pos[0]
    y1 = pos[1]
    if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
        return 1
    else:
        return 0


def Random():
    x0 = randint(100, 700)
    y0 = randint(100, 500)
    r0 = randint(30, 50)
    vx0 = randint(-60, 60)
    vy0 = randint(-60, 60)
    color0 = randint(0, 5)
    return ([x0, y0, r0, vx0, vy0, color0])


p.display.update()
clock = p.time.Clock()
finished = False

random = Random()
x = random[0]
y = random[1]
r = random[2]
vx = random[3]
vy = random[4]
color = random[5]

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
            print('Click!')
            click(event)
            c = score(event.pos, x, y, r)
            points += c
            print(points)
            if c == 1:
                random = Random()
                x = random[0]
                y = random[1]
                r = random[2]
                vx = random[3]
                vy = random[4]
                color = random[5]
    if x - r < 0 or x + r > 1200:
        vx *= -1
    if y - r < 0 or y + r > 700:
        vy *= -1
    x += vx * dt
    y += vy * dt
    new_ball(x, y, r, color)
    p.display.update()
    screen.fill(BLACK)

p.quit()
