# -*- coding: utf-8 -*-
import pygame,math,random
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
point=[]
for x in range(0,640):
    y=int(math.sin(x/640.0*4*math.pi)*200+240)
    point.append([x,y])
    #pygame.draw.rect(screen,[random.randint(0,200),random.randint(0,200),random.randint(0,200)],[x,y,100,100],2)
pygame.draw.lines(screen,[random.randint(0,200),random.randint(0,200),random.randint(0,200)],False,point,5)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()