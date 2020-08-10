#Cell class
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

    def color(self):#Return color tuple
        col = color_decode(self.alive)
        return col

    def neighbours(self, cell_array): #Return the number of live neighbours of a cell
        """Give as output the number of neighbours of a cell (only neighbours with the alive attribute = 1)

            cell_array: List containing all the instances of the initialized cells

            return: number of live neighbours
        """
        num_neighbours = 0
        x = self.x
        y = self.y

        #List of exceptions before the main algorithm
        #Upper-left corner (x = 0, y = 0) !*!*!*!*!*!*!*!*!**!*!*!*!*!*!*!*
        #if (x == 0 and y == 0):
            #Cell on the right -----------
            #if (cell_array[x+1][y].alive == 1):
                #num_neighbours += 1
            #Cell below current ----------------------------------------
            #if (cell_array[])

        #GENERAL ALGORITHM
        #8 Neighbours
        #Cell on top of original
        if (cell_array[x][y-1].alive == 1):
            num_neighbours += 1
        #Cell to the right of current
        if (cell_array[x+1][y-1].alive == 1):
            num_neighbours += 1
        #Cell below current
        if (cell_array[x+1][y].alive == 1):
            num_neighbours += 1
        #Cell below current
        if (cell_array[x+1][y+1].alive == 1):
            num_neighbours += 1
        #Cell to the left of current
        if (cell_array[x][y+1].alive == 1):
            num_neighbours += 1
        #Cell to the left of current
        if (cell_array[x-1][y+1].alive == 1):
            num_neighbours += 1
        #Cell on top of current
        if (cell_array[x-1][y].alive == 1):
            num_neighbours += 1
        #Cell on top of current
        if (cell_array[x-1][y-1].alive == 1):
            num_neighbours += 1

        return num_neighbours
