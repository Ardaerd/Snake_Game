import time
import pygame
from Snake import Snake
from Snack import Snack


SIZE = 40

class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((800, 600))
        # To change background color of the screen
        self.surface.fill((0, 0, 0))
        
        # Initializing the snake and drawing it
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        
        # Initializing the snack and drawing it
        self.snack = Snack(self.surface)
        self.snack.draw()
        
        #self.clock = pygame.time.Clock()


    def display_score(self):
        font = pygame.font.SysFont('calibre-bold',40)
        score = font.render(f'Score: {self.snake.length}',True,(255,255,255))
        self.surface.blit(score,(650,10))

    def play(self):
        self.snake.walk()
        self.display_score()
        self.snack.draw()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.snack.x, self.snack.y):
            print("snack:", "(", self.snack.x, ",", self.snack.y,")")
            
    # Check the collision between head of snakes and snack
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                self.snake.increase_length()
                self.snack.move()
                return True
        
        return False
    
    
    def run(self):
        #self.clock.tick(5)
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
        

                