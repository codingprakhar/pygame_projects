import pygame as game
from pygame.locals import *

game.init()

screen = game.display.set_mode((720, 600))
game.display.set_caption("Vectors")

end = False

while not end:
    for event in game.event.get():
        if event.type == QUIT:
            end = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                end = True

    screen.fill("black")
    game.display.update()
