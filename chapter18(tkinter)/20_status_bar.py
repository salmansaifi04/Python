from tkinter import *

def upload():
    statusbar.set('Busy')
    sbar.update()
    import time
    time.sleep(2)
    statusbar.set('ready now')


top = Tk()
top.geometry('500x400')
top.title('Tkinter - Status Bar')


statusbar = StringVar()
statusbar.set('ready')
sbar = Label(top, textvariable=statusbar, relief=SUNKEN, anchor='w')
sbar.pack(side='bottom',fill=X)

Button(top, text='update', command=upload).pack()


top.mainloop()