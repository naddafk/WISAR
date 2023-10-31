import tkinter as tk
from tkinter import ttk

def Tabs(root):
    root = tk.Tk()
    root.geometry("500x450")
    root.title("Radars")
    tabControl = ttk.Notebook(root)

    Radar1 = ttk.Frame(tabControl)
    Radar2 = ttk.Frame(tabControl)
    Radar3 = ttk.Frame(tabControl)
    Radar4 = ttk.Frame(tabControl)

    tabControl.add(Radar1, text ='Radar1')
    tabControl.add(Radar2, text ='Radar2')
    tabControl.add(Radar3, text ='Radar3')
    tabControl.add(Radar4, text ='Radar4')
    tabControl.pack(expand = 1, fill="both")

    ttk.Label(Radar1, text ="House On Fire").grid(column = 0, row = 0, padx = 30, pady = 30)
    ttk.Label(Radar2, text ="House Not On Fire").grid(column = 0, row = 0, padx = 30, pady = 30)
    ttk.Label(Radar3, text ="House Is On Fire").grid(column = 0, row = 0, padx = 30, pady = 30)
    ttk.Label(Radar4, text ="House Is Not On Fire").grid(column = 0, row = 0, padx = 30, pady = 30)

def fun_Tabs():
    root=tk()
    Tabs(root)
    root.mainloop()