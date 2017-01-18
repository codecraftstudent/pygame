
import pygame
from pygame.locals import *
import random
import time
import sys
from random import randint
from stem_airplane import*




class player(pygame.sprite.Sprite):

    def __init__(self):
        super(player, self).__init__()
        self.image=pygame.image.load('biplane.png').convert()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect()
        
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1,0)

        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>800:
            self.rect.right = 800
        if self.rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=600:
            self.rect.bottom=600


class opponent(pygame.sprite.Sprite):
    #def __init__(self):
      #  super(opponent,self).__init__()
       # self.surf=pygame.Surface((20,10))
      # self.surf.fill((0,255,0))
       # self.rect=self.surf.get_rect(center=(820,random.randint(0,600)))
       # self.speed=random.randint(0,2)
    def __init__(self):
        super(opponent,self).__init__()
        self.image=pygame.image.load('Duck.jpg')
        
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(
            center=(random.randint(850,900),random.randint(0,600))
            )
        self.speed = random.randint(0,2)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()
class meteor(pygame.sprite.Sprite):
    #def __init__(self):
      #  super(opponent,self).__init__()
       # self.surf=pygame.Surface((20,10))
      # self.surf.fill((0,255,0))
       # self.rect=self.surf.get_rect(center=(820,random.randint(0,600)))
       # self.speed=random.randint(0,2)
    def __init__(self):
        super(meteor,self).__init__()
        self.image=pygame.image.load('meteor.png')
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(
            center=(random.randint(850,900),random.randint(0,600))
            )
        self.speed = random.randint(1,9)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()
                        

class Cloud(pygame.sprite.Sprite):
    def __init__(self,color):
        super(Cloud.self). __init__()
        if color=='grey':
            self.image=pygame.image.load('greyCloud.png').convert()
        else:
            slef.image=pygame.image.load('cloud.png').convert()
            self.image.set_colorkey((0,0,0),RLEACCEL)
            self.rect=self.image.get_rect(
                center=(random.randint(820,900),random.randint(0,600))
                )
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.left<0:
            self.kill()
            
class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super(Rain,self).__init__()
        self.image=pygame.image.load('raindrop.png').convert()
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect=self.iamge.get_rect(
            cent=(random.randint(0,800),random.randin(-20.0))
            )

    
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.bottom<900:
            self.kill()
    
        #create level function
def set_level(level):
    caption = 'Airplane - ' + ' Level ' + str(level)
    pygame.display.set_caption(caption)



        

pygame.init()
my_font=pygame.font.SysFont("helvetica",16)
screen=pygame.display.set_mode((800,600))
player = player()
background=pygame.Surface(screen.get_size())
background.fill((0,122,224))

players=pygame.sprite.Group
opponents=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)
ADDOPPONENT=pygame.USEREVENT+1
pygame.time.set_timer(ADDOPPONENT,250)
#surf=pygame.Surface((75,75))
#surf.fill((200,0,1))
#rect=surf.get_rect()
running = True

clock=pygame.time.Clock()
fps=1000
score = 0
while running:
    clock.tick(fps)
    scoretext=my_font.render(str(pygame.time.get_ticks()/3000),1,(0,0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
        elif event.type==QUIT:
            running=False
        elif(event.type==ADDOPPONENT):
            new_opponent=opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
            rnum=randint(0,6)
            if rnum==0:
                new_meteor=meteor()
                opponents.add(new_meteor)
                all_sprites.add(new_meteor)

    screen.blit(background,(0,0))
    screen.blit(scoretext,(5,10))
    pressed_keys=pygame.key.get_pressed()
    player.update(pressed_keys)
    opponents.update()
    #screen.blit(surf,(400,250))
    #screen.blit(player.surf,(400,250))
    #screen.blit(player.surf,player.rect)
    for entity in all_sprites: 
         screen.blit(entity.image, entity.rect)
         
    if pygame.sprite.spritecollideany(player,opponents):
        player.kill()
    pygame.display.flip()


pygame.quit()
