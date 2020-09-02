# Conway Game of Life

import pygame
import random
import sys

#Class cell
from cell import *

# PYGAME INITIALIZATION
success, failure = pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))  # Init the screen
time = pygame.time.Clock()  # Time from startup
FPS = 5

# Screen Area = 480000 px (width * height)
# Area of a cell = 1600px --> 300 Cell
#Each cell: 40px * 40px


#Function needed in the next function ------------------------------------------------
def checkAlive(cell, cellArray, curr_x, curr_y):
    """ Check wheter the current cell near the original cell is alive. If it is alive it returns 1
        else returns 0
        cell: instance of the original cell
        cellArray: cell list with all the initialized cells
        curr_x: x coordinate of the cell which will be examined
        curr_y: y coordinate of the cell which will be examined
    """

    for current_cell in cellArray:
        if (current_cell.x == curr_x and current_cell.y == curr_y):
            if (current_cell.alive == 1):
                return 1
            else:
                return 0
    #If there is some problem
    return 0


#Function to find the neighbours of a cell ---------------------------------------------------

def neighbour(cells, cell):
    """Give as output the number of neighbours of a cell (only neighbours with the alive attribute = 1)

        cells: List containing all the instances of the initialized cells
        cell: The single instance of cell which will be examined to determine the number of live neighbours

        return: number of live neighbours
    """
    num_neighbours = 0 #Number of near live cells(Moore neighbourhood)
    x = cell.x
    y = cell.y

    #List of exceptions before the main algorithm
    #Upper-left corner (x = 0, y = 0) !*!*!*!*!*!*!*!*!**!*!*!*!*!*!*!*
    if (x == 0 and y == 0):
        #Cell on the right -----------
        current_x = 1
        current_y = 0

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current ----------------------------------------
        current_x = 1
        current_y = 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below original cell
        current_x = 0
        current_y = 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Return the number of neighbours
        return num_neighbours

    #Upper-right corner (x = window, y = 0)!*!*!*!*!**!*!*!*!*!*!*!*!*!*!*!*!*!*!**!*!*!*!*!*!*!*!
    elif (x == screen_width - cell.size and y == 0):
        #Cell below -------------------------------------
        current_x = screen_width - cell.size
        current_y = 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of current -----------------------------------
        current_x -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of original
        current_y = 0

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Return the number of neighbours
        return num_neighbours

    #Lower-left corner (x = 0, y = window) !*!*!*!**!*!!*!**!*!!**!*!*!*!*!*
    elif(x == 0 and y == (screen_height - cell.size)):

        #Cell over original ----------------------
        current_x = 0
        current_y = (screen_height - cell.size) - 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current ------------------------------------------
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current ---------------------------------------------
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Return the number of neighbours
        return num_neighbours



    #Lower right corner !*!*!*!*!*!!*!*!*!*!*!*!**!!*!*!*
    elif (x == (screen_width - cell.size) and y == (screen_height - cell.size)):

        #Cell to the left of original ------------------------------------------------
        current_x = (screen_width - cell.size) - 1
        current_y = screen_height - cell.size

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell on top of current -------------------------------------------------------
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Return the number of neighbours
        return num_neighbours


    #If the cell is in the first row (y = 0) (2 corners excluded) !*!*!*!*!*!!*!!*!*!*!*!
    elif (y == 0 and (x != 0 and x != (screen_width - cell.size))):
        #Cell to the right of original
        current_x = x + 1
        current_y = 0

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below original
        current_x = x

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of current
        current_x -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of original
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Return the number of neighbours
        return num_neighbours


    #If the cell is in the last row (y = screen_height) 2 corners excluded !*!*!*!*!*!*!*!!*!*
    elif (y == (screen_height - cell.size) and (x != 0 and x != (screen_width - cell.size))):
        #Cell to the left of original
        current_x = x - 1
        current_y = y

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell on top of current
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Return the number of neighbours
        return num_neighbours


    #If the cell is in the first column (2 corners excluded) !*!*!*!*!*!*!*!*!*!*!*!*
    elif (x == 0 and (y != 0 and y != (screen_height - cell.size))):
        #Cell on top of original
        current_x = x
        current_y = y - 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of current
        current_x -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)


        return num_neighbours


    #If the cell is in the last column (x = screen width) !*!*!*!*!*!*!*!!**!!*
    elif (x == (screen_width - cell.size) and (y != 0 and y != (screen_height - cell.size))):
        #Cell below original
        current_x = x
        current_y = y + 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of current
        current_x -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell on top of current
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell on top of current
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        return num_neighbours


    #GENERAL RULE
    else:
        #8 Neighbours
        #Cell on top of original
        current_x = x
        current_y = y - 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the right of current
        current_x += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell below current
        current_y += 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of current
        current_x -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell to the left of current
        current_x -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell on top of current
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        #Cell on top of current
        current_y -= 1

        num_neighbours += checkAlive(cell, cells, current_x, current_y)

        return num_neighbours


#CELL INITIALIZATION
cell_array = [] #2D array containing the cells in order[x, y]
x = 0
y = 0
init = False #Become true when Initialization is completed

#Array Initialization (X, Y matrix)
for i in range(int(screen_width / CELL_WIDTH)):
    cell_array.append([])
    for j in range(int(screen_height / CELL_WIDTH)):
        cell_array[i].append([])

#Cell Initialization
for i in range()
while not init:
    is_alive = random.choices([0,1], weights = (90, 10), k=1)[0]#Randomly spawn cells with probability (Dead 90%, Alive 10 %)
    cell = Cell(x, y, is_alive)#Single object
    pygame.draw.rect(screen, cell.color(), pygame.Rect(cell.x, cell.y, cell.size, cell.size))
    x += cell.size
    cell_array[int(x / CELL_WIDTH) - 1][int(y / CELL_WIDTH) - 1] = cell
    if x == screen_width: #End of a row
        x = 0
        y += cell.size
    if y == screen_height:#Last row
        init = True


pygame.display.flip() #To update the screen

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
    for i in range(int(screen_width / CELL_WIDTH)):
        for j in range(int(screen_height / CELL_WIDTH)):

            try:
                if cell_array[i][j].neighbours(cell_array) in (2, 3): #2 or 3 live neighbours (survive)
                    cell_array[i][j].alive = 1
                elif cell_array[i][j].neighbours(cell_array) < 2: #Few than 2 live neighbours (dies)
                    cell_array[i][j].alive = 0
                elif cell_array[i][j].neighbours(cell_array) > 3: #More than 3 live neighbours (dies)
                    cell_array[i][j].alive = 0
                elif ((cell_array[i][j].alive == 0) and (cell_array[i][j].neighbours(cell_array) == 3)): #Dead cell with 3 live neigh (live)
                    cell_array[i][j].alive == 1

            except Exception as e:
                print(e)


    #Debug
    print("Algorithm succesful.")

    #DRAWING CELLS
    for i in range(int(screen_width / CELL_WIDTH)):
        for j in range(int(screen_height / CELL_WIDTH)):
            pygame.draw.rect(screen, cell_array[i][j].color(), pygame.Rect(cell_array[i][j].x, cell_array[i][j].y, cell_array[i][j].size, cell_array[i][j].size))


    #Debug
    print("Cell loaded to the screen")

    screen.fill(WHITE)
    pygame.display.flip() #To update the screen
