import tkinter


def init_screen(xlength, ylength) -> none:
    master = Tk()

    w = Canvas(master, width=xlength, height=ylength, bg='black', bd=0)
    w.pack()

    mainloop()

    return
