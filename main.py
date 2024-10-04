import pygame as pg
import json
from enemy import Enemy
from world import World
import Constants as c



pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.screen_width,c.screen_height))
pg.display.set_caption("TDA: Tower Defence Amateur edition")

#load images
# map
map_image = pg.image.load("levels/wmap.png").convert_alpha()
# enemy's
enemy_image = pg.image.load("images/Characters/1.png").convert_alpha()

new_width = 100 
new_height = 100 

enemy_image_resized = pg.transform.scale(enemy_image, (new_width, new_height))

# json
with open("levels/wmap.tmj") as file:
    world_data = json.load(file)

# create world
world = World(world_data, map_image)
world.process_data()

#create groups
enemy_group = pg.sprite.Group()
enemy = Enemy (world.paths, enemy_image_resized)
enemy_group.add(enemy)


#game loop
run = True
while run:
    
    clock.tick(c.FPS)

    screen.fill("grey100")

    # draw world
    world.draw(screen)

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



