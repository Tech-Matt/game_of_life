# Conway Game of Life

import pygame
import random
import sys

# PYGAME INITIALIZATION
success, failure = pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))  # Init the screen
time = pygame.time.Clock()  # Time from startup
FPS = 1

# Screen Area = 480000 px (width * height)
# Area of a cell = 1600px --> 300 Cell

CELL_WIDTH = 40

BLACK = (0, 0, 0)  # Live cell
WHITE = (255, 255, 255)  # dead cell

def color_decode(integer):
    """Return BLACK when integer == 1
       Return WHITE when integer == 0
    """
    if integer == 1:
        return BLACK
    elif integer == 0:
        return WHITE
    else:
        print("Value error in 'alive' attribute")


class Cell:
    """ x: x coordinate
        y: y coordinate
        size: width and height (same, square)
        alive: int (boolean, 0 o 1), to track the status of a cell (live or dead), at the startup is random
    """
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.size = CELL_WIDTH #it's a square
        self.alive = alive

    def draw():#Draw the cell into the screen
        pygame.draw.rect(screen, color_decode(self.alive), pygame.Rect(self.x, self.y, self.size, self.size))

    def update():
        pass

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

        #Cell to the right of original
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
#Useful variable in the for loop
x = 0
y = 0
init = False #Become true when Initialization is completed

#Array Initialization (X, Y matrix)
for i in range(screen_width / CELL_WIDTH):
    cell_array.append([])
    for j in range(screen_height / CELL_WIDTH):
        cell_array[i].append([])

#First Value
cell_array[x][y] = Cell(x, y, random.randint(0, 1))

#Cell Initialization
while not init:
    is_alive = random.choices([0,1], weights = (90, 10), k=1)[0]#Randomly spawn cells with probability (Dead 95%, Alive 5 %)
    cell = Cell(x, y, is_alive)#Single object
    x += cell.size
    cell_array[x / CELL_WIDTH][y / CELL_WIDTH] = cell
    if x == screen_width - cell.size: #End of a row
        x = 0
        y += cell.size
    if y == screen_height - cell.size:#Last row
        init = True


#DRAWING CELLS
for cl in cell_array:
    pygame.draw.rect(screen, cl.color, pygame.Rect(cl.x, cl.y, cl.size, cl.size))#Draw any single cell

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
    for cell in cell_array:
        if neighbour(cell_array, cell) in (2, 3): #2 or 3 live neighbours (survive)
            cell.alive = 1
        elif neighbour(cell_array, cell) < 2: #Few than 2 live neighbours (dies)
            cell.alive = 0
        elif neighbour(cell_array, cell) > 3: #More than 3 live neighbours (dies)
            cell.alive = 0
        elif ((cell.alive == 0) and (neighbour(cell_array, cell) == 3)): #Dead cell with 3 live neigh (live)
            cell.alive == 1


    #Debug
    print("Algorithm succesful.")

    #DRAWING CELLS
    for cl in cell_array:
        pygame.draw.rect(screen, cl.color, pygame.Rect(cl.x, cl.y, cl.size, cl.size))
    #Debug
    print("Cell loaded to the screen")

    screen.fill(WHITE)
    pygame.display.flip() #To update the screen
