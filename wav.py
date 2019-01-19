# -*- coding: utf-8 -*-
import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([640,480])
#pygame.time.delay(1000)
sp=pygame.mixer.Sound("splat.wav")
sp.set_volume(0.1)
sp.play()
pygame.time.delay(2000)
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()