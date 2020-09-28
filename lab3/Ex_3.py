import pygame
from pygame.draw import *


def bird(a, b, c, m):
    polygon(screen, (35, 13, 33),
            [(a, b), (a + 13 * c, b - 7 * m), (a + 45 * c, b - 4 * m), (a + 16 * c, b - 12 * m), (a, b - 8 * m),
             (a - 15 * c, b - 13 * m), (a - 35 * c, b - 5 * m),
             (a - 14 * c, b - 8 * m)])


def cloud(a, b, c, m):
    ellipse(screen, (175, 218, 252), [a, b, 50 * c, 18 * m])
    ellipse(screen, (175, 218, 252), [a - 30 * c, b + 5 * m, 50 * c, 25 * m])
    ellipse(screen, (175, 218, 252), [a - 70 * c, b + 2 * m, 80 * c, 20 * m])
    ellipse(screen, (175, 218, 252), [a - 35 * c, b - 11 * m, 29 * c, 20 * m])
    ellipse(screen, (175, 218, 252), [a - 10 * c, b - 9 * m, 30 * c, 20 * m])


def cloud_1(a, b, c, m):
    ellipse(s, (175, 218, 252), [a, b, 50 * c, 18 * m])
    ellipse(s, (175, 218, 252), [a - 30 * c, b + 5 * m, 50 * c, 25 * m])
    ellipse(s, (175, 218, 252), [a - 70 * c, b + 2 * m, 80 * c, 20 * m])
    ellipse(s, (175, 218, 252), [a - 35 * c, b - 11 * m, 29 * c, 20 * m])
    ellipse(s, (175, 218, 252), [a - 10 * c, b - 9 * m, 30 * c, 20 * m])


print(23)
pygame.init()

FPS = 30
x = 800
y = 500

screen = pygame.display.set_mode((x, y))
s = pygame.Surface((x, 200))
s.set_colorkey((255, 255, 255))
rect(s, (255, 255, 255), (0, 0, x, 200))
s.set_alpha(120)

rect(screen, (253, 222, 173), (0, 0, x, y))
polygon(screen, (250, 219, 200), [(0, 90), (800, 110), (800, 220), (0, 200)])
circle(screen, (248, 243, 43), (370, 100), 40)

# orange mountains
polygon(screen, (255, 164, 32),
        [(0, 200), (8, 170), (130, 120), (160, 80), (190, 90), (205, 110), (324, 170), (370, 160), (385, 170),
         (420, 140), (445, 148), (463, 133), (513, 120), (557, 80), (617, 120), (647, 110), (707, 140), (737, 94),
         (800, 140)])
ellipse(screen, (250, 219, 200), [-190, -130, 370, 300])
ellipse(screen, (255, 164, 32), [541, 80, 40, 60])
ellipse(screen, (250, 219, 200), [410, 10, 140, 120])
polygon(screen, (253, 222, 173), [(410, 10), (410, 100), (537, 101), (576, 50), (540, 10)])
polygon(screen, (253, 222, 173), [(0, 0), (0, 90), (150, 95), (190, 50), (200, 0)])

cloud(400, 100, 0.7, 0.7)
cloud(200, 20, 1, 1)
cloud_1(500, 50, 0.8, 0.8)
cloud(320, 90, 0.55, 0.55)
screen.blit(s, (0, 0))

# purple mountains
polygon(screen, (140, 69, 102),
        [(110, 320), (160, 240), (205, 270), (230, 210), (290, 220), (335, 260), (435, 249), (500, 195), (625, 255),
         (655, 220), (675, 242), (700, 215), (740, 225), (800, 145), (800, 400)])
ellipse(screen, (140, 69, 102), [415, 193, 160, 320])
ellipse(screen, (140, 69, 102), [10, 174, 120, 230])
ellipse(screen, (140, 69, 102), [-50, 220, 100, 200])

polygon(screen, (139, 102, 139, 255), [(0, 300), (800, 290), (800, y), (0, y)])

# dark purple mountains
polygon(screen, (100, 19, 73),
        [(0, 270), (80, 290), (140, 340), (223, 455), (300, 482), (400, 480), (500, 400), (540, 410), (580, 430),
         (637, 428), (680, 360), (x, y), (0, y)])
ellipse(screen, (139, 102, 139, 255), (200, 350, 250, 133))
ellipse(screen, (100, 19, 73), (650, 280, 300, 400))

bird(350, 200, -0.9, 0.9)
bird(320, 180, 0.6, 0.6)
bird(310, 220, 0.55, 0.55)
bird(590, 380, -1.2, 1.2)
bird(490, 310, 0.85, 0.85)
bird(660, 340, 0.75, 0.75)
bird(520, 340, 0.7, 0.7)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
