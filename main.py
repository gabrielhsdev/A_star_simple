import pygame
from src.pathfinder import Pathfinder
from src.gameState import gameState
from src.display import Display

screenW = 1600
screenH = 800

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()
running = True

rows = 10
cols = 20

map = [[0 for x in range(cols)] for y in range(rows)]
map[3][1] = 1
map[3][2] = 1
map[3][3] = 1
map[3][4] = 1
map[3][5] = 1
map[3][6] = 1
map[3][7] = 1

pathfinder = Pathfinder(rows, cols, screenW, screenH, (0, 0), (5, 5), map)
gameState = gameState(pathfinder, pygame)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    gameState.gameLoop()    
    # END RENDERING
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
