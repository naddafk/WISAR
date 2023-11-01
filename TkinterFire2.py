from tkinter import*
from tkinter import ttk
import tkinter as tk 
from tkinter_webcam import webcam
from BackButton2 import*
root=tk.Tk


def Firefighters(root):
    root.geometry("500x450")
    root.title("Firefighters")
    #backbtn= tk.Button(root,text="Back", font= ('Maiandra GD', 25))
    #backbtn.place(x=17, y=70, height = 45, width= 90)
    Label(root, text= "Firefighters", font = ('Maiandra GD', 32), width=20).grid() 
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=17, y=70, height = 45, width= 90)
    Button(root, text= "Jimmy 💗 68", bg = "crimson", fg = 'ghostwhite', font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Jimmy)).grid()
    Button(root, text= "Sarah  💗 83", bg = "crimson", fg = 'ghostwhite', font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Sarah)).grid()
    Button(root, text= "Luffy  💗 76", bg = "crimson",fg = 'ghostwhite', font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Luffy)).grid()
    Button(root, text= "Tom   💗 80",bg = "crimson", fg = 'ghostwhite', font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Tom)).grid()
    Button(root, text= "Blake  💗 94", bg = "crimson",fg = 'ghostwhite', font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Blake)).grid()
    Button(root, text= "Sam    💗 72",bg = "crimson",fg = 'ghostwhite',  font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Sam)).grid()
    Button(root, text= "Bob    💗 95",bg = "crimson",fg = 'ghostwhite',  font = ('Maiandra GD', 17) , width=20 , command= lambda : change(Bob)).grid()
    

def change(root):
     if root.__name__ == "Jimmy":
          fun_Jimmy()
     if root.__name__ == "Sarah":
          fun_Sarah()
     if root.__name__ == "Luffy":
          fun_Luffy()
     if root.__name__ == "Tom":
          fun_Tom()
     if root.__name__ == "Blake":
          fun_Blake()
     if root.__name__ == "Sam":
          fun_Sam()
     if root.__name__ == "Bob":
          fun_Bob()
    

    

def Jimmy(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()
  
def fun_Jimmy():
    Jimmy(root)
    
def Sarah(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()

def fun_Sarah():
    Sarah(root)

def Luffy(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()
    
    
def fun_Luffy():
    Luffy(root)


def fun_Tom():
    Tom(root)

def Tom(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()
        

def Blake(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()

def fun_Blake():
    Blake(root)


def Sam(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()

def fun_Sam():
    Sam(root)

def Bob(root):
    root= Toplevel()

    root.title("Webcam Live Feed")

    root.geometry("500x450")

    video = webcam.Box(root, width=500, height = 450)
    Button(root, text= "Back",  fg = 'black', command= root.destroy). place(x=10, y=60, height = 45, width= 90)
    video.show_frames()

    root.mainloop()

def fun_Bob():
    Bob(root)


def fun_fire():
    root=Tk()
    Firefighters(root)
    root.mainloop()
    






