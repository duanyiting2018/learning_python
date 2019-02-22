# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen=pygame.display.set_mode([600,600])
bg=pygame.Surface(screen.get_size())
bg.fill([255,255,255])
clock=pygame.time.Clock()
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
pygame.time.set_timer(pygame.USEREVENT,100)
dic=1
running=True
while running:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.USEREVENT:
            my_ball.rect.centery=my_ball.rect.centery+(80*dic)
            if my_ball.rect.top<=0 or my_ball.rect.bottom \
            >=screen.get_rect().bottom:
                dic=-dic
    clock.tick(80)
    screen.blit(bg,(0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()
pygame.quit()