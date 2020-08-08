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

    #def neighbours(self, cell_array): #Return the number of live neighbours of a cell
        #num_neighbours = 0
