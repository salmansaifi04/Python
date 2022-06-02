from msilib.schema import ListBox
from tkinter import *

top = Tk()
top.geometry('600x400')
top.title('Tkinter - Scroll bar')

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2 scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(top)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(top, yscrollcommand = scrollbar.set)
# for i in range(555):
#     listbox.insert(END, f"item {i}")

# listbox.pack(fill="both",padx=22)
text = Text(top, yscrollcommand= scrollbar.set)
text.pack(fill='both')


# scrollbar.config(command=listbox.yview)
scrollbar.config(command=text.yview)


top.mainloop()