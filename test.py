import pygame, sys
from pygame.locals import *

pygame.init()
displaySurf = pygame.display.set_mode((800,600))
pygame.display.set_caption('Meow')
running = True
cat = pygame.image.load("cat.png")
catrect = cat.get_rect()
catrect.left = 0
catrect.top = 0
vx = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    displaySurf.fill((125,125,125))
    if(catrect.right>800 or catrect.left<0):
        vx = (-1) * vx
    #load image
    catrect.left += vx
    displaySurf.blit(cat,(catrect.left, catrect.top))
    pygame.time.delay(10)
    pygame.display.update()
pygame.quit()
sys.exit()
