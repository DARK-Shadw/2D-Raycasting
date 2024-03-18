import pygame
import math
import sys
from ray import Ray
from settings import *

class Particle:

    def __init__(self):
        self.pos = pygame.Vector2((WIDTH/2) + 50 , (HEIGHT/2) + 120)
        self.rays = []
        for r in range(0, 360, 10):
            self.rays.append(Ray(self.pos, math.radians(r)))

    def show(self, screen):
        pygame.draw.circle(screen, "blue", self.pos, 6)

    
    def look(self, screen, walls):

        for ray in self.rays:    
            closest = False
            record = sys.maxsize

            for wall in walls:
                pt = ray.update(wall)
                if(pt):
                    distance = pygame.Vector2.distance_to(self.pos, pt)
                    if(distance < record):
                        record = distance
                        closest = pt

            if(closest):
                pygame.draw.line(screen, "white", self.pos, closest)

    def update(self, pos):
        mousePosVector = pygame.Vector2(pos)
        self.pos  = mousePosVector
        for ray in self.rays:
            ray.setPos(self.pos)
