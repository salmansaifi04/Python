from tkinter import *
from PIL import ImageTk,Image  
top = Tk()

top.geometry('900x800')

## for png images
# photo = PhotoImage(file = "01.png") 

path = 'C:/Users/Admin/Downloads/6742e2bf4aada8adcd6f043b5fbc328a.png'

photo = ImageTk.PhotoImage(Image.open(path))  



img_label = Label(image = photo)
img_label.pack()

top.mainloop()

