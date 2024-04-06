from pygame import *

class GameSprite():
    def __init__(self, img, speed, x, y):
        self.img = transform.scale(image.load(img), (50,50))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"

    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))
    

class Hero(GameSprite):
    def move(self):
        keys = key.get_pressed()
       
        if keys[K_d]:
            if self.rect.x < 640:

                self.rect.x += self.speed 
        if keys[K_a]:
            if self.rect.x > 5:
                self.rect.x -= self.speed
        if keys[K_w]:
            if self.rect.y > 5:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y < 440:

                self.rect.y += self.speed


class Enemy(GameSprite):
    def move(self, start, end):
        if self.direction == "right":
            self.rect.x += 5
        if self.direction == "left":
            self.rect.x -= 5
        if self.rect.x >= end:
            self.direction = "left"
        if self.rect.x <= start:
            self.direction = "right"


class Wall():
    def __init__(self, x, y, width, height):
        self.img = Surface((width, height))
        self.img.fill((10, 248, 252))

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


window = display.set_mode((1000, 700))

mixer.init()
mixer.music.load('jungles.ogg')
# mixer.music.play()

kick = mixer.Sound('kick.ogg')

background = transform.scale(image.load('background.jpg'), (1000,700))

game = True
clock = time.Clock()

hero = Hero("hero.png", 5, 25, 25)
enemy = Enemy("cyborg.png", 10, 50, 50)



walls = [ 
         Wall(0, 0, 400, 10),
         Wall(0, 80, 200, 10),
         Wall(270, 60, 200, 10),
         Wall(0, 120, 10, 400),
         ]
map  = '''
11111111111111111111111111111111111111113
10010000000000010000000000000000000000013
10010000000000010000000000000000000000013
10010011111110010000000000000000000000013
10000010010000000000000000000000000000013
10000010010000000000000000000000000000013
11111110010010010000000000000000000000013
10000000000010010000000000000000000000013
10000000000010000000000000000000000000013
10000001111110000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
10000000000000000000000000000000000000013
11111111111111111111111111111111111111113

'''


while game:

    window.blit(background, (0,0))
    hero.reset()
    hero.move()
    enemy.reset()
    enemy.move(0, 700)

    # for wall in walls:
    #     wall.draw()
    wall_x = -25
    wall_y = 0

    for i in map:

        if i == '1':
            wall = Wall(wall_x, wall_y, 25, 25)
            wall.draw()
            if(hero.rect.colliderect(wall.rect)):
                hero.rect.x = 25
                hero.rect.y = 25


        wall_x += 25

        if i == '3':
            wall_y += 25
            wall_x = -25
        


    for e in event.get():
        if e.type == QUIT:
            game = False
        

    display.update()
    clock.tick(60)