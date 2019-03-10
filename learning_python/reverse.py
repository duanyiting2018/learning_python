# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen=pygame.display.set_mode([700,500])
screen.fill([255,255,255])
my_ball=pygame.image.load("beach_ball.png")
x=50
y=50
x_speed=8
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.time.delay(10)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x+=x_speed
    if x>screen.get_width()-90 or x<0:
        x_speed= -x_speed
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
pygame.quit()