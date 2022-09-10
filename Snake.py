import pygame


SIZE = 40

class Snake:
        
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("snake.png").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "down"
        
    
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
        
    def moveDown(self):
        self.direction = "down"
        
    def moveLeft(self):
        self.direction = "left"
        
    def moveRight(self):
        self.direction = "right"   
    