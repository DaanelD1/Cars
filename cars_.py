from tkinter import *
from tkinter.ttk import Radiobutton


def clicked():
    global photo
    if selected.get()==1:
        k = open('bmw.txt')
        lbl.configure(text=k.read())
        photo = PhotoImage(file="bmw.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==2:
        o = open('Dodge.txt')
        lbl.configure(text=o.read())
        photo = PhotoImage(file="Dodge.PNG")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==3:
        zelt = open('Mercedes.txt')
        lbl.configure(text=zelt.read())
        photo = PhotoImage(file="mercedes.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==4:
        zel = open('Politsei.txt')
        lbl.configure(text=zel.read())
        photo = PhotoImage(file="politsei.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif selected.get()==5:
        g = open('Lamborghini.txt')
        lbl.configure(text=g.read())
        photo = PhotoImage(file="lamborghini.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    else:
        lbl.configure(text="Выбери машину")



window = Tk()
window.title("п ")
window.geometry('720x360')
selected = IntVar()
rad1 = Radiobutton(window, text='БМВ', value=1, variable=selected)
rad2 = Radiobutton(window, text='Додж', value=2,variable=selected)
rad3 = Radiobutton(window, text='Мерседес', value=3, variable=selected)
rad4 = Radiobutton(window, text='Полиция', value=4, variable=selected)
rad5 = Radiobutton(window, text='Ламборгини', value=5, variable=selected)
btn = Button(window, text="Узнать характеристики", command=clicked)
lbl = Label(window)

window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=0)
window.rowconfigure(4, weight=0)
window.rowconfigure(5, weight=0)
window.columnconfigure(4, weight=1)

rad1.grid(column=0, row=2)
rad2.grid(column=0, row=3)
rad3.grid(column=0, row=4)
rad4.grid(column=0, row=5)
rad5.grid(column=0, row=6)
btn.grid(column = 0, row = 1)
lbl.grid(column = 2, row = 9, rowspan=6)

canvas = Canvas(window, height=200, width=500)
canvas.grid(row=2, column=2, rowspan=7)



window.mainloop()

