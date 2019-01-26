# -*- coding: utf-8 -*-
import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([640,480])
pygame.time.delay(1000)
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()
sp=pygame.mixer.Sound("splat.wav")
sp.set_volume(0.50)
#sp.play()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if not pygame.mixer.music.get_busy():
        sp.play()
        pygame.time.delay(1000)
        running=False
pygame.quit()