from tkinter import *


class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x500')
        self.title('Tkinter - classes and object')

    def status_bar(self):
        self.var = StringVar()
        self.var.set('ready')
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor='w')
        self.statusbar.pack(side='bottom', fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()


if __name__ == '__main__':
    window = Gui()
    window.status_bar()
    window.click()
    window.createbutton('click me')
    window.mainloop()