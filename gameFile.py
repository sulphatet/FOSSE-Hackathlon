import pygame
import time
import random
import math

#Initialize 
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#title
pygame.display.set_caption("Invaders")
icon = pygame.image.load('startup(1).png')
pygame.display.set_icon(icon)

#about the player
playerImg = pygame.image.load('alien.png')
playerX = 370
playerY = 480
print('WELCOME TO INVADERS: ')
print('SPACEBAR to shoot, KEYS to move your ship')
print('Make sure the invaders do not attack the spaceship! If they come too close, YOU LOSE ')
print('Watch out! As time passes, your visibility will be affected.')

enemyImg = []
enemyX = []
enemyY = []
enemyChangeX = []
EnemyNum = 5

for i in range(EnemyNum):
    enemyImg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyChangeX.append(0.3)
    
bulletImg = pygame.image.load('bullet.png')
bulletX = 480
bulletY = 480
bulletChangeX = 0
bulletChangeY = 0.80
bullet_state = "ready"

score = 0

flag = 0
over_font = pygame.font.Font('freesansbold.ttf',64)

def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))

def enemy(enemyX,enemyY,i):
    screen.blit(enemyImg[i],(enemyX,enemyY))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    P = [enemyX,enemyY]
    Q = [bulletX,bulletY]
    dist = math.dist(P,Q)
    if dist < 27:
        return True
    return False

color = 200
playerChangeX = 0

#game loop
running = True
z = 1
x = time.time()
while running:
    screen.fill((color,color,color))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX = -0.3
            if event.key == pygame.K_RIGHT:
                playerChangeX = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                

        if event.type == pygame.KEYUP:
            playerChangeX = 0 
            
    for i in range(EnemyNum):
        if enemyY[i] > 450:
            for j in range(EnemyNum):
                enemyY[j] = 2000
            print("LOST, GAME OVER")
            quit()
        
        enemyX[i] += enemyChangeX[i]
        if enemyX[i] <= 0:
            enemyChangeX[i] = 0.3*z
        if enemyX[i] >= 736:
            enemyChangeX[i] = -0.3*z
            enemyY[i] += 29
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score += 3
            print('Score: ' + str(score))
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
        
    y = time.time()
    
    if(int(y-x) > 5):
        flag +=1
        z += 0.1
        x = y
    
    if flag == 3:
        if color > 50:
            color -= 50
            for i in range(EnemyNum):
                transparency = 128
                enemyImg[i].fill((255,255,255,transparency),special_flags = pygame.BLEND_RGBA_MULT)
        flag = 0

                
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    playerX += playerChangeX

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletChangeY

    player(playerX,playerY)
    pygame.display.update()
    
