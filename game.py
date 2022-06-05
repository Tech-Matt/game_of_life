# Conway Game of Life

import pygame
import random
import sys

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
NUM_X_CELLS = SCREEN_WIDTH // CELL_WIDTH; 
NUM_Y_CELLS = SCREEN_HEIGHT // CELL_WIDTH;

MAX_X_POS = NUM_X_CELLS - 1
MAX_Y_POS = NUM_Y_CELLS - 1

#Model parameters
CELL_SPAWN_CHANCE = 90



def neighbours(cells, cell):
    """Give as output the number of neighbours of a cell (only neighbours with the alive attribute = 1)

        cells: List containing all the instances of the initialized cells
        cell: The single instance of cell which will be examined to determine the number of live neighbours

        return: number of live neighbours
    """
    num_neighbours = 0 #Number of near live cells(Moore neighbourhood)
    x = cell.x
    y = cell.y

    #[  List of exceptions before the main algorithm  ]
    #Upper-left corner (x = 0, y = 0)]
    if (x == 0 and y == 0):
        #Cell on the right 
        next_x = 1
        next_y = 0

        num_neighbours += cells[next_x][next_y].alive #Summing the alive attributes of near cells will give me the number of them

        #Cell below current ----------------------------------------
        next_x = 1
        next_y = 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below original cell
        next_x = 0
        next_y = 1

        num_neighbours += cells[next_x][next_y].alive

        #Return the number of neighbours
        return num_neighbours

    #Upper-right corner (x = window, y = 0)!*!*!*!*!**!*!*!*!*!*!*!*!*!*!*!*!*!*!**!*!*!*!*!*!*!*!
    elif (x == MAX_X_POS and y == 0):
        #Cell below -------------------------------------
        next_x = MAX_X_POS
        next_y = 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of current -----------------------------------
        next_x -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of original
        next_y = 0

        num_neighbours += cells[next_x][next_y].alive

        #Return the number of neighbours
        return num_neighbours

    #Lower-left corner (x = 0, y = window) !*!*!*!**!*!!*!**!*!!**!*!*!*!*!*
    elif(x == 0 and y == MAX_Y_POS):

        #Cell over original ----------------------
        next_x = 0
        next_y = MAX_Y_POS - 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current ------------------------------------------
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current ---------------------------------------------
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Return the number of neighbours
        return num_neighbours



    #Lower right corner !*!*!*!*!*!!*!*!*!*!*!*!**!!*!*!*
    elif (x == MAX_X_POS and y == MAX_Y_POS):

        #Cell to the left of original ------------------------------------------------
        next_x = MAX_X_POS - 1
        next_y = MAX_Y_POS

        num_neighbours += cells[next_x][next_y].alive

        #Cell on top of current -------------------------------------------------------
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        #Return the number of neighbours
        return num_neighbours


    #If the cell is in the first row (y = 0) (2 corners excluded) !*!*!*!*!*!!*!!*!*!*!*!
    elif (y == 0 and (x != 0 and x != MAX_X_POS)):
        #Cell to the right of original
        next_x = x + 1
        next_y = 0

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below original
        next_x = x

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of current
        next_x -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of original
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Return the number of neighbours
        return num_neighbours


    #If the cell is in the last row (y = screen_height) 2 corners excluded !*!*!*!*!*!*!*!!*!*
    elif (y == MAX_Y_POS and (x != 0 and x != MAX_X_POS)):
        #Cell to the left of original
        next_x = x - 1
        next_y = y

        num_neighbours += cells[next_x][next_y].alive

        #Cell on top of current
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Return the number of neighbours
        return num_neighbours


    #If the cell is in the first column (2 corners excluded) !*!*!*!*!*!*!*!*!*!*!*!*
    elif (x == 0 and (y != 0 and y != MAX_Y_POS)):
        #Cell on top of original
        next_x = x
        next_y = y - 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of current
        next_x -= 1

        num_neighbours += cells[next_x][next_y].alive


        return num_neighbours


    #If the cell is in the last column (x = screen width) !*!*!*!*!*!*!*!!**!!*
    elif (x == MAX_X_POS and (y != 0 and y != MAX_Y_POS)):
        #Cell below original
        next_x = x
        next_y = y + 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of current
        next_x -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell on top of current
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell on top of current
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        return num_neighbours


    #GENERAL RULE
    else:
        #8 Neighbours
        #Cell on top of original
        next_x = x
        next_y = y - 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the right of current
        next_x += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell below current
        next_y += 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of current
        next_x -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell to the left of current
        next_x -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell on top of current
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        #Cell on top of current
        next_y -= 1

        num_neighbours += cells[next_x][next_y].alive

        return num_neighbours


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

#Cell Initialization
while not init:
    is_alive = random.choices([0,1], weights = (CELL_SPAWN_CHANCE, 1- CELL_SPAWN_CHANCE), k=1)[0]#Randomly spawn cells with probability (Dead 90%, Alive 10 %)
    cell = Cell(x, y, is_alive)#Single object
    cell_array[x][y] = cell

    pygame.draw.rect(screen, cell.color(), pygame.Rect(cell.x, cell.y, cell.size, cell.size))

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
    for i in range(NUM_X_CELLS):
        for j in range(NUM_Y_CELLS):

            #try:
                if neighbours(cell_array, cell_array[i][j]) in (2, 3): #2 or 3 live neighbours (survive)
                    cell_array[i][j].alive = 1
                elif neighbours(cell_array, cell_array[i][j]) < 2: #Few than 2 live neighbours (dies)
                    cell_array[i][j].alive = 0
                elif neighbours(cell_array, cell_array[i][j]) > 3: #More than 3 live neighbours (dies)
                    cell_array[i][j].alive = 0
                elif ((cell_array[i][j].alive == 0) and (neighbours(cell_array, cell_array[i][j]) == 3)): #Dead cell with 3 live neigh (live)
                    cell_array[i][j].alive == 1

            # except Exception as e:
            #     print(e)


    #Debug
    print("Algorithm succesful.")

    #DRAWING CELLS
    for i in range(int(SCREEN_WIDTH / CELL_WIDTH)):
        for j in range(int(SCREEN_HEIGHT / CELL_WIDTH)):
            pygame.draw.rect(screen, cell_array[i][j].color(), pygame.Rect(cell_array[i][j].x, cell_array[i][j].y, cell_array[i][j].size, cell_array[i][j].size))


    #Debug
    print("Cell loaded to the screen")

    screen.fill(WHITE)
    pygame.display.update() #To update the screen
