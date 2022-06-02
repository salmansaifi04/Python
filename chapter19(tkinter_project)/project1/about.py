from tkinter import *
from PIL import Image, ImageTk

import os
def home():
    top.destroy()
    os.system('python home.py')


def about():
    top.destroy()
    os.system('python about.py')

def services():
    top.destroy()
    os.system('python services.py')

def contact():
    top.destroy()
    os.system('python contact.py')



top = Tk()
top.title("Welcome to my site")
top.geometry('1300x770')
top.minsize(width=1300, height=770)
top.maxsize(width=1300, height=770)

f1 = Frame(top, height=80,  bg='black')
f1.pack(fill=X)


# buttons
Label(f1,bg='black',text='Travelling', font='sans 18',fg='white').pack(padx=200,side='left')
Button(f1,text='Home', font='sans 14',command=home).pack(side='left',padx=50, pady=25)
Button(f1,text='About', font='sans 14',command=about,bg='black',borderwidth=0,fg='white').pack(side='left',padx=50, pady=25)
Button(f1,text='Services', font='sans 14',command=services).pack(side='left',padx=50, pady=25)
Button(f1,text='Contact Us', font='sans 14',command=contact).pack(side='left',padx=50, pady=25)


f2 = Frame(top, height=500, width=1300)
f2.pack(pady=20)

f3 = Frame(f2, height=500, width=430)
f3.pack(side=LEFT, fill=Y)

## image
img = ImageTk.PhotoImage(Image.open('about1.jpg'))
Label(f3,image=img).pack()
Button(f3, text='Read More ...', font='sans 14',bg='red', fg='white', borderwidth=1).pack(pady=20)

f4 = Frame(f2, height=500, width=430)
f4.pack(side=LEFT, fill='both')

## image
img1 = ImageTk.PhotoImage(Image.open('about2.jpg'))
Label(f4,image=img1).pack()
Button(f4, text='Read More ...', font='sans 14',bg='green',  fg='white', borderwidth=1).pack(pady=20)

f6 = Frame(f2, height=500, width=430)
f6.pack(side=RIGHT, fill='both')

## image
img2 = ImageTk.PhotoImage(Image.open('about3.jpg'))
Label(f6,image=img2).pack()
Button(f6, text='Read More ...', font='sans 14',bg='yellowgreen', fg='white', borderwidth=1).pack(pady=20)

f5 = Frame(top, height=70, width=1300, bg='black')
f5.pack(fill=X)

Label(f5, text='2022 Copyright || All Right Reserve', font='sans 16',bg='black', fg='white').pack(pady=10)


top.mainloop()