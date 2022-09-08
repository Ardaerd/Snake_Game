import pygame

class Snake:
    
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("snake.png").convert()
        self.x = 100
        self.y = 100
        self.direction = "down"
        
    
    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
    def moveUp(self):
        self.y -= 10
        self.draw()
        
    def moveDown(self):
        self.y += 10
        self.draw()
        
    def moveLeft(self):
        self.x -= 10
        self.draw()
        
    def moveRight(self):
        self.x += 10
        self.draw()
    