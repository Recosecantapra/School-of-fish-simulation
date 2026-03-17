import pygame
from vector import *
from fish import *
from flock import Flok


# fish_position = Vector(200,200)
# velocity = Vector(6,7)

#fishy = Fish(fish_position, velocity, "fisk.png") 

fishy = Flok(69)

pygame.init()
screen = pygame.display.set_mode((750, 600))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    fishy.update()
    fishy.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()