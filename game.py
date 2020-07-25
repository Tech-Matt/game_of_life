#Game of Life

import pygame
import random


#INIZIALIZZAZIONE PYGAME
success, failure = pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height)) #Inizializza lo schermo
time = pygame.time.Clock() #Tiene traccia del tempo trascorso
FPS = 5

#Area = 480000 px
#Cell of area = 100px --> 4800 Cell

BLACK = (0, 0, 0)#Cella Viva
WHITE = (255, 255, 255)#Cella morta


#Classe di celle
class Cell:
    """ x: ascissa
        y: ordinata
        size: grandezza
        alive: int (boolean, 0 o 1) flag per indicare lo stato della cella (morta, viva), all'inizio e' casuale
    """
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.size = 10 #it's a square
        self.alive = alive
        if self.alive == 1:
            self.color = BLACK
        elif self.alive == 0:
            self.color = WHITE

#Function needed in the next function ------------------------------------------------
def checkAlive(cell, cellArray, curr_x, curr_y, counter):
    """ Check wheter the current cell near the original cell is alive. If it is alive it adds 1 to the counter

        cell: object of the original cell
        cellArray: cell list with all the initialized cells
        curr_x: x coordinate of the cell which will be examined
        curr_y: y coordinate of the cell which will be examined
        counter: variable that is updated whenever a cell near to original has the "alive" attribute = 1
    """

    for current_cell in cellArray:
        if (current_cell.x == curr_x and current_cell.y == curr_y):
            if (current_cell.alive == 1):
                counter += 1


#Funzione per trovare i vicini delle celle ---------------------------------------------------

def neighbour(cells, cell):
    """ Da in output il numero di vicini di cell che hanno l'attributo alive = 1

        cells: lista che contiene tutte le istanze di tipi cella inizializzate
        cell: l'istanza di cui dobbiamo determinare i vicini 'vivi'

        return: number of live neighbours
    """
    num_neighbours = 0 #Numero di celle vicine vive (vicinanza di Moore)
    x = cell.x
    y = cell.y

    #Angolo in alto a sinistra (x = 0, y = 0) !*!*!*!*!*!*!*!*!**!*!*!*!*!*!*!*
    if (x == 0 and y == 0):
        #Cella alla sua destra -----------
        current_x = 1
        current_y = 0

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current ----------------------------------------
        current_x = 1
        current_y = 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a quella iniziale
        current_x = 0
        current_y = 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Ritorno il numero di vicini
        return num_neighbours

    #Angolo in alto a destra (x = finestra, y = 0)!*!*!*!*!**!*!*!*!*!*!*!*!*!*!*!*!*!*!**!*!*!*!*!*!*!*!
    elif (x == screen_width - cell.size and y == 0):
        #Cella sotto -------------------------------------
        current_x = screen_width - cell.size
        current_y = 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di current -----------------------------------
        current_x -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di original
        current_y = 0

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Ritorno il numero di vicini
        return num_neighbours

    #Angolo in basso a sinistra (x = 0, y = finestra) !*!*!*!**!*!!*!**!*!!**!*!*!*!*!*
    elif(x == 0 and y == (screen_height - cell.size)):

        #Cella sopra a original ----------------------
        current_x = 0
        current_y = (screen_height - cell.size) - 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current ------------------------------------------
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current ---------------------------------------------
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Ritorno il numero di vicini
        return num_neighbours



    #Angolo in basso a destra !*!*!*!*!*!!*!*!*!*!*!*!**!!*!*!*
    elif (x == (screen_width - cell.size) and y == (screen_height - cell.size)):

        #Cella a sinistra di original ------------------------------------------------
        current_x = (screen_width - cell.size) - 1
        current_y = screen_height - cell.size

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sopra a current -------------------------------------------------------
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Ritorno il numero di vicini
        return num_neighbours


    #Se la cella si trova nella prima riga (y = 0) (e non e' nei 2 angoli) !*!*!*!*!*!!*!!*!*!*!*!
    elif (y == 0 and (x != 0 and x != (screen_width - cell.size))):
        #Cella a destra di original
        current_x = x + 1
        current_y = 0

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a original
        current_x = x

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di current
        current_x -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di original
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Ritorno il numero di vicini
        return num_neighbours


    #Se la cella si trova nell'ultima riga (y = screen_height) e non nei due angoli !*!*!*!*!*!*!*!!*!*
    elif (y == (screen_height - cell.size) and (x != 0 and x != (screen_width - cell.size))):
        #Cella a sinistra di original
        current_x = x - 1
        current_y = y

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sopra a current
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Ritorno il numero di vicini
        return num_neighbours


    #Se la cella si trova nella prima colonna (e non nei due angoli) !*!*!*!*!*!*!*!*!*!*!*!*
    elif (x == 0 and (y != 0 and y != (screen_height - cell.size))):
        #Cella sopra a original
        current_x = x
        current_y = y - 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di current
        current_x -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)


        return num_neighbours


    #Se la cella si trova nell'ultima colonna (x = screen width) !*!*!*!*!*!*!*!!**!!*
    elif (x == (screen_width - cell.size) and (y != 0 and y != (screen_height - cell.size))):
        #Cella sotto a original
        current_x = x
        current_y = y + 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di current
        current_x -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sopra a current
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sopra a current
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        return num_neighbours


    #CASO GENERALE
    else:
        #8 Vicini
        #Cella sopra a original
        current_x = x
        current_y = y - 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a destra di current
        current_x += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sotto a current
        current_y += 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di current
        current_x -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella a sinistra di current
        current_x -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sopra a current
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        #Cella sopra a current
        current_y -= 1

        checkAlive(cell, cells, current_x, current_y, num_neighbours)

        return num_neighbours




#INIZIALIZZAZIONE Celle
cell_array = []
#Useful variable in the for loop
x = 0
y = 0
init = False #Diventa True quando ha inizializzato tutte le celle


#Inizializzazione
while not init:

    is_alive = random.choices([0,1], weights = (95, 5), k=1)[0]#Sceglie random utilizzando la probabilita'
    cell = Cell(x, y, is_alive)#Single object
    x += cell.size
    cell_array.append(cell)
    if x == screen_width: #Fine riga
        x = 0
        y += cell.size
    if y == screen_height:
        init = True #Celle inizializzate


#DISEGNO CELLE
for cl in cell_array:
    pygame.draw.rect(screen, cl.color, pygame.Rect(cl.x, cl.y, cl.size, cl.size))#Disegna ogni singola cella

pygame.display.flip() #To update the screen

#Debug
print("Initialization Completed.")


done = False #Check whether the program should run

#Main loop
while not done:
    #FPS
    time.tick(FPS)

    #GESTORE EVENTI
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Exit button
            print("Quitting.")
            done = True



    #SIMULAZIONE --------------------------------------------------------------------

    #Esegue l'algoritmo del 'gioco' e aggiorna quindi la schermata (algoritmo di Moore)
    #Per ogni cella che ha l'attributo alive
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

    #DISEGNO CELLE
    for cl in cell_array:
        pygame.draw.rect(screen, cl.color, pygame.Rect(cl.x, cl.y, cl.size, cl.size))#Disegna ogni singola cella
    #Debug
    print("Cell loaded to the screen")

    pygame.display.flip() #To update the screen
