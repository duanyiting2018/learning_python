# -*- coding: utf-8 -*-
import pygame,random
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,imageName,loc,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imageName)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=loc
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.right>screen.get_width():
            self.speed[0]=-self.speed[0]
        if self.rect.top<0:
            self.speed[1]=-self.speed[1]
        if self.rect.bottom>screen.get_height():
            print("你输了！")
            return -1
        return 0
class WackyPadClass(pygame.sprite.Sprite):
    def __init__(self,loc2):
        pygame.sprite.Sprite.__init__(self)
        i_s=pygame.surface.Surface([400,60])
        i_s.fill([random.randint(100,200),random.randint(100,200),random.randint(100,200)])
        self.image=i_s.convert()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=loc2
pygame.init()
screen=pygame.display.set_mode([700,700])
clock=pygame.time.Clock()
ball_s=[8,8]
myball=MyBallClass('wackyball.bmp',[100,100],ball_s)
balgro=pygame.sprite.Group(myball)
pad=WackyPadClass([100,400])
running=True
while running:
    clock.tick(35)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                    pad.rect.left=pad.rect.left-50
            elif event.key==pygame.K_b:
                    pad.rect.right=pad.rect.right+50
    if pygame.sprite.spritecollide(pad,balgro,False):
        myball.speed[1]=-myball.speed[1]
    a=myball.move()
    if a==-1:
        running=False
    else:
        screen.blit(myball.image,myball.rect)
        screen.blit(pad.image,pad.rect)
        pygame.display.flip()
pygame.quit()