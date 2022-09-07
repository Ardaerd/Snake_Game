import pygame

class Cube:
    
    rows = 20
    width = 500
    
    def __init__(self, start, dx = 1, dy = 0, color = (255,0,0)):
        self.pos = start
        self.dx = 1
        self.dy = 0
        self.color = color

    
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.pos(self.pos[0] + self.dx, self.pos[1] + self.dy)
        
    
    def draw(self, surface, eyes=False):
        dis = self.width // self.row
        
        i = self.pos[0]
        j = self.pos[1]
        
        pygame.draw.rect(surface, self.color, i*dis + 1, j*dis + 1, dis-2, dis-2)
        
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+1,j*dis+1,dis-2,dis-2)
            circleMiddle2 = (i*dis+dis - radius*2,j*dis+8)
            pygame.draw.circle(surface, (0,0,0),circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0),circleMiddle2, radius)
        
        