# from tkinter import *
# import tkinter.messagebox as tmsg
#
# def getdollar():
#     print(f"We have credited {myslider2.get()} dollars to your bank account")
#     tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")
#
#
# top = Tk()
# top.geometry('500x400')
# top.title('Tkinter - Slider')
#
#
# ## vertical slider
# # myslider = Scale(top, from_= 0 , to_= 100)
# # myslider.pack()
#
# Label(top, text="How many dollars do you want?").pack()
# ## horizontal slider
# myslider2 = Scale(top, from_= 0, to_=100, orient= HORIZONTAL,tickinterval=50)
# ## where to start
# # myslider2.set(32)
# myslider2.pack()
#
# Button(top, text="Get dollars!", pady=10, command=getdollar).pack()
#
# top.mainloop()





###  quick quiz ###
from tkinter import *
import tkinter.messagebox as msg

def rate_us():
    value =  f"Rated successfully, Thanks for rating us. You have rated us {r_slider.get()} points.\n"
    msg.askokcancel("Thanks for Rating Us", f"You have rated {r_slider.get()} points.")
    print(value)
    with open("Ratings.txt", "a") as f:
        f.write(value)


top = Tk()
top.geometry('400x200')
top.title('Resturaunt')

Label(top, text='Plz rate us now ... ',font='sans 16 bold').pack()

r_slider = Scale(top, from_= 0, to_=10,orient=HORIZONTAL)
r_slider.pack(pady=10)

Button(top, text='Rate us', command=rate_us).pack()


top.mainloop()







