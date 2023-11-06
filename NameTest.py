from tkinter import *

from tkinter import messagebox

top = Tk()


top.resizable(0,0)
top.geometry("300x250")
def CallBack():
   msg = messagebox.showinfo( "Hello Python", Button(text=('New Fire')))
def NewFire():
   A = Button(top, text = "Add Firefighter", command = CallBack)

   A.place(x = 50,y = 110)
  


NewFire()
top.mainloop()