# Conway Game of Life

import pygame
import random

#Class cell
from cell import *

# PYGAME INITIALIZATION
success, failure = pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Init the screen
pygame.display.set_caption("Game Of Life")
time = pygame.time.Clock()  # Time from startup
FPS = 2

#Number of cells for every row and column
NUM_X_CELLS = SCREEN_WIDTH // CELL_WIDTH
NUM_Y_CELLS = SCREEN_HEIGHT // CELL_WIDTH

MAX_X_POS = NUM_X_CELLS - 1
MAX_Y_POS = NUM_Y_CELLS - 1

#Model parameters
CELL_SPAWN_CHANCE = 5

#CELL INITIALIZATION
cell_array = [] #2D array containing the cells in order[x, y]
x = 0
y = 0
init = False #Become true when initialization is completed

#Array Initialization (X, Y matrix)
for i in range(NUM_X_CELLS):
    cell_array.append([])
    for j in range(NUM_Y_CELLS):
        cell_array[i].append([])

is_alive = random.choices([0,1], weights = ( 100 - CELL_SPAWN_CHANCE, CELL_SPAWN_CHANCE), k=NUM_X_CELLS*NUM_Y_CELLS)#Randomly spawn cells with probability (Dead 90%, Alive 10 %)
#Cell Initialization
while not init:
    cell = Cell(x, y, is_alive[x*y+x])#Single object
    cell_array[x][y] = cell

    pygame.draw.rect(screen, cell.color(), pygame.Rect(cell.x*CELL_WIDTH, cell.y*CELL_WIDTH, cell.size, cell.size))

    x += 1
    if y == (NUM_Y_CELLS - 1) and x == (NUM_X_CELLS):#Last row
        init = True

    if x == (NUM_X_CELLS): #End of a row
        x = 0
        y += 1
    


pygame.display.update() #To update the screen

#Debug
print("Initialization Completed.")


done = False #Check whether the program should run

#Main loop
while not done:

    #FPS
    time.tick(FPS)

    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Exit button
            print("Quitting.")
            done = True



    #SIMULATION --------------------------------------------------------------------
    #Run the algorithm of the game and update the screen (Moore algorithm)
    copy_array = cell_array # This is to prevent new cell changes from affecting calculations
    for i in range(NUM_X_CELLS):
        for j in range(NUM_Y_CELLS):
            cell_neighboors = cell_array[i][j].neighboors(copy_array)
            if cell_array[i][j].alive:
                # Logic for live cells
                if cell_neighboors < 2:
                    cell_array[i][j].alive = 0
                elif cell_neighboors > 3:
                    cell_array[i][j].alive = 0
                # else cell continues to live
            else:
                # Logic for dead cells
                if cell_neighboors == 3:
                    cell_array[i][j].alive = 1
                # else cell stays dead

    #Debug
    print("Algorithm succesful.")

    #DRAWING CELLS
    for i in range(int(SCREEN_WIDTH / CELL_WIDTH)):
        for j in range(int(SCREEN_HEIGHT / CELL_WIDTH)):
            pygame.draw.rect(screen, cell_array[i][j].color(), pygame.Rect(cell_array[i][j].x*CELL_WIDTH, cell_array[i][j].y*CELL_WIDTH, cell_array[i][j].size, cell_array[i][j].size))


    #Debug
    print("Cell loaded to the screen")

    #screen.fill(WHITE) #Overwiting the screen Blank
    pygame.display.update() #To update the screen
