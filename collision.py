import pygame, sys
from pygame.locals import *

pygame.init()
displaySurf = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Pygame World!')
isrunning = True

cat = pygame.image.load("cat.png")
rock = pygame.image.load("Rock.png")
catRect = cat.get_rect()
rockRect = rock.get_rect()

catRect.top = 80
catRect.left = 420
rockRect.top = 100
rockRect.left = 100

vx=1
vy=0

# main game loop
while isrunning:
    displaySurf.fill((125,125,125))
    for event in pygame.event.get():
        if event.type == QUIT:
            isrunning = False
       
    font = pygame.font.Font("freesansbold.ttf",50)
    textSurf = font.render('My Text',True,(255,0,0))

    # catRect.top += vy
    # catRect.left += vx

    if(not catRect.colliderect(rockRect)):
        catRect.left -= vx
    """
    if(catRect.right == 400):
        vx=0
        vy=1
    if(catRect.bottom == 300):
        vx=0
        vy=0
    """
    displaySurf.blit(cat,catRect)
    displaySurf.blit(rock,rockRect)

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
sys.exit()
