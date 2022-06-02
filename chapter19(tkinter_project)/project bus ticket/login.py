from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


## database connectivity start ###
def show():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', passwd='salman@123',db='registration_form_connectivity')
    cur = db.cursor()
    sq = ("select * from login_details where user_name='%s' and password = '%s'"%(t1.get(),t4.get()))
    cur.execute(sq)
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("error", "Invalid username,password")  
    else:
        messagebox.showinfo("Success","successfully login")  
        import os
        top.destroy()
        os.system('python home.py')
        


## database connectivity end ###
import os
def reg():
    top.destroy()
    os.system('python registration.py')




top = Tk()
top.title("Bus Ticket - Login")
top.geometry('630x680+0+0')
top.resizable(width=False, height=False)


f1 = Frame(top, height=80,  bg='skyblue')
f1.pack(fill=X)

Label(f1,bg='skyblue',text='eBusTicket - Bus Ticket Booking System', font='sans 18',fg='blue').pack(pady=20)


f2 = Frame(top,height=300, width=630)
f2.place(x=0, y=380)


#  Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("img_login.jpg"))

# Create a Label Widget to display the text or Image
label = Label(top, image = img)
label.pack()

###### first label ######
l1 = Label(f2, text='Username', font=('sans', 16))
l1.place(x=50, y=30)

t1 = Entry(f2, width=27, font=('sans', 16))
t1.place(x=250, y=30)
t1.focus()

# ###### second label ######
l4 = Label(f2, text='Password', font=('sans', 16))
l4.place(x=50, y=90)
t4 = Entry(f2, width=27, font=('sans', 16))
t4.place(x=250, y=90)


# ###### login Button ######
b1 = Button(f2, text='Login',bg="green",fg='white', font=('sans', 16), command=show)
b1.place(x=280, y= 150)


# ###### Registration Button ######
l6 = Label(f2, text='If you don\'t have an account then you can create here', font="sans 14").place(x=50, y=230)
b2 = Button(f2, text='register',bg="white",fg='black', font=('sans', 16), command=reg)
b2.place(x=515, y= 225)

top.mainloop()