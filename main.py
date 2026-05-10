from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_x, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   ##################################################
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - self.rect.height - 5:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - self.rect.height - 5:
            self.rect.y += self.speed
    ################################################
left_r = Player("racket.png", 250, 50, 3, (30, 150))
right_r = Player("racket.png", 250, 630, 3, (30, 150))
####################################################
ball = GameSprite("tenis_ball.png", 250, 350, 3, (50, 50))
speed_x, speed_y = 2, 2
font.init()
my_font = font.SysFont("Arial", 35)
    ################################################
win_l = my_font.render("Победила левая рекатка!", True, (255, 255, 0))
win_r = my_font.render("Победила правая рекатка!", True, (255, 255, 0))
    ################################################
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')

clock = time.Clock()
FPS = 60
run = True
finish = False

win = my_font.render("Вы победили!", True, (255, 255, 0))
while run:
    window.fill((117, 153, 161))
    ################################################
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
    ################################################
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        #######################################################
        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(left_r, ball) or sprite.collide_rect(right_r, ball):
            speed_x *= -1
    ###############################################
        left_r.reset()
        right_r.reset()
        left_r.update_l()
        right_r.update_r()
    ##################################################
    if ball.rect.x < 0:
      finish = True
      window.blit(win_r, (180, 200))
    if ball.rect.x > 700:
      finish = True
      window.blit(win_l, (180, 200))
    #########################################################3
    display.update() 
    clock.tick(60)
