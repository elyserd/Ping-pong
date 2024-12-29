from pygame import *


class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, hight):
       #вызываем конструктор класса (Sprite):
        super().__init__()


       #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, hight))
        self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


back = (200, 255, 255)
win_width = 600
win_hight = 600
win = display.set_mode((win_width, win_hight))
win.fill(back)

font.init()
font = font.Font(None, 30)
lose1 = font.render('пользователь1 проиграл', True, (180, 0, 0))
lose2 = font.render('пользователь2 проиграл', True, (180, 0, 0))

game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1 
            speed_y *= -1

        if ball.rect.y > win_hight - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            win.blit(lose1,(200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            win.blit(lose2,(200, 200))
            game_over = True
        
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)

        




