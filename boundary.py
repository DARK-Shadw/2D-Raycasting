import pygame

class Boundary:
    
    def __init__(self, x1, y1, x2, y2):
        self.a = pygame.Vector2(x1, y1)
        self.b = pygame.Vector2(x2, y2)
    
    def show(self, screen):
        pygame.draw.line(screen, "red",self.a, self.b, 2)
