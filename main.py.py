
from tkinter import *
window = Tk()






lab1 =Label(window,bg='lightgreen',bd=15,text='Change case',font=('calibri',30,'bold'))
lab1.pack(padx=15,pady=15)
#lab1.grid(row=0,column=7)

ent1 = Entry(window,bg='orange',bd=3,font=('Calibri',30),text='Enter text')
ent1.pack()
#ent1.pack()



lab2 = Label(window,bg='lightgreen',bd=10,text='Result',font=('calibri',30,'bold'))
lab2.pack(padx=15,pady=15)


def changeupper():
    name = ent1.get()
    upper = name.upper()
    lab2.config(text=upper)

def changelower():
    name = ent1.get()
    lower = name.lower()
    lab2.config(text=lower)


def changetitle():
    name = ent1.get()
    title = name.title()
    lab2.config(text=title)


def changeswap():
    name = ent1.get()
    swap = name.swapcase()
    lab2.config(text=swap)

btn1 = Button(window,text='upper',font=('calibri',20,'bold'),bg='green',fg='yellow',command=changeupper)
btn1.pack()


btn2 = Button(window,text='lower',font=('calibri',20,'bold'),bg='green',fg='yellow',command=changelower)
btn2.pack()


btn3 = Button(window,text='title',font=('calibri',20,'bold'),bg='green',fg='yellow',command=changetitle)
btn3.pack()


btn4 = Button(window,text='swapcase',font=('calibri',20,'bold'),bg='green',fg='yellow',command=changeswap)
btn4.pack()











window = mainloop() # infinite loop .place at the bottom of code


