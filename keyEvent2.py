import pygame, sys
from pygame.locals import *
    
pygame.init()
displaySurf = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello Pygame World!')
isrunning = True

cat = pygame.image.load("cat.png")
catRect = cat.get_rect()

catRect.centerx=300
catRect.centery=300

vx=1
vy=1

# main game loop
while isrunning:
    displaySurf.fill((125,125,125))
    for event in pygame.event.get():
        if event.type == QUIT:
            isrunning=False
    key = pygame.key.get_pressed()
    if(key[K_UP]):
        catRect.top -= vy
    if(key[K_DOWN]):
        catRect.top += vy
    if(key[K_UP]):
        catRect.top -= vy
    if(key[K_DOWN]):
        catRect.top += vy
    displaySurf.blit(cat,catRect)

    pygame.display.update()
pygame.quit()
sys.exit()

