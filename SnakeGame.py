import pygame
from pygame.locals import *


def drawBlock():
    pass


if __name__ == '__main__':
    pygame.init()
    
    surface = pygame.display.set_mode((500,500))
    # To change background color of the screen
    #surface.fill((22, 33, 62))
    
    block = pygame.image.load("snake.png").convert()
    
    block_x = 100
    block_y = 100
    
    surface.blit(block, (block_x, block_y))

    pygame.display.flip()
    
    running = True
    
    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            
            else:
                pressed = pygame.key.get_pressed()
                
                if pressed[pygame.K_DOWN]:
                    block_y += 10
                    drawBlock()
                    
                elif pressed[pygame.K_UP]:
                    block_y -= 10
                    drawBlock()
                    
                elif pressed[pygame.K_LEFT]:
                    block_x -= 10
                    drawBlock()
                    
                elif pressed[pygame.K_RIGHT]:
                    block_x += 10
                    drawBlock()
                elif pressed[pygame.K_ESCAPE]:
                    running = False