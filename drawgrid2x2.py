import pygame, sys
from pygame.locals import *

screen_width = 600
screen_height = 600
black = (0,0,0)
gray = (128,128,128)
block_width = screen_width//2
block_height = screen_height//2

pygame.init()
displaySurf = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("grid2x2")

running = True
while running:
    displaySurf.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    y_offset=0
    for i in range(2):
        x_offset=0
        for j in range(2):
            pygame.draw.rect(displaySurf,gray,(x_offset,y_offset,block_width,block_height),5)
            x_offset+=block_width
        y_offset+=block_height
    pygame.display.update()
pygame.quit()
sys.exit()
