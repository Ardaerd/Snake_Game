import pygame 
from Cube import Cube

class Snake:
    
    body = []
    turns = {}
    
    # initializing the head of the snake, color and initial movement
    def __init__(self,color,pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dx = 0
        self.dy = 1
        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                    
                elif keys[pygame.K_LEFT]:
                    self.dx = -1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                    
                elif keys[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                    
                elif keys[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.pos[:]] = [self.dx,self.dy]
                    
                for i, c in enumerate(self.body):
                    p = c.pos[:]
                    
                    if p in self.turns:
                        turn = self.turns[p]
                        c.move(turn[0], turn[1])
                        
                        if i == len(self.body)-1:
                            self.turns.pop(p)
