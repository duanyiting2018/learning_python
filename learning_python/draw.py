# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen=pygame.display.set_mode([700,500])
screen.fill([55,205,155])
pygame.draw.circle(screen,[255,245,250],[300,300],50,50)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()