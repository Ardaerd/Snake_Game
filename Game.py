from operator import is_
from pygame.locals import *
import time
import pygame
from Snake import Snake
from Snack import Snack


SIZE = 60
BACKGROUND_COLOR = (0,0,0)
COLOR_WHITE = (255,255,255)
WIDTH = 1200
HEIGHT = 750


class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((1200, 750))
        # To change background color of the screen
        self.surface.fill(BACKGROUND_COLOR)
        
        # Initializing the snake and drawing it
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        
        # Initializing the snack and drawing it
        self.snack = Snack(self.surface)
        self.snack.draw()
        
        self.clock = pygame.time.Clock()


    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('calibre-bold',40)
        line_1 = font.render(f"Game Over !",True,COLOR_WHITE)
        self.surface.blit(line_1,(500,200))
        
        line_2 = font.render(f"Your Score: {self.snake.length}",True,COLOR_WHITE)
        self.surface.blit(line_2,(500,240))
        
        line_3 = font.render("To Play Again Press Enter. To Exit Press Escape!",True,COLOR_WHITE)
        self.surface.blit(line_3,(270,370))
        
        pygame.display.flip()


    def restart(self):
        self.snake = Snake(self.surface,1)
        self.snack = Snack(self.surface)
    

    def display_score(self):
        font = pygame.font.SysFont('calibre-bold',40)
        score = font.render(f'Score: {self.snake.length}',True,COLOR_WHITE)
        self.surface.blit(score,(1050,10))

    def play(self):
        self.snake.walk()
        self.display_score()
        self.check_borders(self.snake.x[0],self.snake.y[0])
        self.snack.draw()
        
        # Head of the Snake collide with the snack
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.snack.x, self.snack.y):
            sound = pygame.mixer.Sound("resources\yummy.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.snack.move()
            print("snack:", "(", self.snack.x, ",", self.snack.y,")")
            
        # Snake colliding with itself
        for i in range(1, self.snake.length):
            sound = pygame.mixer.Sound("resources\zombie-die-2.wav")
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                pygame.mixer.Sound.play(sound)
                raise "Game over"
        
        # Body parts of the Snake colliding with Snack
        for i in range(1, self.snake.length):
            if self.is_collision(self.snack.x, self.snack.y, self.snake.x[i], self.snake.y[i]):
                self.snack.move()
            
    # Check the collision between head of snakes and snack
    def is_collision(self,x1,y1,x2,y2):
        if x1+24 >= x2 and x1 < x2 + SIZE:
            if y1+24 >= y2 and y1 < y2 + SIZE:
                return True
        
        return False
    
    # Check the snake is crossing the border 
    def check_borders(self,x,y):
        if x >= WIDTH:
            self.snake.x[0] = 0
        if x < 0:
            self.snake.x[0] = WIDTH
            
        if y >= HEIGHT:
            self.snake.y[0] = 0
        if y < 0:
            self.snake.y[0] = HEIGHT
    
    def run(self):
        self.clock.tick(60)
        running = True
        pause = False
        
        while running:
            
            for event in pygame.event.get():
                pygame.event.pump()

                if event.type == pygame.QUIT:
                    pygame.quit()
                
                elif event.type == KEYDOWN:
                    
                    if event.key == K_RETURN:
                        pause = False
                    
                    if event.key == K_ESCAPE:
                        running = False 
                        
                    if not pause:
                    
                        if event.key == K_DOWN:
                            self.snake.moveDown()
                            
                        elif event.key == K_UP:
                            self.snake.moveUp()
                            
                        elif event.key == K_LEFT:
                            self.snake.moveLeft()
                            
                        elif event.key == K_RIGHT:
                            self.snake.moveRight()

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.restart()

            time.sleep(0.2)
        

                