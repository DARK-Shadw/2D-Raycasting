import pygame
import math

class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = pygame.Vector2(math.cos(angle), math.sin(angle))

    def setPos(self, pos):
        self.pos = pos

    
    def show(self, screen):
        end = self.pos + (self.dir * 10)
        pygame.draw.line(screen, "blue", self.pos, end, 2)

    def lookat(self, mouse):
        mouseX, mouseY = mouse
        self.dir.x = mouseX - self.pos.x
        self.dir.y = mouseY - self.pos.y
        self.dir = self.dir.normalize()

    def update(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y
        

        den = (x1 - x2) * (y3 - y4) - (y1 -y2) * (x3 - x4)
        
        if(den == 0):
            return
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))/ den
        u =  -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))/den
        
        if(t > 0 and t < 1 and u > 0):
            pt = pygame.Vector2()
            pt.x = (x1 + t * (x2 - x1))
            pt.y = (y1 + t * (y2 - y1))
            return pt
        else:
            return


        