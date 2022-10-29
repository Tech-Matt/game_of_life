#Cell class
CELL_WIDTH = 40

BLACK = (0, 0, 0)  # Living cell
WHITE = (255, 255, 255)  # Dead cell


def color_decode(integer):
    """Return BLACK when integer == 1
       Return WHITE when integer == 0
    """
    if integer == 1:
        return BLACK
    elif integer == 0:
        return WHITE
    else:
        print("[VALUE ERROR] in alive attribute")


class Cell:

    def __init__(self, x, y, alive):
        """ x: x coordinate
            y: y coordinate
            alive: int (boolean, 0 o 1), to track the status of a cell (live or dead),
            at startup is random
        """
        self.x = x
        self.y = y
        self.size = CELL_WIDTH #it's a square
        self.alive = alive

    def color(self):#Return color tuple
        col = color_decode(self.alive)
        return col
    
    def neighboors(self, array):
        minX = 0
        minY = 0
        maxX = 0
        maxY = 0
        # Set X bounds
        if self.x == 0:
            minX = 0
        else:
            minX = self.x - 1
        if self.x == len(array[self.y])-1:
            maxX = self.x
        else:
            maxX = self.x + 1
        # Set Y bounds
        if self.y == 0:
            minY = 0
        else:
            minY = self.y - 1
        if self.y == len(array)-1:
            maxY = self.y
        else:
            maxY = self.y + 1
        # Loop Ranges counting the Alive
        counter = 0
        for xIter in range(minX, maxX+1):
            for yIter in range(minY, maxY+1):
                if array[xIter][yIter].alive:
                    counter += 1
        return counter - self.alive
    
    


