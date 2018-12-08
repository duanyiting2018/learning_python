# -*- coding: utf-8 -*-
import pygame
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,imageName,loc):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imageName)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=loc
size=width,height=(700,700)
screen=pygame.display.set_mode(size)
screen.fill([255,255,255])
imageName="beach_ball.png"
balls=[]
for i in range(4):
    for j in range(4):
            loc=[i*200,j*200]
            ball=MyBallClass(imageName,loc)
            balls.append(ball)
for ball in balls:
    screen.blit(ball.image,ball.rect)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()