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


