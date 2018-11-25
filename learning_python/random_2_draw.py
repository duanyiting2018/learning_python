# -*- coding: utf-8 -*-
import pygame,random
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(random.randint(50,100)):
    width=random.randint(0,300)
    height=random.randint(0,200)
    top=random.randint(0,500)
    left=random.randint(0,600)
    pygame.draw.rect(screen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)],[left,top,width,height],random.randint(0,10))
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()