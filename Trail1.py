from tkinter import*
import tkinter as tk
from tkinter import ttk 
from RadarT import*
from FireT import*

def start(root):
    root.title("Welcome To Wisar")
    root.geometry("605x450")
    Label(root, fg = "black" ,text=  "Welcome To",  font = ('Maiandra GD', 40), width=20).grid()
    Label(root, fg = "SpringGreen4" ,text=  "WISAR",  font = ('Maiandra GD', 40), width=20).grid()
    Button(root, bg = "floralwhite", text= "View Radars", font = ('Maiandra GD', 32) , width=20 , command= lambda : change(root)).grid()
    Button(root, bg = "floralwhite", text= "Find Firefighters", font = ('Maiandra GD', 32) , width=20 , command= lambda : change(root)).grid()



def change(Tabs):
    Tabs.destroy()
    fun_tabs()


def change(Firefighters):
    Firefighters.destroy()
    fun_fire()


def call():
    root=Tk()
    start(root)
    root.mainloop()


call()