from tkinter import *

def add_item():
    global i
    list_box.insert(ACTIVE,i)
    i+=1

i=0


top = Tk()
top.geometry('600x400')
top.title('Tkinter - list box')

list_box = Listbox(top)
list_box.pack()

list_box.insert(END, 'first list box item')

Button(top, text='add item', command=add_item).pack()


top.mainloop()
