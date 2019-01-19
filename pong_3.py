# -*- coding: utf-8 -*-
import pygame,random
lives=random.randint(1,5)
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,imageName,loc,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imageName)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=loc
        self.speed=speed
    def move(self):
        global score,font,surf
        self.rect=self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.right>screen.get_width():
            self.speed[0]=-self.speed[0]
        if self.rect.top<=0:
            self.speed[1]=-self.speed[1]
            score+=1
            surf=font.render(str(score),1,(random.randint(100,200),random.randint(100,200),random.randint(100,200)))
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
a=random.randint(1,10)
ball_s=[a,a]
myball=MyBallClass('wackyball.bmp',[100,100],ball_s)
balgro=pygame.sprite.Group(myball)
pad=WackyPadClass([100,400])
score=0
font=pygame.font.Font(None,50)
surf=font.render(str(score),1,(random.randint(100,200),random.randint(100,200),random.randint(100,200)))
pos=[10,10]
done=False
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
        myball.speed[1]=-5
    myball.move()
    if not done:
        screen.blit(myball.image,myball.rect)
        screen.blit(pad.image,pad.rect)
        screen.blit(surf,pos)
        for i in range(lives):
            width=screen.get_rect().width
            screen.blit(myball.image,[width-40*i,20])
        pygame.display.flip()
    if myball.rect.top>=screen.get_rect().bottom:
        lives-=1
        if lives==0:
            text1="GAME OVER"
            text2="YOUR SCORE:"+str(score)
            font1=pygame.font.Font(None,70)
            surf1=font1.render(text1,1,(0,0,0))
            font2=pygame.font.Font(None,50)
            ft2=font2.render(text2,1,(0,0,0))
            screen.blit(surf1,[screen.get_width()/2 - \
                        surf1.get_width()/2,100])
            screen.blit(ft2,[screen.get_width()/2 - \
                        ft2.get_width()/2,400])
            pygame.display.flip()
            done=True
        else:
            pygame.time.delay(1000)
            myball.rect.topleft=[50,50]
pygame.quit()