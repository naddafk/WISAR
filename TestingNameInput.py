import tkinter as tk
import tkinter.messagebox

def btn_clicked():
    b2 = tk.Button(text="Firefighter", borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")
    
    b2.place(x = 200, y = 200, width = 213,height = 72)

def btn_clicked1():
    b3 = tk.Button(text="Firefighter", borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")
    
    b3.place(x = 200, y = 200, width = 213,height = 72)

window = tk.Tk()

window.geometry("1000x600")
window.configure(bg = "#293335")

b1 = tk.Button(text='Add', borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")

b1.place(x = 5, y = 5,width = 213,height = 72)

window.resizable(False, False)
window.mainloop()