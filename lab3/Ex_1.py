import pygame
from pygame.draw import *
print(23)
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect ( screen, (255,255,255), (0,0,400,400))
circle(screen, (255, 255, 0), (200,200), 150)
circle(screen, (0,0,0), (200,200), 151,1)
circle(screen, (255, 0, 0), (130, 170), 35)
circle(screen, (255, 0, 0), (270, 170), 24)
circle(screen, (0, 0, 0), (130, 170), 36, 1)
circle(screen, (0, 0, 0), (270, 170), 25, 1)
circle(screen, (0,0,0), (130, 170), 10)
circle(screen, (0,0,0), (270, 170), 10)
rect ( screen, (0,0,0), (130,270,140,30))
polygon (screen, (0,0,0), [(170,170),(180,160),(110,90),(100,100)])
polygon (screen, (0,0,0), [(240,170),(230,160),(290,90),(300,100)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()