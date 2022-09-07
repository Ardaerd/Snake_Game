import pygame

class Cube:
    
    rows = 0
    width = 0
    
    def __init__(self, start, dx = 1, dy = 0, color = (255,0,0)):
        self.pos = start
        self.dx = 1
        self.dy = 0
        self.color = color

    
    def move(self, dx, dy):
        pass
    
    def draw(self, surface, eyes=False):
        pass