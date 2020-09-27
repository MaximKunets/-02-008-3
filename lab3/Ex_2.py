import pygame
from pygame.draw import *

print(23)
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 400))

rect(screen, (253, 222, 173), (0, 0, 800, 400))
polygon(screen, (250, 219, 200), [(0, 90), (800, 110), (800, 220), (0, 200)])
circle(screen, (248, 243, 43), (370, 100), 40)

polygon(screen, (255, 164, 32),
        [(0, 200), (8, 170), (130, 120), (160, 80), (190, 90), (205, 110), (324, 170), (370, 160), (385, 170),
         (420, 140), (445, 148), (463, 133), (513, 120), (557, 80), (617, 120), (647, 110), (707, 140), (737, 94),
         (800, 140)])
ellipse(screen, (250, 219, 200), [-190, -130, 370, 300])
ellipse(screen, (255, 164, 32), [541, 80, 40, 60])
ellipse(screen, (250, 219, 200), [410, 10, 140, 120])
polygon(screen, (253, 222, 173), [(410, 10), (410, 100), (537, 101), (576, 50), (540, 10)])
polygon(screen, (253, 222, 173), [(0, 0), (0, 90), (150, 95), (190, 50), (200, 0)])
ellipse(screen, (140, 69, 102), [10, 174, 120, 230])
ellipse(screen, (140, 69, 102), [-50, 220, 100, 200])

polygon(screen, (140, 69, 102),
        [(110, 320), (160, 240), (205, 270), (230, 210), (290, 220), (335, 260), (435, 249), (500, 195), (625, 255),
         (655, 220), (675, 242), (700, 215), (740, 225), (800, 145), (800, 400)])
ellipse(screen, (140, 69, 102), [415, 193, 160, 320])
polygon(screen, (139, 102, 139, 255), [(0, 300), (800, 290), (800, 400), (0, 400)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
