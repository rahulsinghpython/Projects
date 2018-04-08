import pygame
import sys
import random
import time

check_errors = pygame.init()
score = 0

if check_errors[1] > 0:
    print("(!) had {} initialising errors, exiting".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame sucessfully launched.")

#player surface
playsurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")

#colours
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
brown = pygame.Color(165,42,42)

#FPS
fpsController = pygame.time.Clock()

#snake pos
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

snakeFood = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = "RIGHT"
changeto = direction

#GAME OVER FUNCTIONS
def gameover():
    myfont = pygame.font.SysFont('monaco', 72)
    GOsurf = myfont.render('GAME OVER', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playsurface.blit(GOsurf,GOrect)
    pygame.display.flip()
    showscore(123)
    time.sleep(5)

    pygame.quit() #must exit the game and the console, therefore 2
    sys.exit()

def showscore(choice = 1):
    myfont = pygame.font.SysFont('monaco', 40)
    sSurf = myfont.render('SCORE {}'.format(score), True, black)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (80, 10)
    else:
        sRect.midtop = (360, 100)
    playsurface.blit(sSurf, sRect)
    pygame.display.flip()


#Main Logic
while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is pygame.KEYDOWN:
            if event.key is pygame.K_RIGHT or event.key is ord("d"):
                changeto = "RIGHT"
            if event.key is pygame.K_LEFT or event.key is ord("a"):
                changeto = "LEFT"
            if event.key is pygame.K_UP or event.key is ord("w"):
                changeto = "UP"
            if event.key is pygame.K_DOWN or event.key is ord("s"):
                changeto = "DOWN"
            if event.key is pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    #validation of direction
    if changeto is 'RIGHT' and not direction is 'LEFT':
        direction = 'RIGHT'
    if changeto is 'LEFT' and not direction is 'RIGHT':
        direction = 'LEFT'
    if changeto is 'UP' and not direction is 'DOWN':
        direction = 'UP'
    if changeto is 'DOWN' and not direction is 'UP':
        direction = 'DOWN'


    if direction is "RIGHT":
        snakePos[0] += 10
    if direction is "LEFT":
        snakePos[0] -= 10
    if direction is "UP":
        snakePos[1] -= 10
    if direction is "DOWN":
        snakePos[1] += 10

    #snake body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == snakeFood[0] and snakePos[1] == snakeFood[1]:
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()

    if foodSpawn is False:
        snakeFood = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playsurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playsurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playsurface, brown, pygame.Rect(snakeFood[0], snakeFood[1], 10, 10))


    if snakePos[0] > 710 or snakePos[0] <10:
        gameover()
    if snakePos[1] >450 or snakePos[1] <10:
        gameover()
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameover()

    showscore()
    pygame.display.update()
    fpsController.tick(20)
