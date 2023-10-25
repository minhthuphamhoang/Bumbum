
import pygame 
import os
import asyncio
from random import randint
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.font.init()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed   
        self.width = width
        self.height = height 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.rect.x < win_width-55:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(self.width,win_width-self.width*3)
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load("space_2-02.png")
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = -self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = -1
         
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = -self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = -self.rectBGimg.height
             
      def render(self):
         window.blit(self.bgimage, (self.bgX1, self.bgY1))
         window.blit(self.bgimage, (self.bgX2, self.bgY2))

win_width = 400
win_height = 700
lost = 0
kill = 0
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Shooter")
back_ground = Background()

background = pygame.image.load("space_2-02.png")
background_image = "space_2-02.png"

trans = pygame.sprite.Group()
trans_bg = Player('702k_rcbl_211015 [Converted]-04.png',0,0,400,700,0)
trans.add(trans_bg)
ufos = pygame.sprite.Group() 
for i in range(1, 6):
    ufo = Enemy('ufo_3.png',randint(0,win_width-50 ),0,50,50,randint(2,4))
    ufos.add(ufo)
bullets = pygame.sprite.Group()
font= pygame.font.Font(None,36)
text = font.render("Score: " + str(kill), 1, (255, 255, 255))
text2 = font.render("Lives: " + str(3-lost), 1, (255, 255, 255))
clock = pygame.time.Clock()
start_image = 'Start 1-02.png'
instruct_image = 'instruction-02.png'
home_image = 'bùm bùm by mint-02.png'

FPS = 60
run = True
finish = False
scroll = 0
count = 1  

async def main():
     
    def char(count):
        global rocket_img
        if count == 1:
            rocket_img = 'rocket_1.png'
        elif count == 2:
            rocket_img = 'rocket_2-02.png'
        else:
            rocket_img ='rocket_3-03.png'
        return rocket_img


    def homescreen():
        global home_image
        global run
        while True:
            window.blit(pygame.image.load(home_image),(0,0))
            for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            run = False
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_RETURN:
                                instruction()
            pygame.display.update()

    def instruction():
        global instruct_image
        global run
        while True:
            window.blit(pygame.image.load(instruct_image),(0,0))
            for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            run = False
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_RETURN:
                                start()
            pygame.display.update()
        
    def start():
        global count
        global start_image
        global run
        while True:
            window.blit(pygame.image.load(start_image),(0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        run = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        play()
                    elif e.key ==pygame. K_LEFT:
                        if count == 1:
                            count = 1
                        else:
                            count -= 1
                    elif e.key == pygame.K_RIGHT:
                        if count == 3:
                            count = 3
                        else:
                            count += 1
            if count == 1:
                start_image = 'Start 1-02.png'
                
            elif count == 2:
                start_image = 'Start 2-02.png'
            else:
                start_image = 'Start 3-02.png'
            window.blit(pygame.image.load(start_image),(0,0))
            pygame.display.update()
            
        return count
    def play():
            global run
            global kill
            global scroll
            global background
            global count
            char(count)
            rocket = Player(rocket_img,175,600,64,51,8)

            while True:
                clock.tick(FPS)
                
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        run = False
                    elif e.type == pygame.KEYDOWN:
                        if e.key ==pygame. K_SPACE:
                            bullet = Bullet('bullet.png',rocket.rect.x, 600, 20, 40 , 15)
                            bullets.add(bullet)
                
                back_ground.update()
                back_ground.render()
                text = font.render("Score: " + str(kill), 1, (255, 255, 255))
                text2 = font.render("Lives: " + str(3-lost), 1, (255, 255, 255))
                
                window.blit(text,(10,20))
                window.blit(text2,(10,50))
                rocket.reset()
                rocket.update()
                ufos.update()
                ufos.draw(window)
                bullets.update()
                bullets.draw(window)
                trans.update()
                trans.draw(window)

                collides = pygame.sprite.groupcollide(ufos, bullets, True, True)
                for c in collides:
                    ufo = Enemy('ufo_3.png',randint(0,win_width-50),0,50,50,randint(2,4))
                    ufos.add(ufo)
                    kill += 1
                if 3 - lost == 0:
                    collidess = pygame.sprite.groupcollide(ufos,trans,True, False)
                    for i in range(1, 6):
                        ufo = Enemy('ufo_3.png',randint(0,win_width-50 ),0,50,50,randint(2,4))
                        ufos.add(ufo)
                    ufos.update()
                    ufos.draw(window)
                    gameover()
                    

                pygame.display.update()
    def gameover():
        global run
        global kill
        global lost
        while True:
            window.blit(pygame.image.load('game over-02.png'),(0,0))
            for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            run = False
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_RETURN:
                                kill = 0
                                lost = 0
                                start()
            text = font.render("Score: " + str(kill), 1, (255, 255, 255))
            window.blit(text,(150,475))
            pygame.display.update()   
        return kill, lost 


        
    homescreen()
    await asyncio.sleep(0)
asyncio.run(main())





    
