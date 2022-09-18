import numpy as np
from tkinter import *
from PIL import Image


def pbc(x, y, xl, yl):
    if x < 0:
        x = x + xl
    if x >= xl:
        x = x - xl
    if y < 0:
        y = y + yl
    if y >= yl:
        y = y - yl

    return x, y


def surface(board, paras):
    xl = paras["xlength"]
    yl = paras["ylength"]

    # initialize map
    names = ["river", "water", "food"]
    types = ["int16", "int16", "int16"]

    mapp = np.zeros([xl, yl], dtype={'names': names, 'formats': types})

    # generate rivers
    riv_maxlength = 5000
    riv_minlength = 10
    riv_num = 20
    riv_range = 7  # how far water spreads

    for i in range(riv_num):
        print("Initialize rivers: ", i, "/", riv_num)

        riv_length = np.random.randint(riv_minlength, riv_maxlength)
        x_r = np.random.randint(int(xl * 0.1), int(xl * 0.9))
        y_r = np.random.randint(int(yl * 0.1), int(yl * 0.9))

        pref_x = np.random.randint(0, 2)
        pref_y = np.random.randint(0, 2)

        for j in range(riv_length):

            direction = np.random.randint(0, 10)
            if direction == 0 or direction == 1:
                x_r += 1
            elif direction == 2 or direction == 3:
                y_r += 1
            elif direction == 4 or direction == 5:
                x_r += -1
            elif direction == 6 or direction == 7:
                y_r += -1
            elif direction == 8:
                x_r += pref_x
                y_r += pref_y

            x_r, y_r = pbc(x_r, y_r, xl, yl)

            mapp[x_r, y_r]["river"] = 1

            # distribute water in vicinity

            for i in range(x_r - riv_range, x_r + riv_range):
                for j in range(y_r - riv_range, y_r + riv_range):
                    x_wat, y_wat = pbc(i, j, xl, yl)
                    mapp[x_wat, y_wat]["water"] += 1

    # create river image

    flat_map = list(np.reshape(np.transpose(mapp["river"]), xl * yl))
    flat_map_wat = list(np.reshape(np.transpose(mapp["water"]), xl * yl))

    for i in range(xl * yl):
        if flat_map[i] == 1:
            red = 0
            green = 0
            blue = 255
        else:
            if flat_map_wat[i] > 0:
                red = min(int(7 * flat_map_wat[i] / 5), 140)
                green = min(int(4 * flat_map_wat[i] / 5), 70)
                blue = min(int(1 * flat_map_wat[i] / 5), 20)
            else:
                red = 0
                green = 0
                blue = 0

        # blue = min(255 * flat_map[i] + 2 * flat_map_wat[i], 255)
        flat_map[i] = (red, green, blue)

    # brown: 139, 69, 19

    river_img = Image.new('RGB', (xl, yl))
    river_img.putdata(flat_map)
    # river_img.show()
    river_img.save('rivers.gif')

    # show image on canvas
    tk_river = PhotoImage(file='./rivers.gif')

    river_label = Label(board, image=tk_river)  # label required to keep image after function call
    river_label.image = tk_river

    board.create_image(0, 0, image=tk_river, anchor=NW)

    return mapp


def indivi_pos(board, population, paras):
    size = paras["indivi_size"]

    n = np.shape(population)[0]

    for i in range(0, n):
        if population[i]["alive"]:
            i_id = board.create_rectangle(population[i]["x"], population[i]["y"],
                                          population[i]["x"] + size, population[i]["y"] + size,
                                          fill=population[i]["color"])
            population[i]["id"] = i_id

    print(population)


def init_indivi(paras):
    n0 = paras["ini_indivi"]
    n = paras["max_indivi"]
    max_water = paras["max_water"]
    max_food = paras["max_food"]
    max_age = paras["max_age"]
    xlength = paras["xlength"]
    ylength = paras["ylength"]

    # initialize datatype
    names = ["x", "y", "color", "alive", "id", "age",
             "agelimit", "water", "food", "reproprob"]
    types = ["int16", "int16", "S7", "bool", "int16", "int16",
             "int16", "int16", "int16", "float16"]

    population = np.zeros(paras["max_indivi"], dtype={'names': names, 'formats': types})

    # make alive first n0
    population["alive"] = np.concatenate((np.ones(n0), np.zeros(n - n0)))

    # zero age
    population["age"] = 0

    # start with max energy
    population["food"] = max_food
    population["water"] = max_water

    # get max_age
    x_ini = np.random.normal(loc=max_age,
                             scale=max_age / 4, size=n)

    population["agelimit"] = x_ini

    # set reproduction probabilities
    population["reproprob"] = np.random.randint(1, 10, n) / max_age

    # set positions
    x_ini = np.random.randint(0, xlength, n)
    y_ini = np.random.randint(0, ylength, n)

    population["x"] = x_ini
    population["y"] = y_ini

    # initialize a color

    color_ini = []
    for i in range(0, n):

        aa = '#'
        for j in range(0, 6):
            a = str(np.random.randint(0, 16))
            if a == '10':
                a = 'a'
            elif a == '11':
                a = 'b'
            elif a == '12':
                a = 'c'
            elif a == '13':
                a = 'd'
            elif a == '14':
                a = 'e'
            elif a == '15':
                a = 'f'

            aa += a
        color_ini.append(aa)

    population["color"] = color_ini

    # print(population)

    return population
