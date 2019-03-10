# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen=pygame.display.set_mode([600,600])
bg=pygame.Surface(screen.get_size())
bg.fill([255,255,255])
clock=pygame.time.Clock()
d=100
i=50
pygame.key.set_repeat(d,i)
class Ball(pygame.sprite.Sprite):
    def __init__(self,imageName,speed,loc):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imageName)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=loc
        self.speed=speed
    def move(self):
        if self.rect.left<=screen.get_rect().left or self.rect.right>=screen.get_rect().right:
            self.speed[0]=-self.speed[0]
        np=self.rect.move(self.speed)
        self.rect=np
my_ball=Ball('beach_ball.png',[10,0],[20,20])
held_down=False
running=True
while running:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            held_down=True
        elif event.type==pygame.MOUSEBUTTONUP:
            held_down=False
        elif event.type==pygame.MOUSEMOTION:
            #DO STH
            if held_down:
                my_ball.rect.center=event.pos
    clock.tick(60)
    screen.blit(bg,(0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()
pygame.quit()   