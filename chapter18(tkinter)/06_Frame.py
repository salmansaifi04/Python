# frames 


from tkinter import *

top = Tk()

top.geometry('500x400')
top.title('Frame')

f2 = Frame(top, bg='black')
f2.pack(fill=X, side=TOP)

l2 = Label(f2, text='Nav bar', bg='black', fg='white', font='sans 20 bold')
l2.pack(pady=50)

f1 = Frame(top, bg='grey')
f1.pack(side=LEFT, fill=Y)

l1 = Label(f1, text='side bar', bg='grey', fg='white', font='sans 20 bold')
l1.pack(padx=20, pady=180)


top.mainloop()

