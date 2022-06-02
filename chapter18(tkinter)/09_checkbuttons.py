from tkinter import *

top = Tk()
top.geometry("500x300")

Label(top, text="Welcome to the Sk Travels", font="sans 18 bold",pady=10).grid(row=0, column=2)

## creating labels
name = Label(top, text="Name") 
Phone = Label(top, text="Phone") 
Gender = Label(top, text="Gender") 
Payment_mode = Label(top, text="Payment mode") 

## packing the labels
name.grid(row=1, column=1) 
Phone.grid(row=2, column=1) 
Gender.grid(row=3, column=1) 
Payment_mode.grid(row=4, column=1) 

## creating entries widget
name_entry = Entry(top)
phone_entry = Entry(top)
gender_entry = Entry(top)
payment_entry = Entry(top)

## packing the entries 
name_entry.grid(row=1, column=2)
phone_entry.grid(row=2, column=2)
gender_entry.grid(row=3, column=2)
payment_entry.grid(row=4, column=2)

## creating checkbuttons
check_button = Checkbutton(top, text="Want to prebook your meals?")
check_button.grid(row=5, column=2) 

## creating button
Button(top,text='submit',font='sans 14 bold').grid(row=6, column=2)


top.mainloop()


## Quick Exercise ##

from tkinter import *

top = Tk()

## defining a function
def show():
    t1 = userentry.get()
    t2 = passentry.get()
    print(f"user name is {t1}")
    print(f"password is {t2}")



top.geometry('400x200')
username = Label(top, text='username', font='sans 14 bold',pady=10)
username.grid(row=2, column=1)
password = Label(top, text='password', font='sans 14 bold',pady=10)
password.grid(row=3, column=1)

## text variables
userval = StringVar()
passval = StringVar()

## entry widget
userentry = Entry(top, textvariable=userval)
userentry.grid(row=2, column=2)

passentry = Entry(top, textvariable=passval)
passentry.grid(row=3, column=2)

## button
Button(top, text='submit',command=show).grid(row=4, column=2)

top.mainloop()