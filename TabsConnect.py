import tkinter as tk                    
from tkinter import ttk 
from tkinter import*
from tkinter_webcam import webcam

def change(root):
        if root.__name__ == "Tabs1":
            fun_Tabs1()
        if root.__name__ == "Tabs2":
            fun_Tabs2()
        if root.__name__ == "Tabs3":
            fun_Tabs3()
        if root.__name__ == "Tab4":
            fun_Tabs4()
        


def Tabs1(root):
        root.geometry("500x450")
        root.title("Radars") 
        tabControl = ttk.Notebook(root) 
    
        Radar1 = ttk.Frame(tabControl) 
    
        tabControl.add(Radar1, text ='Radar1') 
        tabControl.pack(expand = 1, fill ="both") 
    
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
    
        Radar2 = ttk.Frame(tabControl) 
    
        tabControl.add(Radar2, text ='Radar1') 
        tabControl.pack(expand = 1, fill ="both") 
    
        video = webcam.Box(Radar2, width=450, height=450)
        video.show_frames()
        root.mainloop()


def fun_Tabs2():
        root=Toplevel()
        Tabs2(root)
        root.mainloop() 


def Tabs3(root):
        root.geometry("500x450")
        root.title("Radars") 
        tabControl = ttk.Notebook(root) 
    
        Radar3 = ttk.Frame(tabControl) 
    
        tabControl.add(Radar3, text ='Radar1') 
        tabControl.pack(expand = 1, fill ="both") 
    
        video = webcam.Box(Radar3, width=450, height=450)
        video.show_frames()
        root.mainloop()


def fun_Tabs3():
        root=Toplevel()
        Tabs3(root)
        root.mainloop() 

def Tabs4(root):
        root.geometry("500x450")
        root.title("Radars") 
        tabControl = ttk.Notebook(root) 
    
        Radar4 = ttk.Frame(tabControl) 
    
        tabControl.add(Radar4, text ='Radar1') 
        tabControl.pack(expand = 1, fill ="both") 
    
        video = webcam.Box(Radar4, width=450, height=450)
        video.show_frames()
        root.mainloop()


def fun_Tabs4():
        root=Toplevel()
        Tabs4(root)
        root.mainloop() 

