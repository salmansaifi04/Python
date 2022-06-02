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

f1 = Frame(top, height=80,  bg='black')
f1.pack(fill=X)


# buttons
Label(f1,bg='black',text='Travelling', font='sans 18',fg='white').pack(padx=200,side='left')
Button(f1,text='Home', font='sans 14',command=home).pack(side='left',padx=50, pady=20)
Button(f1,text='About', font='sans 14',command=about).pack(side='left',padx=50, pady=20)
Button(f1,text='Services',bg='black',borderwidth=0,fg='white', font='sans 14',command=services).pack(side='left',padx=50, pady=20)
Button(f1,text='Contact Us', font='sans 14',command=contact).pack(side='left',padx=50, pady=20)


f2 = Frame(top, height=200, width=1300)
f2.pack()
# image
img = ImageTk.PhotoImage(Image.open('services.jpg'))
Label(f2,image=img).pack()

f3 = Frame(top, height=100,  bg='grey')
f3.pack(fill=X, pady='20')
Label(f3,text='MALDIVES', font='sans 16').pack(padx=20,pady='30',side='left')

Label(f3,text='03 Days/ 02 Nights', font='sans 16').pack(padx=350,pady='30',side='left')

Label(f3,text='$25', font='sans 16').pack(pady='30',side='left')
Button(f3, text='BOOK NOW',font='sans 11').pack(pady='30',side='right',padx=15)



f4 = Frame(top, height=100, bg='grey')
f4.pack(fill='x',pady=10)
Label(f4,text='LONDON, ENGLAND', font='sans 16').pack(padx=20,pady='30',side='left')

Label(f4,text='03 Days/ 02 Nights', font='sans 16').pack(padx=260,pady='30',side='left')

Label(f4,text='$35', font='sans 16').pack(pady='30',padx=88,side='left')
Button(f4, text='BOOK NOW',font='sans 11').pack(pady='30',side='right',padx=15)


f5 = Frame(top, height=100, bg='grey')
f5.pack(fill='x',pady=10)
Label(f5,text='TURKEY, GRENEDA', font='sans 16').pack(padx=20,pady='30',side='left')

Label(f5,text='07 Days/ 06 Nights', font='sans 16').pack(padx=260,pady='30',side='left')

Label(f5,text='$49', font='sans 16').pack(pady='30',padx=88,side='left')
Button(f5, text='BOOK NOW',font='sans 11').pack(pady='30',side='right',padx=15)





f6 = Frame(top, height=80, width=1300, bg='black')
f6.pack(fill=X,anchor='se', side='bottom')

Label(f6, text='2022 Copyright || All Right Reserve', font='sans 16',bg='black', fg='white').pack(pady=10)


top.mainloop()