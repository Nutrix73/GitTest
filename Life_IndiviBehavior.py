import numpy as np


def pbc(x, y, s, xl, yl):
    if x < 0:
        x = x + xl
    if x >= xl:
        x = x - xl
    if y < 0:
        y = y + yl
    if y >= yl:
        y = y - yl

    return x, y


def behave(board, indiv, paras, map):
    indivi_size = paras["indivi_size"]
    xlength = paras["xlength"]
    ylength = paras["ylength"]
    watcost_move = paras["watcost_move"]
    foodcost_move = paras["foodcost_move"]
    max_water = paras["max_water"]
    max_food = paras["max_food"]

    # get variables
    id_no = indiv["id"]
    x, y, x2, y2 = board.coords(id_no)

    # aging
    indiv["age"] += 1

    # update position
    x_new = int(x + np.random.randint(-1, 2))
    y_new = int(y + np.random.randint(-1, 2))
    x_new, y_new = pbc(x_new, y_new, indivi_size, xlength, ylength)
    board.coords(id_no, x_new, y_new, x_new + indivi_size, y_new + indivi_size)

    # remove energy for movement
    indiv["water"] -= watcost_move

    # drink if possible
    if map[x_new, y_new]["water"] > 0:
        indiv["water"] = max_water

    # multiply check
    if np.random.uniform() < indiv["reproprob"]:
    # now check if enough food and water, substract energy form multiplying

    # check for oldage and exhaustion
    if (indiv["age"] >= indiv["agelimit"]) \
            or (indiv["water"] <= 0) or (indiv["food"] <= 0):
        indiv["alive"] = 0
        board.delete(id_no)

    return indiv
