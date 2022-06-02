from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry 
import datetime
import pymysql as mysql




## define a submit function
def submit(): 
    total = 500
    total= total*entry_text.get()
    tax = total/18
    global sub_total
    sub_total = total+tax
    sub_var.set(sub_total)

    ## getting the values
    from_val = from_combo_var.get()
    to_val = to_combo_var.get()
    cal_val = cal.get()
    var_val = var.get()
    var1_val = var1.get()
    entry_val = entry_text.get()
    sub_val = sub_var.get()
    user_val = username.get()

    if from_val =='' or to_val == '' or cal_val == '' or var_val == 'None' or var1_val == 'None'or entry_val == 0 or sub_val == '':
        messagebox.showerror('Error', 'Field not be empty !!!')
    else:
        try:
            db = mysql.connect(user='root', host='localhost', password='salman@123', database='registration_form_connectivity')
            cur = db.cursor()    
            sq = "insert into ticket(from_city, to_city, journey_date, ticket_type, class, num_of_passenger, sub_total, user_name) values('%s','%s','%s','%s','%s','%s','%f','%s')"%(
            from_val,
            to_val,
            cal_val,
            var_val,
            var1_val,
            entry_val,
            sub_val,
            user_val
            )
            cur.execute(sq)
            db.commit()
            if db.commit == None:
                messagebox.showerror("error", 'something went wrong')
            else:
                total_var.set(total)
                tax_var.set(tax)
                sub_var.set(sub_total)
                messagebox.showinfo('Ticket Booking Confirm',"Thanks for Booking your ticket 'If you want to update, delete you can check on the right side'")
                
                from_combo_var.set('')
                to_combo_var.set('')
                cal.set_date(datetime.datetime.now())
                var.set(var.set("None"))
                var1.set(var1.set("None"))
                entry_text.set('')
                total_var.set('')
                tax_var.set('')
                sub_var.set('')
                total_var.set('')
                tax_var.set('')
                sub_var.set('')
        except Exception as e:
            messagebox.showerror("Error" , f"Error Due to : {str(e)}")


## login ###
def login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', passwd='salman@123',db='registration_form_connectivity')
    cur = db.cursor()
    sq = ("select * from login_details where user_name='%s' and password = '%s'"%(username.get(),pass_var.get()))
    cur.execute(sq)
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("error", "Invalid username,password")  
    else:
        submit()



## reset function
def reset():
    from_combo_var.set('')
    to_combo_var.set('')
    cal.set_date(datetime.datetime.now())
    var.set(var.set("None"))
    var1.set(var1.set("None"))
    entry_text.set('')
    total_var.set('')
    tax_var.set('')
    sub_var.set('')
    pass_var.set('')
    username.set('')
    er1.focus()


## check price function
def price():
    total = 500
    total= total*entry_text.get()
    tax = total/18
    global sub_total 
    sub_total = total+tax
    
    try:
        if sub_total == 0:
            messagebox.showwarning('Error','Please select the number of passenger ...')
        else:
            total_var.set(total)
            tax_var.set(tax)
            sub_var.set(sub_total)
    except Exception as e:
        messagebox.showerror("Error" , f"Error Due to : {str(e)}")



## quit_exit function
def quit_exit():
    res=messagebox.askquestion('Exit Application', 'Do you really want to exit')
    if res == 'yes' :
        top.destroy()




top = Tk()
top.geometry('1100x680+50+10')
top.title('Bus ticketing system')
top.resizable(height=False, width=False)

## variables
username = StringVar()
pass_var = StringVar()
from_combo_var = StringVar()
to_combo_var = StringVar()
var = StringVar()
var.set("None")
var1 = StringVar()
var1.set("None")
entry_text = DoubleVar()
entry_text.set(0)
total_var = DoubleVar()
tax_var = DoubleVar()
sub_var = DoubleVar()

# ----- main frame 1 -----
f1 = Frame(top,width=1350,height=80, bg='skyblue')
f1.pack(fill=X)

# header design "Label"
l1 = Label(f1, text='Bus Ticketing System', bg='skyblue', fg='white', font='sans 20 bold')
l1.pack(pady=10)

### main frame ----
lf1 = Frame(top)
lf1.pack(anchor="nw")

# ------ main frame 2 ---------
f2 = Frame(lf1,borderwidth=1, relief='solid')
f2.pack(anchor="nw",padx=30,pady=20,ipady=0,side='left')

## username ##
fr1 = Frame(f2)
fr1.pack(pady=10)

user_name = Label(fr1, text='user_name', font='lucida 14')
user_name.pack(side='left',padx=25)

er1 = Entry(fr1,width=26, textvariable=username)
er1.pack(side='left',padx=32)
er1.focus()


## password ##
fr2 = Frame(f2)
fr2.pack()

password = Label(fr2, text='password', font='lucida 14')
password.pack(side='left',padx=30)

er2 = Entry(fr2,width=26, textvariable=pass_var)
er2.pack(side='left',padx=35)

# --------- frame 3 --------
f3 = Frame(f2)
f3.pack(pady=5)


## from label ##
des_from = Label(f3, text='From City', font='lucida 14')
des_from.pack(side='left',padx=30)

## from combo box (drop down) ##

## variable declare for from city

combo_from = ttk.Combobox(f3,textvariable=from_combo_var,
values=
[
"Abohar, Punjab",
"Abu road, Rajasthan",
"Adipur, Gujarat",
"Agra, Uttar Pradesh",
"Ahmedabad Airport, Gujarat",
"Ahmedabad, Gujarat",
"Ahmednagar, Maharashtra",
"Ajmer, Rajasthan",
"Akbarpur, Uttar Pradesh",
"Allahabad, Uttar Pradesh",
"Alwar, Rajasthan",
"Aurangabad, Maharashtra",
"Ayodhya, Uttar Pradesh",
"Fatehpur Sikri, Rajasthan",
"Hapur, Uttar Pradesh"
], font='lucida 12',width=15,state='readonly')
combo_from.pack(side='right',padx=40)

## ---------- frame 4 -----------------
f4 = Frame(f2)
f4.pack(pady=10)

## to city label ##
des_to = Label(f4, text='To City', font='lucida 14')
des_to.pack(side='left',padx=40)

## from combo box (drop down) ##

## variable declare for to city

combo_to = ttk.Combobox(f4,textvariable=to_combo_var,
values=
[
"Abohar, Punjab",
"Abu road, Rajasthan",
"Adipur, Gujarat",
"Agra, Uttar Pradesh",
"Ahmedabad Airport, Gujarat",
"Ahmedabad, Gujarat",
"Ahmednagar, Maharashtra",
"Ajmer, Rajasthan",
"Akbarpur, Uttar Pradesh",
"Allahabad, Uttar Pradesh",
"Alwar, Rajasthan",
"Aurangabad, Maharashtra",
"Ayodhya, Uttar Pradesh",
"Fatehpur Sikri, Rajasthan",
"Hapur, Uttar Pradesh"
], font='lucida 12',width=15,state='readonly')
combo_to.pack(side='right',padx=30)

## Date of journey
f5 = Frame(f2)
f5.pack()

doj = Label(f5, text='Journey Date', font='lucida 14')
doj.pack(side='left',padx=12)

d1 = datetime.datetime.now()

cal = DateEntry(f5,width=23,selectmode='day',mindate=d1)
cal.pack(side='left',padx=30)

## ticket type ##
f6 = Frame(f2)
f6.pack(pady=10)

Tt = Label(f6, text='Ticket Type', font='lucida 14',width=15)
Tt.pack(side='left')
radio1 = Radiobutton(f6, text="One Way", padx=5, variable=var, value="oneway",font='lucida 12').pack(side=LEFT)
radio2 = Radiobutton(f6, text="Round Trip", padx=5, variable=var, value="roundtrip",font='lucida 12').pack(side=LEFT)

## class type ##
f7 = Frame(f2)
f7.pack()

ct = Label(f7, text='Class', font='lucida 14',width=15)
ct.pack(side='left')

radio = Radiobutton(f7, text="First Class", padx=5, variable=var1, value="firstclass",font='lucida 12').pack(side=LEFT)
radio = Radiobutton(f7, text="Economy", padx=5, variable=var1, value="economy",font='lucida 12').pack(side=LEFT)

## Number of passenger ##
f8 = Frame(f2)
f8.pack(pady=10)

no_passenger = Label(f8, text='No. of Passenger', font='lucida 14')
no_passenger.pack(side='left')


e1 = Entry(f8,width=25, textvariable=entry_text)
e1.pack(side='left',padx=20)


## ---- main frame 9 (Button) -----##
f9 = Frame(f2)
f9.pack(anchor="nw",pady=20,padx=50)


Button(f9, text='Check Price',font='lucida 12', bg='yellowgreen', fg='white',borderwidth=0,command=price).pack(ipadx=10,side='left',padx=10)

Button(f9, text='Submit',font='lucida 12', bg='green', fg='white',borderwidth=0,command=login).pack(ipadx=10,padx=10,side=LEFT)

Button(f9, text='Reset',font='lucida 12', bg='red', fg='white',borderwidth=0,command=reset).pack(ipadx=10,padx=10,side=LEFT)



## ---- main frame 10 bill -----##
f10 = Frame(f2,borderwidth=1, relief='solid')
f10.pack(anchor="nw",padx=30,pady=10)

## --- frame 11 ----
f11 = Frame(f10)
f11.pack(pady=10)
total_label = Label(f11,text='Total',font='lucida 14')
total_label.pack(side=LEFT, padx=50)

total_entry = Entry(f11,width=30,textvariable=total_var)
total_entry.pack(side=LEFT,padx=20)

total_entry.configure(state= "readonly")

## --- frame 12 ----
f12 = Frame(f10)
f12.pack()
tax_label = Label(f12,text='Tax',font='lucida 14')
tax_label.pack(side=LEFT, padx=55)

tax_entry = Entry(f12,width=30,textvariable=tax_var)
tax_entry.pack(side=RIGHT,padx=20)

tax_entry.configure(state= "readonly")

## --- frame 13 ----
f13 = Frame(f10)
f13.pack(pady=10)
sub_total_label = Label(f13,text='Sub Total',font='lucida 14')
sub_total_label.pack(side=LEFT, padx=30)

sub_total_entry = Entry(f13,width=30,textvariable=sub_var)
sub_total_entry.pack(side=LEFT,padx=25)

sub_total_entry.configure(state= "readonly")


### ----- confirm detail ----- ###
## ----- main frame right hand side ----- ##
rf1 = Frame(lf1,width=500, height=200, borderwidth=1, relief=SOLID)
rf1.pack(anchor='ne',side='top', padx=50, pady=20,ipady=15)

## Frame 1 - Title ##
rf2 = Frame(rf1)
rf2.pack()

title = Label(rf2, text='Check Your Details....', fg='green', font='lucida 16 bold')
title.pack(ipadx=200, pady=20)


## --- Frame 8 - button section ----- ##
rf10 = Frame(rf1)
rf10.pack(pady=30)

## button 1 - search
Button(rf10, text='Search', font='lucida 14', bg='red', fg='white',borderwidth=0,padx=15).pack(side=LEFT)  


# button 2 - update
Button(rf10, text='Update', font='lucida 14', bg='skyblue', fg='white',borderwidth=0,padx=15).pack(side=LEFT, padx=20) 


# button 2 - delete
Button(rf10, text='Delete', font='lucida 14', bg='skyblue', fg='white',borderwidth=0,padx=15).pack(side=LEFT, padx=20) 


## button 3 - exit
Button(rf10, text='Exit', font='lucida 14', bg='#b87906', fg='white',borderwidth=0,padx=15,command=quit_exit).pack(side=LEFT,padx=20) 


## footer section ##
last_frame = Frame(top, bg='skyblue')
last_frame.pack(fill=BOTH)

Label(last_frame, text='No Booking Charges !!!', fg='red', bg='skyblue', font='lucida 14 bold', pady=11).pack()





top.mainloop()





'''

SELECT 
    mydatabase1.tblUsers.UserID, 
    mydatabse2.tblUsers.UserID
FROM 
   mydatabase1.tblUsers
       INNER JOIN mydatabase2.tblUsers 
           ON mydatabase1.tblUsers.UserID = mydatabase2.tblUsers.UserID
'''