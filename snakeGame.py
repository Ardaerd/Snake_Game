import pygame 


def drawGrid(width,rows,surface):
    size = width // rows  # cells size
    
    # initial coordinates
    x = 0
    y = 0
    
    for i in range(rows):
        x = x + size
        y = y + size
        
        pygame.draw.line(surface, (255,255,255), (x,0), (x,height))
        pygame.draw.line(surface, (255,255,255), (0,y), (width,y))
    

def redrawWindow(surface):
    global rows,width
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()


def randomSnack(rows,item):
    pass

def message_box(subject,content):
    pass

def main():
    global width, height, rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

main()