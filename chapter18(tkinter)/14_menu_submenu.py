from cProfile import label
from tkinter import *
top = Tk()

def myfunc():
    pass

top.geometry('600x400')
top.title("Menu and submenu")

## how to create non drop menu
# mymenu = Menu(top)
# mymenu.add_command(label='File', command=myfunc)
# mymenu.add_command(label='Exit', command=quit) 
# top.config(menu=mymenu)


## how to create a drop down menu

# main menu
mainmenu = Menu(top)

# sub menu 1
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='New project')
m1.add_command(label='Save')
m1.add_separator()
m1.add_command(label='Save As')
m1.add_command(label='Print')
top.config(menu=mainmenu)
mainmenu.add_cascade(label='File', menu=m1)


# sub menu 2
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='Cut')
m2.add_command(label='Copy')

m2.add_separator()   # add file between the text

m2.add_command(label='Paste')
m2.add_command(label='Find')
top.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit', menu=m2)


top.mainloop()