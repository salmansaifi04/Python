from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import datetime



class lib_mang:
    def __init__(self,top):
        self.top = top
        self.top.title("Library Management system")
        self.top.geometry("1360x700+0+0")
        self.top.resizable(0,0)

        ## ------------ creating the variable -------------- ##
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.authorname_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.actualprice_var = StringVar()

        

        ### ---------- heading ------------ ###
        lblheading = Label(self.top, text = 'LIBRARY MANAGEMENT SYSYTEM', bg = 'powder blue', fg='green', bd=15, relief='ridge', font='sans 30 bold', padx=2, pady=6)
        lblheading.pack(side=TOP, fill=X)

        ### -------------- creating a main frame ---------------- ###
        main_frame = Frame(self.top, bd=10,relief='ridge', bg='powder blue')
        main_frame.place(x=0, y=90, width=1360, height=350)

        ### left frame ###
        left_frame = LabelFrame(main_frame,text = 'Library membership information', bg = 'powder blue', fg='green', bd=12, relief='ridge', font='sans 12 bold')
        left_frame.place(x=10, y=5, width=600, height=310)


        ## ---- left side frame --- ##
        ## creating label1 ##
        lblmember = Label(left_frame, text='Member Type', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=0, column=0, sticky=W)
        commember = ttk.Combobox(left_frame,font='sans 10 bold',textvariable=self.member_var, state='readonly', width=19)
        commember['value'] = ('Admin Staf', 'Student', 'Lecturer')
        commember.grid(row=0, column=1)

        ## crating label2 ##
        lblmember = Label(left_frame, text='PRN No.', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=1, column=0, sticky=W)
        txtprn = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.prn_var)
        txtprn.grid(row=1, column=1)

        ## crating label3 ##
        lblmember = Label(left_frame, text='ID No.', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=2, column=0, sticky=W)
        txtid = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.id_var)
        txtid.grid(row=2, column=1)

        ## crating label4 ##
        lblmember = Label(left_frame, text='First Name', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=3, column=0, sticky=W)
        txt_first_name = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.firstname_var)
        txt_first_name.grid(row=3, column=1)

        ## crating label5 ##
        lblmember = Label(left_frame, text='Last Name', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=4, column=0, sticky=W)
        txt_last_name = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.lastname_var)
        txt_last_name.grid(row=4, column=1)

        ## crating label6 ##
        lblmember = Label(left_frame, text='Address1', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=5, column=0, sticky=W)
        txt_address1 = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.address1_var)
        txt_address1.grid(row=5, column=1)

        ## crating label7 ##
        lblmember = Label(left_frame, text='Address2', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=6, column=0, sticky=W)
        txt_address2 = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.address2_var)
        txt_address2.grid(row=6, column=1)

        ## crating label8 ##
        lblmember = Label(left_frame, text='Post code', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=7, column=0, sticky=W)
        txt_post_code = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.postcode_var)
        txt_post_code.grid(row=7, column=1)

        ## crating label9 ##
        lblmember = Label(left_frame, text='Mobile No.', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=8, column=0, sticky=W)
        txt_mobile = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.mobile_var)
        txt_mobile.grid(row=8, column=1)

        ## ----- right side frame ---- ##
        ## creating label1 ##
        lblmember = Label(left_frame, text='Book Id : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=0, column=3, sticky=W)
        txt_book_id = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.bookid_var)
        txt_book_id.grid(row=0, column=4)
        
        ## creating label2 ##
        lblmember = Label(left_frame, text='Book Title : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=1, column=3, sticky=W)
        txt_book_title = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.booktitle_var)
        txt_book_title.grid(row=1, column=4)
        
        ## creating label3 ##
        lblmember = Label(left_frame, text='Author Name : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=2, column=3, sticky=W)
        txt_author_name = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.authorname_var)
        txt_author_name.grid(row=2, column=4)
        
        
        ## creating label4 ##
        lblmember = Label(left_frame, text='Date Borrowed : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=3, column=3, sticky=W)
        txt_date_borrowed = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.dateborrowed_var)
        txt_date_borrowed.grid(row=3, column=4)
        
        
        ## creating label4 ##
        lblmember = Label(left_frame, text='Date Due : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=4, column=3, sticky=W)
        txt_date_due = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.datedue_var)
        txt_date_due.grid(row=4, column=4)
        
        
        ## creating label4 ##
        lblmember = Label(left_frame, text='Days On Book : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=5, column=3, sticky=W)
        txt_days = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.daysonbook_var)
        txt_days.grid(row=5, column=4)
        
        
        ## creating label4 ##
        lblmember = Label(left_frame, text='Late Return Fine : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=6, column=3, sticky=W)
        txt_late_fine = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.latereturnfine_var)
        txt_late_fine.grid(row=6, column=4)
        
        
        ## creating label4 ##
        lblmember = Label(left_frame, text='Date Over Due : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=7, column=3, sticky=W)
        txt_over_date = Entry(left_frame,font='sans 10 bold',width=22, textvariable=self.dateoverdue_var)
        txt_over_date.grid(row=7, column=4)
        
        
        ## creating label4 ##
        lblmember = Label(left_frame, text='Actual Price : ', font='sans 10 bold', bg='powder blue', pady=5, padx=2)
        lblmember.grid(row=8, column=3, sticky=W)
        txt_actual_price = Entry(left_frame,font='sans 10 bold',width=22,textvariable=self.actualprice_var)
        txt_actual_price.grid(row=8, column=4)
        

        ### ------- right frame ---------- ###
        right_frame = LabelFrame(main_frame,text = 'Books Details', bg = 'powder blue', fg='green', bd=12, relief='ridge', font='sans 12 bold')
        right_frame.place(x=624, y=5, width=700, height=310)

        ## creating a scroll bar ##
        list_scroll_bar = Scrollbar(right_frame)
        list_scroll_bar.grid(row=0, column=1, sticky='ns',pady=6)


        ## creating book list ##
        books_list = ['Head Firt Book','Learn Pyhton The Hard Way', 'Python Programming', 'Secrete Rahshy', 'Python CoockBook','Intro to Machine Learning','Fluent Python', 'Machine tecno', 'My Python', 'Joss Ellif guru', 'Elite  Jungle Python', 'Jungli Python', 'Mumbai Python', 'Pune Python', 'Machine Python', 'Adavance Python', 'Inton Python', 'Redchilli Pyhton']

        ## define the select function ##
        def SelectBook(event=""):
            value = str(list_box.get(list_box.curselection()))
            x = value
            if (x == 'Head Firt Book'):
                self.bookid_var.set('Bkid123')
                self.booktitle_var.set('Python Manual')
                self.authorname_var.set('Paul Berry')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.daysonbook_var.set(15)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs 30")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs 800")


        ## Creating a list box (left side) ##
        list_box = Listbox(right_frame, font='sans 10 bold', width=30, height=15,selectmode="SINGLE")
        list_box.bind('<<ListboxSelect>>', SelectBook)
        list_box.grid(row=0, column=0, padx=10, pady=6)
        list_scroll_bar.config(command=list_box.yview)    

        for item in books_list:
            list_box.insert(END,item)

        
        ## Creating a text box (right side) ##
        self.txt_box = Text(right_frame, font='sans 8 bold', width=56, height=18)
        self.txt_box.grid(row=0, column=2, padx=10, pady=6)


        ### ----------------- creating a button frame -------------------------- ###
        button_frame = Frame(self.top, bd=10,relief='ridge', bg='powder blue')
        button_frame.place(x=0, y=440, width=1360, height=70)

        ### creating button 1 (add data) ###
        btn_add_data = Button(button_frame, text='Add Data', font='sans 12 bold', width=20, command=self.add_data, fg='white', bg='blue')
        btn_add_data.grid(row=0, column=0, pady=8, padx=10)

        ### creating button 2 (show data)###
        btn_show_data = Button(button_frame, command=self.show_data, text='Show Data', font='sans 12 bold', width=20, fg='white', bg='blue')
        btn_show_data.grid(row=0, column=1, pady=8, padx=10)

        ### creating button 3 (Update data) ###
        btn_update_data = Button(button_frame,command=self.update, text='Update Data', font='sans 12 bold', width=20, fg='white', bg='blue')
        btn_update_data.grid(row=0, column=3, pady=8, padx=10)

        ### creating button 4 (Delete data) ###
        btn_dlt_data = Button(button_frame, command=self.dlt ,text='Delete Data', font='sans 12 bold', width=20, fg='white', bg='blue')
        btn_dlt_data.grid(row=0, column=4, pady=8, padx=10)

        ### creating button 5 (Reset data) ###
        btn_reset_data = Button(button_frame ,command=self.reset_data ,text='Reset Data', font='sans 12 bold', width=20, fg='white', bg='blue')
        btn_reset_data.grid(row=0, column=5, pady=8, padx=10)

        ### creating button 6 (Exit button) ###
        btn_exit_data = Button(button_frame,command=self.i_exit ,text='Exit', font='sans 12 bold', width=16, fg='white', bg='blue')
        btn_exit_data.grid(row=0, column=6, pady=8, padx=10)



        ### ----------------- creating a sql data frame -------------------------- ###
        sql_frame = Frame(self.top, bd=10,relief='ridge', bg='powder blue')
        sql_frame.place(x=0, y=510, width=1360, height=190)

        table_frame = Text(sql_frame,bd=4, relief='ridge', bg='powder blue',cursor="arrow")
        table_frame.place(x=0, y=2, width=1340, height=170)

        ## creating scroll bar ##
        xscroll =   ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll =   ttk.Scrollbar(table_frame,orient=VERTICAL)


        ## creating a tree view ##
        self.library_table = ttk.Treeview(table_frame, columns=("membertype","prnno","idno","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author", "dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("idno", text="ID No.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post code")
        self.library_table.heading("mobile", text="Mobile No.")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author Name")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days on book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Actual Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill='both', expand=1)

        ## width adjust ##
        
        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("idno", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    ### ---------- define the add data function ------------- ###
    def add_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="salman@123", database="library_management")
        my_cur = conn.cursor()
        my_cur.execute("insert into library_record values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(
                    self.member_var.get(),
                    self.prn_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.authorname_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook_var.get(),
                    self.latereturnfine_var.get(),
                    self.dateoverdue_var.get(),
                    self.actualprice_var.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Memeber has been inserted successfully")
    
    ## define the update function ##
    def update(self):
        conn = pymysql.connect(host="localhost", user="root", password="salman@123", database="library_management")
        my_cur = conn.cursor()
        my_cur.execute("update library_record set member='%s',id='%s' ,first_name='%s' ,last_name='%s',address1='%s',address2='%s',post_code='%s',mobile='%s',bookid='%s',booktitle='%s',author_name='%s',date_borrowed='%s',date_due='%s',days_on_book='%s',late_return_fine='%s',date_over_due='%s', actual_price='%s' where prn_no = '%s'"%(
                    self.member_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.authorname_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook_var.get(),
                    self.latereturnfine_var.get(),
                    self.dateoverdue_var.get(),
                    self.actualprice_var.get(),
                    self.prn_var.get(),
            ))
        
        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")



    ## fetch data to the bottom table ##
    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="salman@123", database="library_management")
        my_cur = conn.cursor()
        my_cur.execute("select * from library_record")
        rows = my_cur.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    ## cursor click ##
    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.authorname_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.actualprice_var.set(row[17])

    ## show data function ##    
    def show_data(self):
        self.txt_box.insert(END, "Member Type : \t \t" + self.member_var.get() + "\n")
        self.txt_box.insert(END, "PRN No. : \t \t" + self.prn_var.get() + "\n")
        self.txt_box.insert(END, "ID No. : \t \t" + self.id_var.get() + "\n")
        self.txt_box.insert(END, "First name : \t \t" + self.firstname_var.get() + "\n")
        self.txt_box.insert(END, "Last name : \t \t" + self.lastname_var.get() + "\n")
        self.txt_box.insert(END, "Address1 : \t \t" + self.address1_var.get() + "\n")
        self.txt_box.insert(END, "Address2 : \t \t" + self.address2_var.get() + "\n")
        self.txt_box.insert(END, "Post_code : \t \t" + self.postcode_var.get() + "\n")
        self.txt_box.insert(END, "Mobile_no. : \t \t" + self.mobile_var.get() + "\n")
        self.txt_box.insert(END, "Book_Id : \t \t" + self.bookid_var.get() + "\n")
        self.txt_box.insert(END, "Book_Title : \t \t" + self.booktitle_var.get() + "\n")
        self.txt_box.insert(END, "Author_Name : \t \t" + self.authorname_var.get() + "\n")
        self.txt_box.insert(END, "Date_Borrowed : \t \t" + self.dateborrowed_var.get() + "\n")
        self.txt_box.insert(END, "Date_Due : \t \t" + self.datedue_var.get() + "\n")
        self.txt_box.insert(END, "Days_On_Book : \t \t" + self.daysonbook_var.get() + "\n")
        self.txt_box.insert(END, "Late_Return_Fine : \t \t" + self.latereturnfine_var.get() + "\n")
        self.txt_box.insert(END, "Date_Over_Due : \t \t" + self.dateoverdue_var.get() + "\n")
        self.txt_box.insert(END, "Actual_Price : \t \t" + self.actualprice_var.get() + "\n")

    ## reset the data function ##
    def reset_data(self):
        self.member_var.set(""),
        self.id_var.set(""),
        self.prn_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.authorname_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set(""),
        self.txt_box.delete("1.0",END)

    ## exit function ##
    def i_exit(self):
        x = messagebox.askyesno("Library Management System","Do you want to exit")
        if x==YES:
            self.top.destroy()

    ## delete function ##
    def dlt(self):
        if self.prn_var.get() == "" or self.id_var.get()=="":
            messagebox.showerror("Error", "First select the member")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="salman@123", database="library_management")
            my_cur = conn.cursor()
            my_cur.execute("delete from library_record where prn_no = '%s'"%(self.prn_var.get()))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")           


if __name__ == "__main__":
    top = Tk()
    obj = lib_mang(top)
    top.mainloop()


