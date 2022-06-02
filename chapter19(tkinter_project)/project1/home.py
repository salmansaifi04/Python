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
top.geometry('1300x700')
top.minsize(width=1300, height=700)
top.maxsize(width=1300, height=700)

f1 = Frame(top, height=100,  bg='black')
f1.pack(fill=X)


# buttons
Label(f1,bg='black',text='Travelling', font='sans 18',fg='white').pack(padx=200,side='left')
Button(f1,text='Home',bg='black',borderwidth=0,fg='white', font='sans 14',command=home).pack(side='left',padx=50, pady=30)
Button(f1,text='About', font='sans 14',command=about).pack(side='left',padx=50, pady=30)
Button(f1,text='Services', font='sans 14',command=services).pack(side='left',padx=50, pady=30)
Button(f1,text='Contact Us', font='sans 14',command=contact).pack(side='left',padx=50, pady=30)


f2 = Frame(top, height=500, width=1300)
f2.pack()

f3 = Frame(f2, height=500, width=580)
f3.pack(side=LEFT, fill=Y)

# image
img = ImageTk.PhotoImage(Image.open('01.jpg'))
Label(f3,image=img).pack()


f4 = Frame(f2, height=500, width=710,)
f4.pack(side=RIGHT, fill='both')

Label(f4,text='Exploring The World', font='sans 22 bold',width=710).pack(pady=50)
Label(f4,text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n Lorem Ipsum has been the industry\'s standard dummy text ever since \n the 1500s, when an unknown printer took a galley of type and scrambled \n it to make a type specimen book. It has survived not only five centuries, \n but also the leap into electronic typesetting, remaining essentially \n unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop \n publishing software like Aldus PageMaker including \n versions of Lorem Ipsum', font='sans 16').pack()
Button(f4, text='Read More ...', font='sans 16 bold').pack(pady=40)

f5 = Frame(top, height=100, width=1300, bg='black')
f5.pack(fill=X)

Label(f5, text='2022 Copyright || All Right Reserve', font='sans 16',bg='black', fg='white').pack(pady=30)


top.mainloop()