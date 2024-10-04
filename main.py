import pygame as pg
from enemy import Enemy
import Constants as c



pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.screen_width,c.screen_height))
pg.display.set_caption("TDA: Tower Defence Amateur edition")

#load images
enemy_image = pg.image.load("images/Characters/1.png").convert_alpha()


#create groups
enemy_group = pg.sprite.Group()

enemy = Enemy ((200,300), enemy_image)
enemy_group.add(enemy)


#game loop
run = True
while run:
    
    clock.tick(c.FPS)

    screen.fill("grey100")

    #update groups
    enemy_group.update()

    #draw groups
    enemy_group.draw(screen)

    #event handler 
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit



#YOLOOOOOOOOOOOOOOOOOOO