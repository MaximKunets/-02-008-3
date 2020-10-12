import pygame as p
import numpy as np
from pygame.draw import *
from random import randint

p.init()
FPS = 1000
c = 0
g = 0
end = -1
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


def new_ball(x0, y0, r0, color0):
    col = COLORS[color0]
    circle(screen, col, (int(x0), int(y0)), int(r0))


'''

Функция рисует шар на экране
screen - экран
col - цвет, заданный в формате, подходящем для pygame.color
x0,y0 - координаты центра шара
r0 - радиус шара
COLORS - кортеж цветов
'''


def new_triangle(x0, y0, r0, f0, color0):
    col = COLORS[color0]
    polygon(screen, col, [(int(x0 - r0 * np.sin(f)), int(y0 - r0 * np.cos(f))),
                          (int(x0 + r0 * np.cos(np.pi / 6 - f0)), int(y0 + r0 * np.sin(np.pi / 6 - f0))),
                          (int(x0 - r0 * np.cos(np.pi / 6 + f0)), int(y0 + r0 * np.sin(np.pi / 6 + f0)))])


'''

Функция рисует правильный треугольник на экране
screen - экран
col - цвет, заданный в формате, подходящем для pygame.color
x0,y0 - координаты центра масс треугольника
r0 - длина стороны
COLORS - кортеж цветов
f0 - угол поворота треугольника относительно вертикальной оси 
    (начальное положение - одна вершина сверху, две снизу, основание горизонтально)
'''


def score(pos, x0, y0, r0):
    x1 = pos[0]
    y1 = pos[1]
    if (x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1) <= r0 * r0:
        return 1
    else:
        return 0


'''

Функция определяет попадание по шару и начисляет очки за это
x0,y0 - координаты центра шара
r0 - радиус шара
pos - кортеж координат (непосредственно x1 и y1) клика мыши
'''


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


'''

Функция определяет попадание по треугольнику и начисляет очки за это
x,y - координаты центра масс треугольника
r - длина стороны треугольника
x1, y1, x2, y2, x3, y3 - координаты вершин треугольника
f - поворот треугольника относительно начального положения
'''


def random_():
    x0 = randint(100, 700)
    y0 = randint(100, 500)
    r0 = randint(30, 50)
    vx0 = randint(-120, 120)
    vy0 = randint(-120, 120)
    color0 = randint(0, 5)
    return [x0, y0, r0, vx0, vy0, color0]


'''

Функция задаёт случайные параметры шара и треугольника, которые надо нарисовать
color0 - номер цвета в COLORS
x0,y0 - координаты центра шара или треугольника
r0 - радиус шара или длина стороны треугольника
vx0, vy0 - скорости объекта по осям
'''


def nice_bro():
    rect(screen, YELLOW, (300, 200, 500, 300))
    font1 = p.font.Font(None, 100)
    text1 = font1.render("Nice, bro", True, RED)
    screen.blit(text1, [400, 300])


'''

Функция выводит на экран надпись при попадании по треугольнику
screen - экран
RED, YELLOW - - цвет, заданный в формате, подходящем для pygame.color
'''

p.display.update()
clock = p.time.Clock()
finished = False

balls = []
for i in range(10):
    random = random_()
    x = random[0]
    y = random[1]
    r = random[2]
    vx = random[3]
    vy = random[4]
    color = random[5]
    balls.append([x, y, r, vx, vy, color])

triangles = []
for i in range(4):
    random = random_()
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
    if end > 0:
        end -= 1
        rect(screen, YELLOW, (300, 200, 500, 300))
        font = p.font.Font(None, 50)
        text = font.render("Pleas, enter your name", True, RED)
        screen.blit(text, [370, 300])
        text = font.render("into the command line", True, RED)
        screen.blit(text, [370, 350])
    if end == 0:
        finished = True
    for event in p.event.get():
        if event.type == p.QUIT:
            end = 1000
            print(points)
        elif event.type == p.MOUSEBUTTONDOWN:
            push = 1
            for j in balls:
                c = score(event.pos, j[0], j[1], j[2])
                points += c
                if c == 1:
                    random = random_()
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
                    random = random_()
                    j[0] = random[0]
                    j[1] = random[1]
                    j[2] = random[2]
                    j[3] = random[3]
                    j[4] = random[4]
                    j[5] = random[5]
                    nice_bro()
                    g += 1

    if 100 > g > 0:
        nice_bro()
        g += 1
    else:
        g = 0
    font = p.font.Font(None, 40)

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
file = open('output.txt', 'a')
file.write('\n' + input() + ' : ' + str(points))
file.close()
p.quit()
