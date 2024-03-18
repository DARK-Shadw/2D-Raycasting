import pygame
import sys
import random
from settings import *
from boundary import Boundary
from particle import Particle

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    walls = []

    for i in range(5):
        x1 = random.randint(0, WIDTH)
        x2 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        y2 = random.randint(0, HEIGHT)
        walls.append(Boundary(x1, y1, x2, y2))
    particle = Particle()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill("black")
        for wall in walls:
            wall.show(screen)
        particle.show(screen)
        particle.update(pygame.mouse.get_pos())
        particle.look(screen, walls)

        pygame.display.update()
        


if __name__ == '__main__':
    main()
    