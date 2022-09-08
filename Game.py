import pygame
from Snake import Snake


class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        # To change background color of the screen
        self.surface.fill((0, 0, 0))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        
        while running:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                else:
                    
                    pressed = pygame.key.get_pressed()
                    
                    
                    if pressed[pygame.K_DOWN]:
                        self.snake.moveDown()
                        
                    elif pressed[pygame.K_UP]:
                        self.snake.moveUp()
                        
                    elif pressed[pygame.K_LEFT]:
                        self.snake.moveLeft()
                        
                    elif pressed[pygame.K_RIGHT]:
                        self.snake.moveRight()
                        
                    elif pressed[pygame.K_ESCAPE]:
                        running = False 