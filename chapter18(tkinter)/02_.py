# label, geometry, minsize, maxsize

from tkinter import *
top = Tk()

# geometry  (width x height)
top.geometry('800x500')

# minsize (width, height)
top.minsize(200, 100)

# maxsize (width, height)
top.maxsize(1200, 600)

# label
l1 = Label(top, text='Salman is a good boy')
l1.pack()


top.mainloop()

