# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([200,205,55])
pygame.draw.rect(screen,[250,232,184],[250,150,150,200],100)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()