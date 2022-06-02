## all tkinter events google search ##

from tkinter import *


def show(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

def quit(event):
    print("Double click to stop")
    import sys
    sys.exit()


top = Tk()
top.geometry('600x300')
top.title("Tkinter Events")

widget = Button(top, text='click me please')
widget.pack()

widget.bind('<Button-1>', show)
widget.bind('<Double-1>', quit)


top.mainloop()
