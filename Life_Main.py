import Life_Initialize as Initialize
import Life_IndiviBehavior as IndiviBehavior
import numpy as np
from tkinter import *

# important parameter
##########################################################
# ini_indivi = 100    # initial number of indivis
# max_indivi = 200    # maximum allowed number of indivis
# max_age = 1000      # maximum allowed age
# max_energy = 1000   # maximum energy of individual
#
# ecost_move = 10     # energy cost for moving one pixel
#
# xlength = 1400      # screen width
# ylength = 750       # screen length
# indivi_size = 4     # pixel length of indivi squares
##########################################################

Life_paras = {"ini_indivi": 100, "max_indivi": 200, "max_age": 10000,
              "max_food": 10000, "max_water": 10000,
              "watcost_move": 10, "foodcost_move": 0,
              "xlength": 1400, "ylength": 750, "indivi_size": 4}

# init indivi
Population = Initialize.init_indivi(Life_paras)


# main loop
def turn():
    '''
    Running one turn
    '''

    for i in range(0, Life_paras["max_indivi"]):

        if Population[i]["alive"]:
            Population[i] = IndiviBehavior.behave(board, Population[i], Life_paras, Map)

        # x1,y1,x2,y2=board.coords(id1)
        # board.coords(id1,x1+np.random.randint(-1,2),y1+np.random.randint(-1,2),x2+np.random.randint(-1,2),y2+np.random.randint(-1,2))
    board.after(1, turn)


# tkinter loop
master = Tk()
board = Canvas(master, width=Life_paras["xlength"],
               height=Life_paras["ylength"], bg='black', bd=0)
board.pack()

Map = Initialize.surface(board, Life_paras)
Initialize.indivi_pos(board, Population, Life_paras)

board.after(1, turn)

mainloop()
