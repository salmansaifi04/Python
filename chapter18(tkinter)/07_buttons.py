from tkinter import *

def button1():
    print("Hello This is button 1")


def button2():
    print("Hello This is button 2")


def button3():
    print("Hello This is button 3")


top = Tk()
top.geometry('700x500')
top.title('Buttons')

f1 = Frame(top, bg='lightgrey')
f1.pack(side=TOP, fill=X)

b1 = Button(f1, text='Button1', bg='black', fg='white', font='sans 16', command=button1)
b1.pack(side = 'left', pady=20, padx=20)

b2 = Button(f1, text='Button2', bg='black', fg='white', font='sans 16', command=button2)
b2.pack(side = 'left',pady=20)

b3 = Button(f1, text='Button3', bg='black', fg='white', font='sans 16',command=button3)
b3.pack(side = 'left',pady=20, padx=20)



top.mainloop()