import time
import pygame
from Snake import Snake
from Snack import Snack


class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 600))
        # To change background color of the screen
        self.surface.fill((0, 0, 0))
        self.snake = Snake(self.surface,6)
        self.snake.draw()
        self.snack = Snack(self.surface)
        self.snack.draw()
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.time.delay(50)
        self.clock.tick(5)
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
  
            self.play()
            time.sleep(0.2)
        
    def play(self):
            self.snake.walk()
            self.snack.draw()
                