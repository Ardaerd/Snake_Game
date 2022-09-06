import pygame 


def drawGrid(w,rows,surface):
    pass

def redrawWindow(surface):
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
        