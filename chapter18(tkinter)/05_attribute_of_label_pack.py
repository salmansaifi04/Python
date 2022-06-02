from tkinter import *
top = Tk()
top.geometry('1100x700')
top.title("First Gui")

# Important Label Options
# text - adds the text
# bg - background
# fg - foreground  (textcolor)
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback singer and television personality. In a film career spanning \nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film \nproducer, and two Filmfare Awards for acting.nd rank with earnings of $37.7 million.''', bg='red', fg='white', font=('sans', 12, 'bold'), padx=50, pady=50, relief=GROOVE,  borderwidth=20)


# Important Pack options
# anchor = nw, ne
# side = top, bottom, left, right
# fill
# padx
# pady


# title_label.pack(anchor='nw')  # left-top
# title_label.pack(anchor='ne')  # right-top
# title_label.pack(side= 'bottom',anchor='se')    # right-bottom
# title_label.pack(side= 'bottom',anchor='sw')    # left-bottom
# title_label.pack(side= 'bottom', anchor='sw', fill=X) 
title_label.pack(side= 'left', fill=Y, padx=30, pady=40) 



top.mainloop()



#### Quick exercise ####
# from tkinter import *
# from tkinter.font import BOLD
# top = Tk()
# top.geometry('500x400')

# label = Label(top, text='Ready', bg='red', pady=20, font=("sans", 20, BOLD))
# label.pack(fill=X, anchor='se', side='bottom')



# top.mainloop()