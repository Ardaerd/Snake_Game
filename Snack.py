import pygame


SIZE = 40

class Snack:
    
    def __init__(self, parent_screen):
        self.block = pygame.image.load("snack.png").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3
        
    
    def draw(self):
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
        