# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen=pygame.display.set_mode([700,500])
screen.fill([255,255,255])
my_ball=pygame.image.load("beach_ball.png")
screen.blit(my_ball,[60,60])
pygame.display.flip()
x=60
y=60
for i in range(1,100):
    pygame.time.delay(1000)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x+=200
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
#pygame.time.delay(1000)
#pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()