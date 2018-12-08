# -*- coding: utf-8 -*-
import pygame
from random import choice
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,imageName,loc,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imageName)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=loc
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.right>width:
            self.speed[0]=-self.speed[0]
        if self.rect.top<0 or self.rect.bottom>height:
            self.speed[1]=-self.speed[1]
size=width,height=(700,700)
screen=pygame.display.set_mode(size)
screen.fill([255,255,255])
imageName="beach_ball.png"
balls=[]
for i in range(4):
    for j in range(4):
            loc=[i*200,j*200]
            speed=[choice([-2,2]),choice([-2,2])]
            ball=MyBallClass(imageName,loc,speed)
            balls.append(ball)
running=True
while running:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill([255,255,255])
    for ball in balls:
        ball.move()
        screen.blit(ball.image,ball.rect)
    pygame.display.flip()
pygame.quit()