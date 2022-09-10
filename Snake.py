import pygame


SIZE = 40

class Snake:
        
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources\snake_down.png").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "down"
        
    
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    
    
    # Snake should keep going according to the last direction
    def walk(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if self.direction == "down":
            self.y[0] += SIZE
        
        elif self.direction == "up":
            self.y[0] -= SIZE
        
        elif self.direction == "left":
            self.x[0] -= SIZE
        
        elif self.direction == "right":
            self.x[0] += SIZE
            
        self.draw()
    
    # Drawing the all screen again in every movement
    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        
    # Changing the direction of the snake
    def moveUp(self):
        self.direction = "up"
        self.block = pygame.image.load("resources\snake_up.png").convert()
        
    def moveDown(self):
        self.direction = "down"
        self.block = pygame.image.load("resources\snake_down.png").convert()
        
    def moveLeft(self):
        self.direction = "left"
        self.block = pygame.image.load("resources\snake_left.png").convert()
        
    def moveRight(self):
        self.direction = "right" 
        self.block = pygame.image.load("resources\snake_right.png").convert()  
    