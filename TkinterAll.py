from tkinter import*  
#from TabsConnect import* 
from TkinterRad1 import*
from TkinterFire2 import*
from tkinter import*
from tkinter_webcam import webcam
import tkinter as tk


def start(root):
    root.geometry("605x450")
    root.title("Welcome To WISAR")
    Label(root, fg = "black" ,text=  "Welcome To",  font = ('Maiandra GD', 40), width=20).grid()
    Label(root, fg = "SpringGreen4" ,text=  "WISAR",  font = ('Maiandra GD', 40), width=20).grid()
    Button(root, bg = "floralwhite", text= "View Radars", font = ('Maiandra GD', 32) , width=20 , command= lambda : change(Tabs)).grid()
    Button(root, bg = "floralwhite", text= "Find Firefighters", font = ('Maiandra GD', 32) , width=20 , command= lambda : change(Firefighters)).grid()


def change(root):
     if root.__name__ == "Tabs":
          fun_Tabs()
     if root.__name__ == "Firefighters":
          fun_fire()
    
def call():
     root=Tk()
     start(root)
     root.mainloop()

call()