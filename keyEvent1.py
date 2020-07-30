import pygame, sys
from pygame.locals import *
    
pygame.init()
displaySurf = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello Pygame World!')
isrunning = True

cat = pygame.image.load("cat.png")
rock = pygame.image.load("Rock.png")
catRect = cat.get_rect()
rockRect = rock.get_rect()

catRect.centerx=300
catRect.centery=300
rockRect.top = 100
rockRect.left = 100


vx=0
vy=0

# main game loop
while isrunning:
    displaySurf.fill((125,125,125))
    for event in pygame.event.get():
        if event.type == QUIT:
            isrunning=False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                vy = -1
            if event.key == K_DOWN:
                vy = 1
            if event.key == K_LEFT:
                vx = -1
            if event.key == K_RIGHT:
                vx = 1
        elif event.type == KEYUP:
            if event.key == K_UP:
                vy = 0
            if event.key == K_DOWN:
                vy = 0
            if event.key == K_LEFT:
                vx = 0
            if event.key == K_RIGHT:
                vx = 0
        if(not catRect.colliderect(rockRect)):
               catRect.left -= vx          
    catRect.top+=vy
    catRect.left+=vx
    
    if(catRect.right>600):
        catRect.right = 600
    if(catRect.left<0):
        catRect.left = 0
    if(catRect.top<0):
        catRect.top = 0
    if(catRect.bottom>600):
        catRect.bottom = 600


    displaySurf.blit(cat,catRect)

    pygame.display.update()
pygame.quit()
sys.exit()
