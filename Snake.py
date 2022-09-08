import pygame

class Snake:
    
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("snake.png").convert()
        self.x = 100
        self.y = 100
        self.direction = "down"
        
    
    # Snake should keep going according to the last direction
    def walk(self):
        
        if self.direction == "down":
            self.y -= 10
        
        elif self.direction == "up":
            self.y += 10
        
        elif self.direction == "left":
            self.x -= 10
        
        elif self.direction == "right":
            self.x += 10
    
    # Drawing the all screen again in every movement
    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
    # Changing the direction of the snake
    def moveUp(self):
        self.direction = "up"
        
    def moveDown(self):
        self.direction = "down"
        
    def moveLeft(self):
        self.direction = "left"
        
    def moveRight(self):
        self.direction = "right"   
    