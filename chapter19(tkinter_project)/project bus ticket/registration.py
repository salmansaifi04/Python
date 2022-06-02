from tkinter import *
from tkinter import messagebox  
import os


## database connectivity start ###
def show():
    import pymysql as sql
    Full_name = fullname.get()
    user_name = username.get()
    email_id = emailadd.get()
    password = password_pass.get()
    confirm_password = confirmpass.get()
    
    
    if Full_name == '' or user_name == '' or email_id == '' or password == '' or confirm_password == '':
        messagebox.showerror('Error', 'Field not be empty !!!')
    elif password != confirm_password:
        messagebox.showerror('Error', 'password and confirm password must be same !!!')
    else:
        try:
            db = sql.connect(host='localhost', user='root', passwd='salman@123',db='registration_form_connectivity')
            cur = db.cursor()
            sq = "insert into login_details values('%s','%s','%s','%s','%s')"%(Full_name,user_name,email_id,password,confirm_password)
            cur.execute(sq)
            db.commit()

            fullname.set("")
            username.set('')
            emailadd.set('')
            password_pass.set('')
            confirmpass.set('')
            if db.commit == None:
                messagebox.showerror("error", "Invalid username")  
            else:
                messagebox.showinfo("Success","successfully register Now you can login")  
                # top.destroy()
                # os.system('python login.py')
        except Exception as e:
            messagebox.showerror("Error" , f"Error Due to : {str(e)}")


    


## database connectivity end ###
def login():
    top.destroy()
    os.system('python login.py')


top = Tk()
top.title("Welcome to my site")
top.geometry('630x580+100+30')
top.resizable(width=False, height=False)

f1 = Frame(top, height=80,  bg='black')
f1.pack(fill=X)


Label(f1,bg='black',text='Register here !!!', font='sans 18',fg='white').pack(pady=20)


f2 = Frame(top,height=460, width=630)
f2.place(x=0, y=80)

## variables
fullname = StringVar()
username = StringVar()
emailadd = StringVar()
password_pass = StringVar()
confirmpass = StringVar()


###### first label ######
l1 = Label(f2, text='Name', font=('sans', 16))
l1.place(x=50, y=30)

t1 = Entry(f2, width=27, font=('sans', 16),textvariable=fullname)
t1.place(x=250, y=30)
t1.focus()

# ###### second label ######
l2 = Label(f2, text='Username', font=('sans', 16))
l2.place(x=50, y=90)
t2 = Entry(f2, width=27,textvariable=username, font=('sans', 16))
t2.place(x=250, y=90)

# ###### third label ######
l3 = Label(f2, text='Email', font=('sans', 16))
l3.place(x=50, y=150)
t3 = Entry(f2, width=27,textvariable=emailadd, font=('sans', 16))
t3.place(x=250, y=150)

# ###### four label ######
l4 = Label(f2, text='Password', font=('sans', 16))
l4.place(x=50, y=210)
t4 = Entry(f2, width=27,textvariable=password_pass, font=('sans', 16))
t4.place(x=250, y=210)

# ###### four label ######
l5 = Label(f2, text='Confirm password', font=('sans', 16))
l5.place(x=50, y=270)
t5 = Entry(f2, width=27, font=('sans', 16),textvariable=confirmpass)
t5.place(x=250, y=270)


# ###### Registration Button ######
b1 = Button(f2, text='Register',bg='black',fg='white', font=('sans', 16), command=show)
b1.place(x=300, y= 330)

# ###### login Button ######
l6 = Label(f2, text='If you already have an account then you can login here', font="sans 14").place(x=50, y=420)
b2 = Button(f2, text='Login',bg="white",fg='black', font=('sans', 16), command=login)
b2.place(x=515, y= 415 )





top.mainloop()