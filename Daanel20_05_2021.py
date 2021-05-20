from tkinter import *
from tkinter import scrolledtext

win = Tk()
win.title("Privet")
win.resizable(width=False, height=False)


def control():
    accept()
    picture()

def accept():
    show.config(text=spisok.get(spisok.curselection()))
    if spisok.get == 'bmw':
        txt.delete(1.0, END)
        f = open('bmw.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Mercedes':
        txt.delete(1.0, END)
        f = open('Mercedes.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Dodge':
        txt.delete(1.0, END)
        f = open('Dodge.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Politsei':
        txt.delete(1.0, END)
        f = open('Politsei.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Lamborghini':
        txt.delete(1.0, END)
        f = open('Lamborghini.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()



def picture():
    global photo
    global spisok
    show.config(text=spisok.get(spisok.curselection()))
    if spisok.get(spisok.curselection)()==1:
        k = open('bmw.txt')
        lbl.configure(text=k.read())
        photo = PhotoImage(file="img/bmw.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif spisok.get()==2:
        k = open('Mercedes.txt')
        lbl.configure(text=o.read())
        photo = PhotoImage(file="img/mercedes.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif spisok.get()==3:
        k = open('Dodge.txt')
        lbl.configure(text=zelt.read())
        photo = PhotoImage(file="img/Dodge.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif spisok.get()==4:
        k = open('Politsei.txt')
        lbl.configure(text=zel.read())
        photo = PhotoImage(file="img/politsei.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)
    elif spisok.get()==5:
        k = open('Lamborghini.txt')
        lbl.configure(text=g.read())
        photo = PhotoImage(file="img/lamborghini.png")
        canvas.create_image(0, 0, anchor='nw',image=photo)

spisok = Listbox(selectmode=SINGLE, width=10, height=12)
spisok.insert(1, 'Bmw')
spisok.insert(2, 'Mercedes')
spisok.insert(3, 'Dodge')
spisok.insert(4, 'Politsei')
spisok.insert(5, 'Lamborghini')
spisok.grid(column=0, row=0, padx=10)

Button(win, text='Подтвердить', command=lambda: control()).grid(column=1, row=0)

txt = scrolledtext.ScrolledText(win, width=40, height=10, borderwidth=5)
txt.grid(column=2, row=0, padx=10)

show = Label(win)
win.mainloop()
(0, )


