from tkinter import *
from PIL import Image, ImageTk

## database connectivity start ###
def show():
    import pymysql as sql
    first_name = t1.get()
    last_name = t2.get()
    email_id = t3.get()
    password = t4.get()
    db = sql.connect(host='localhost', user='root', passwd='salman@123',db='registration_form_connectivity')
    cur = db.cursor()
    sq = "insert into reg_info values('%s','%s','%s','%s')"%(first_name,last_name,email_id, password)
    cur.execute(sq)
    db.commit()


## database connectivity end ###

import os
def home():
    top.destroy()
    os.system('python home.py')


def about():
    top.destroy()
    os.system('python about.py')

def services():
    top.destroy()
    os.system('python services.py')

def contact():
    top.destroy()
    os.system('python contact.py')



top = Tk()
top.title("Welcome to my site")
top.geometry('1300x700')
top.minsize(width=1300, height=700)
top.maxsize(width=1300, height=700)

f1 = Frame(top, height=80,  bg='black')
f1.pack(fill=X)


# buttons
Label(f1,bg='black',text='Travelling', font='sans 18',fg='white').pack(padx=200,side='left')
Button(f1,text='Home', font='sans 14',command=home).pack(side='left',padx=50, pady=20)
Button(f1,text='About', font='sans 14',command=about).pack(side='left',padx=50, pady=20)
Button(f1,text='Services', font='sans 14',command=services).pack(side='left',padx=50, pady=20)
Button(f1,text='Contact Us', font='sans 14',command=contact,bg='black',borderwidth=0,fg='white').pack(side='left',padx=50, pady=20)


f2 = Frame(top, height=500, width=1300)
f2.pack(pady=30)

f3 = Frame(f2, height=500, width=580)
f3.pack(side=LEFT, fill=Y)
# image
img = ImageTk.PhotoImage(Image.open('contact.jpg'))
Label(f3,image=img).pack()


f4 = Frame(f2, height=500, width=710,)
f4.pack(side=RIGHT, fill='both')

# -------
#############

l = Label(f4, text='Register Here !!!', font='sans 22 bold',width=710)
l.pack(pady=20)

###### first label ######
l1 = Label(f4, text='Firstname', font=('sans', 16))
l1.place(x=60, y= 130)

t1 = Entry(f4, width=30, font=('sans', 16))
t1.place(x=220, y= 130)

# ###### second label ######
l2 = Label(f4, text='Lastname', font=('sans', 16))
l2.place(x=60, y= 210)
t2 = Entry(f4, width=30, font=('sans', 16))
t2.place(x=220, y= 210)

# ###### third label ######
l3 = Label(f4, text='Email', font=('sans', 16))
l3.place(x=60, y= 290)
t3 = Entry(f4, width=30, font=('sans', 16))
t3.place(x=220, y= 290)

# ###### four label ######
l4 = Label(f4, text='Password', font=('sans', 16))
l4.place(x=60, y= 370)
t4 = Entry(f4, width=30, font=('sans', 16))
t4.place(x=220, y= 370)

# ###### Button ######
b1 = Button(f4, text='Register',bg='green',fg='white', font=('sans', 16), command=show)
b1.place(x=520, y= 440)









f6 = Frame(top, height=80, width=1300, bg='black')
f6.pack(fill=X,anchor='se', side='bottom')

Label(f6, text='2022 Copyright || All Right Reserve', font='sans 16',bg='black', fg='white').pack(pady=10)


top.mainloop()