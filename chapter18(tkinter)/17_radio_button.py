from tkinter import *
import tkinter.messagebox as msg

def order():
    msg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")


top = Tk()
top.geometry('400x200')
top.title('Tkinter - Radio Button')

Label(top, text = "What would you like to have sir?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)


radio = Radiobutton(top, text='Dosa',variable=var, value='Dosa').pack(anchor="w")
radio = Radiobutton(top, text='Idly',variable=var, value='Idly').pack(anchor="w")
radio = Radiobutton(top, text='Somosa',variable=var, value='Somosa').pack(anchor="w")
radio = Radiobutton(top, text='paratha',variable=var, value='paratha').pack(anchor="w")

Button(top, text="Order Now", command=order).pack()

top.mainloop()


