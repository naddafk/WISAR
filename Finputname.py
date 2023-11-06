from tkinter import*
from tkinter import ttk
import tkinter as tk 
from tkinter_webcam import webcam
import tkinter as tk
import random
root=tk.Tk

def Firefighters(root):
    root.geometry("500x450")
    root.title("Firefighters")
    Label(root, text= "Firefighters", font = ('Maiandra GD', 32), width=20).grid() 
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=17, y=70, height = 45, width= 90)
    Button(root, text= "Firefighter1", font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Add_Firefighter)).grid()
    
def change(root):
     if root.__name__ == "Add_Firefighter":
          fun_Add()
    

def Add_Firefighter(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=5, y=20, height = 45, width= 90)
    video.show_frames()

    root.mainloop()
    
  
def fun_Add():
    Add_Firefighter(root)


def fun_fire():
    root=Tk()
    Firefighters(root)
    root.mainloop()
    






