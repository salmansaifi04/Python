from tkinter import *

top = Tk()
top.geometry("500x300")

## defining function
def show():
    k1 = name_entry.get()
    k2 = phone_entry.get()
    k3 = gender_entry.get()
    k4 = payment_entry.get()
    k5 = checkbutton_var.get()
    print(k1)
    print(k2)
    print(k3)
    print(k4)
    print(k5)

    with open("demo.txt", "a") as f:
        f.write(f"{k1, k2, k3, k4, k5}\n")


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

## creating variables
name_var = StringVar
phone_var = IntVar
gender_var = StringVar
payment_var = StringVar
checkbutton_var = IntVar()



## creating entries widget
name_entry = Entry(top,textvariable=name_var)
phone_entry = Entry(top,textvariable=phone_var)
gender_entry = Entry(top,textvariable=gender_var)
payment_entry = Entry(top,textvariable=payment_var)

## packing the entries 
name_entry.grid(row=1, column=2)
phone_entry.grid(row=2, column=2)
gender_entry.grid(row=3, column=2)
payment_entry.grid(row=4, column=2)

## creating checkbuttons
check_button = Checkbutton(top, text="Want to prebook your meals?",variable=checkbutton_var)
check_button.grid(row=5, column=2) 

## creating button
Button(top,text='submit',font='sans 14 bold', command=show).grid(row=6, column=2)


top.mainloop()

