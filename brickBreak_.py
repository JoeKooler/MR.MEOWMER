import pygame,sys
from pygame.locals import *

# object dimensions
screen_width = 640
screen_height = 480

brick_width = 60
brick_height = 15
paddle_width = 60
paddle_height = 12
ball_diameter = 16
ball_radius = ball_diameter // 2

#paddle Y coordinate
paddle_y = screen_height - paddle_height - 10

#color
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
brick_color = (200,200,0)

# state
ball_in_paddle = 0
playing = 1
won = 2
gameover = 3

bricks = []
lives = 3
score = 0
paddle = 0
ball = 0
ball_vel = [5,-5]
state = ball_in_paddle

def setup():
	global lives, score, state, paddle, ball, ball_vel
	lives = 3
	score = 0
	state = ball_in_paddle
	paddle = pygame.Rect(300, paddle_y, paddle_width, paddle_height)
	ball = pygame.Rect(0, 0, ball_diameter,ball_diameter)
	ball.centerx = paddle.centerx
	ball.bottom = paddle.top
	ball_vel = [5,-5]
	createBricks()
        
def createBricks():
	global bricks
	bricks = []
	y_offset = 35
	for i in range(7):
		x_offset = 60
		for j in range(8):
			bricks.append(pygame.Rect(x_offset,y_offset,brick_width,brick_height))
			x_offset += brick_width+5
		y_offset += brick_height+5

def drawBrick():
        for brick in bricks:
                pygame.draw.rect(displaySurf,brick_color,brick)

def showScoreAndLive():
        textSurf = font.render("SCORE: " + str(score) + " LIVES: " + str(lives),True,white)
        textRect = textSurf.get_rect()
        textRect.centerx = screen_width//2
        textRect.top = 5
        displaySurf.blit(textSurf,textRect)

def showMessage(message):
        textSurf = font.render(message, True, white)
        textRect = textSurf.get_rect()
        textRect.centerx = screen_width//2
        textRect.centery = screen_height//2
        displaySurf.blit(textSurf,textRect)

def checkInput():
        global state,paddle,ball_vel
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
                paddle.left -= 7
                if paddle.left < 0:
                        paddle.left = 0
        if key[K_RIGHT]:
                paddle.left += 7
                if paddle.right > screen_width:
                        paddle.right = screen_width
        if key[K_SPACE] and state == ball_in_paddle:
                ball_vel = [5, -5]
                state = playing
        if key[K_RETURN] and (state == gameover or state == won):
                setup()

def moveBall():
        global ball
        ball = ball.move(ball_vel)
        if ball.left <= 0:
                ball.left = 0
                ball_vel[0] = -ball_vel[0]
        if ball.right >= screen_width:
                ball.right = screen_width
                ball_vel[0] = -ball_vel[0]
        if ball.top <= 0:
                ball.top = 0
                ball_vel[1] = -ball_vel[1]
        if ball.bottom >= screen_height:
                ball.bottom = screen_height
                ball_vel[1] = -ball_vel[1]

def handleCollision():
        global score,ball_vel,state,lives
        index = ball.collidelist(bricks)
        if index!=-1:
                brick = bricks[index]
                score+=3
                if ball.centerx > brick.left and ball.centerx < brick.right:
                        ball_vel[1] = -ball_vel[1]
                else:
                        ball_vel[0] = -ball_vel[0]
                bricks.remove(bricks[index])
        if len(bricks)==0:
                state = won
        if ball.colliderect(paddle):
                ball.bottom = paddle.top
                ball_vel[1] = -ball_vel[1]
        elif ball.top > paddle.top:
                lives -= 1
                if lives > 0:
                        state = ball_in_paddle
                else:
                        state = gameover
               
pygame.init()
displaySurf = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("brick break!!")
font = pygame.font.Font("freesansbold.ttf",24) 
setup()
running = True
while running:
        for event in pygame.event.get():
                if event.type == QUIT:
                        running = False
        checkInput()
        displaySurf.fill(black)
        if state == playing:
                moveBall()
                handleCollision()
        elif state == ball_in_paddle:
                ball.centerx = paddle.centerx
                ball.bottom = paddle.top
                showMessage("PRESS SPACE TO LAUNCH THE BALL")
        elif state == gameover:
                showMessage("GAME OVER. PRESS ENTER TO PLAY AGAIN")
        elif state == won:
                showMessage("YOU WON! PRESS ENTER TO PLAY AGAIN")
 
        #draw brick
        drawBrick()
        #draw paddle
        pygame.draw.rect(displaySurf, blue, paddle)
        #draw ball
        pygame.draw.circle(displaySurf, white, (ball.centerx,ball.centery),ball_radius)
        #draw score and lives
        showScoreAndLive()
        pygame.time.delay(20)
        pygame.display.update()
pygame.quit()
