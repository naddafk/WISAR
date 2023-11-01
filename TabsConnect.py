import tkinter as tk                    
from tkinter import ttk 
from tkinter import*
from tkinter_webcam import webcam

def change(root):
        if root.__name__ == "Tabs1":
            fun_Tabs1()
     


def Tabs1(root):
        root.geometry("500x450")
        root.title("Radars") 
        tabControl = ttk.Notebook(root) 
    
        Radar1 = ttk.Frame(tabControl) 
    
        tabControl.add(Radar1, text ='Radar1') 
        tabControl.pack(expand = 1, fill ="both") 
    
        Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)

        video = webcam.Box(Radar1, width=450, height=450)
        video.show_frames()
        root.mainloop()


def fun_Tabs1():
        root=Toplevel()
        Tabs1(root)
        root.mainloop() 


def Tabs2(root):
        root.geometry("500x450")
        root.title("Radars") 
        tabControl = ttk.Notebook(root) 
    
        Radar1 = ttk.Frame(tabControl) 
    
        tabControl.add(Radar1, text ='Radar2') 
        tabControl.pack(expand = 1, fill ="both") 
    
        video = webcam.Box(Radar1, width=450, height=450)
        video.show_frames()
        root.mainloop()

def fun_Tabs2():
        root=Toplevel()
        Tabs2(root)
        root.mainloop() 



