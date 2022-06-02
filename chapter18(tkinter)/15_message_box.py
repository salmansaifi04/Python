from tkinter import *
import tkinter.messagebox as tmsg

def help():
    print("I will help you")
    tmsg.showinfo("Help", "I will help you")
    # tmsg.showerror('error', 'error')
    # tmsg.showwarning('warning', 'warning')

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)


def divya():
    ans = tmsg.askretrycancel("Divya se dosti kar lo", "Sorry divya nahi banegi aapki dost")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")

    else:
        print("Bahut badiya bhai cancel kar diya warna pitte")




top = Tk()
top.geometry('600x400')
top.title('menu , submenu, message box')

mainmenu = Menu(top)

# submenu 1
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='New Project')
m1.add_command(label='Save')
m1.add_separator()
m1.add_command(label='Save As')
m1.add_command(label='Print')
top.config(menu=mainmenu)
mainmenu.add_cascade(label='File', menu=m1)


# submenu 2
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='Cut')
m2.add_command(label='Copy')

m2.add_separator()   # add file between the text

m2.add_command(label='Paste')
m2.add_command(label='Find')
top.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit', menu=m2)


# submenu 3
m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label='Help', command=help)
m3.add_command(label='Rate us', command=rate)
m3.add_command(label = "Befriend Divya", command=divya)

top.config(menu=mainmenu)
mainmenu.add_cascade(label='Help', menu=m3)



top.mainloop()