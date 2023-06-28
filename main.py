import time

import pygame
import random

pygame.init()
dis = pygame.display.set_mode((1600, 900))
snakelong=[]
snakelen=1
l=True
x=800
y=450
j=0
i=0
x_food=random.randrange(10,1590)
y_food=random.randrange(10,890)
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,100)

def ass(txt,col):
    v=font.render(txt, True, col)
    dis.blit(v,[800,450])

def popa(snakelon):
    for a in snakelon:
        pygame.draw.rect(dis,[196,0,171],[a[0],a[1],10,10])



pygame.display.set_caption("окно")

while l:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            l = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                j=-10
                i=0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                j=+10
                i=0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                j=0
                i=-10
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                j=0
                i=+10
    if x<10 or x>1590 or y<10 or y > 890:
        ass('nigger', [0, 100, 100])
        pygame.display.update()
        time.sleep(0.01)
        l= False
    x+=j
    y+=i
    snakel=[]
    snakel.append(x)
    snakel.append(y)
    snakelong.append(snakel)
    if len(snakelong) >  snakelen:
        del snakelong[0]
    dis.fill([0,0,0])
    pygame.draw.rect(dis,[100,0,0],[x_food,y_food,20,20])

    popa(snakelong)

    if x_food-20<x<x_food+20 and  y_food-20<y<y_food+20 :
        x_food = random.randrange(10, 1590)
        y_food = random.randrange(10, 890)
        snakelen+=1

    pygame.draw.line(dis,[0,0,100],[0,0],[0,900],10)
    pygame.draw.line(dis, [0, 0, 100], [0, 0], [1600,0], 10)
    pygame.draw.line(dis, [0, 0, 100], [0, 900], [1600, 900], 10)
    pygame.draw.line(dis, [0, 0, 100], [1600, 0], [1600, 900], 10)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()