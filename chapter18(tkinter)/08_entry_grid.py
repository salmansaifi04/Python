# Entry widget and grid layout

from tkinter import *

def getval():
    print(uservalue.get())
    print(passvalue.get())


top = Tk()
top.geometry('700x600')

username = Label(top, text='username')
password = Label(top, text='password')
username.grid()
password.grid()

# variable clases in tkinter
# Booleanvar, Doublevar, Intvar, Stringvar

uservalue = StringVar() 
passvalue = StringVar() 

e1 = Entry(top, textvariable=uservalue)
e2 = Entry(top, textvariable=passvalue)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(top, text='submit', command=getval).grid()


top.mainloop()