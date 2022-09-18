from tkinter import *

'''
Added Docstring
'''


def place_img(canvas):

    photo=PhotoImage(file='rivers.gif')
    photo_label = Label(canvas, image=photo)
    photo_label.image = photo
    canvas.create_image(25, 0, image=photo, anchor=NW)

    return

def place_point(canvas):

    canvas.create_rectangle(200, 200, 205, 205, fill='red')

    return

master = Tk()
canvas = Canvas(master, width=300, height=300, bg='black', bd=0)
canvas.pack()

place_point(canvas)
place_img(canvas)

mainloop()
