import pygame,sys, random
from pygame.locals import*

pygame.init()
displaySurf = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Mr.Meowmer')
isrunning = True

disRect = displaySurf.get_rect()

cat = pygame.image.load("cat_s.png")
bg  = pygame.image.load("grass bg.png")
##ghost = pygame.image.load("ghost.png")
##star = pygame.image.load("Star.png")
##treeShort = pygame.image.load("Tree_Short.png") 
##treeTall = pygame.image.load("Tree_Tall.png")
##finish = pygame.image.load("catgirl.png")

isWin = False
isLose = False
##
##treeShortList = []
##for i in range(random.randint(5,15)):
##    treeShortList.append(treeShort)
##treeShortRectList = []
##for i in range(len(treeShortList)):
##    treeShortRect = treeShortList[i].get_rect()
##    treeShortRect.centerx = random.randint(50,550)
##    treeShortRect.centery = random.randint(50,550)
##    treeShortRectList.append(treeShortRect) 

catRect = cat.get_rect()
catRect.centerx = 20
catRect.centery = 580

bgRect = bg.get_rect()
##
##ghostList = []
##for i in range(random.randint(5,7)):
##    ghostList.append(ghost)
##
##ghostRectList = []
##for i in range(len(ghostList)):
##    ghostRect = ghostList[i].get_rect()
##    ghostRect.centerx = random.randint(50,550)
##    ghostRect.centery = random.randint(50,550)
##    ghostRectList.append(ghostRect)

##starList = []
##for i in range(3):
##    starList.append(star)
##starRectList = []
##for i in range(len(starList)):
##    starRect = starList[i].get_rect()
##    starRect.centerx = random.randint(50,550)
##    starRect.centery = random.randint(50,550)
##    starRectList.append(starRect)
##
##finishRect = finish.get_rect()
##finishRect.centerx = 550
##finishRect.centery = 60

##font = pygame.font.Font('freesansbold.ttf',75)
##finishText = font.render('You Win!', True, (255,0,0))
##finishTextRect = finishText.get_rect()
##finishTextRect.centerx = disRect.width//2
##finishTextRect.centery = disRect.height//2

##loseText = font.render('You Lose!', True, (255,0,0))
##loseTextRect = loseText.get_rect()
##loseTextRect.centerx = disRect.width//2
##loseTextRect.centery = disRect.height//2

speed = 3

vgx = []
vgy = []
i = 0
##while i < len(ghostRectList):
##    vgx.append(random.randint(-speed, speed))
##    vgy.append(random.randint(-speed, speed))
##    if(vgx[i] == 0 and vgy[i] == 0):
##        vgx[i] = 1
##    i += 1

while isrunning:

    vx = 0
    vy = 0

    #close panel
    for event in pygame.event.get():
        if event.type == QUIT:
            isrunning=False
        key = pygame.key.get_pressed()

    #cat move
    if(key[K_w]):
        vy = -speed
    if(key[K_s]):
        vy = speed
    if(key[K_a]):
        vx = -speed
    if(key[K_d]):
        vx = speed
        
    catRect.right += vx
##    #check cat&tree collision x
##    if(catRect.collidelist(treeShortRectList) != -1):
##        catRect.left -= vx
            
    catRect.top += vy
##    #check cat&tree collision y
##    if(catRect.collidelist(treeShortRectList) != -1):
##        catRect.top -= vy

    #ghost loop
    i = 0
##    for ghost in ghostRectList:
##
##        #ghost move x
##        ghost.left += vgx[i]
##        #check ghost&tree collision x
##        if(ghost.collidelist(treeShortRectList) != -1):
##            ghost.left -= vx
##            vgx[i] = random.randint(-speed,speed)
##            vgy[i] = random.randint(-speed,speed)
##            if(vgx[i] == 0 and vgy[i] == 0):
##                vgx[i] = speed
##            
##            
##        #ghost move y
##        ghost.top += vgy[i]
##        #check ghost&tree collision y
##        if(ghost.collidelist(treeShortRectList) != -1):
##            ghost.top -= vy
##            vgx[i] = random.randint(-speed,speed)
##            vgy[i] = random.randint(-speed,speed)
##            if(vgx[i] == 0 and vgy[i] == 0):
##                vgx[i] = speed
##
##        i += 1
            
            
    #check wall collision
    if(catRect.right>600):
        catRect.right = 600
    if(catRect.left<0):
        catRect.left = 0
    if(catRect.top<0):
        catRect.top = 0
    if(catRect.bottom>600):
        catRect.bottom = 600
    i = 0
##    for ghost in ghostRectList:
##        if(ghost.right>600):
##            ghost.right = 600
##            vgx[i] = -vgx[i]
##        if(ghost.left<0):
##            ghost.left = 0
##            vgx[i] = -vgx[i]
##        if(ghost.top<0):
##            ghost.top = 0
##            vgy[i] = -vgy[i]
##        if(ghost.bottom>600):
##            ghost.bottom = 600
##            vgy[i] = -vgy[i]
##        i += 1

##    #check star collision
##    if(catRect.collidelist(starRectList) != -1):
##        starList.pop(catRect.collidelist(starRectList))
##        starRectList.pop(catRect.collidelist(starRectList))

    #add pic to main surface
    displaySurf.blit(bg,bgRect)
    displaySurf.blit(cat,catRect)
##    for i in range(len(treeShortList)):
##        displaySurf.blit(treeShortList[i],treeShortRectList[i])
##    for i in range(len(starList)):
##        displaySurf.blit(starList[i],starRectList[i])
##    for i in range(len(ghostList)):
##        displaySurf.blit(ghostList[i],ghostRectList[i])
##    displaySurf.blit(finish,finishRect)

##    #check ghost cat collision
##    if(catRect.collidelist(ghostRectList) != -1 or isLose):
##        displaySurf.blit(loseText,loseTextRect)
##        isLose = True
##        speed = 0
##        i = 0
##        while i < len(vgx):
##            vgx[i] = vgy[i] = 0
##            i += 1

##    #check finish point collision    
##    if(catRect.colliderect(finishRect) or isWin):
##        if (len(starList)==0):
##            displaySurf.blit(finishText,finishTextRect)
##            isWin = True
##            speed = 0
##            i = 0
##            while i < len(vgx):
##                vgx[i] = vgy[i] = 0
##                i += 1
##            
    
    pygame.display.update()
pygame.quit()
sys.exit()


