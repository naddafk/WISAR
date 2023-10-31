from tkinter import*
from tkinter import ttk

import tkinter as tk
root=tk.Tk
from tkinter_webcam import webcam

def Firefighters(root):
    root.geometry("500x450")
    root.title("Firefighters")
    Label(root, text= "Firefighters", font= ('Arial', 32), width=20).grid()
    Button(root, text= "Jimmy", font = ('Arial', 17), width=20 , command= lambda: change(Jimmy)).grid()
    Button(root, text= "Sarah", font = ('Arial', 17), width=20 , command= lambda: change(Sarah)).grid()
    Button(root, text= "Luffy", font = ('Arial', 17), width=20 , command= lambda: change(Luffy)).grid()
    Button(root, text= "Tom", font = ('Arial', 17), width=20 , command= lambda: change(Tom)).grid()
    Button(root, text= "Blake", font = ('Arial', 17), width=20 , command= lambda: change(Blake)).grid()
    Button(root, text= "Sam", font = ('Arial', 17), width=20 , command= lambda: change(Sam)).grid()
    Button(root, text= "Bob", font = ('Arial', 17), width=20 , command= lambda: change(Bob)).grid()

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
    root.geometry("500x450")
    root.title("Firefighter")
    Label(root, text= "Jimmy's Status", font = ('Arial', 32), width=20).grid()


def fun_Jimmy():
    root=Tk()
    Jimmy(root)



def Sarah(root):
    root.geometry("500x450")
    root.title("Firefighter")
    Label(root, text="Sarah's Status", font = ('Arial', 32), width=20).grid()


def fun_Sarah():
    root=Tk()
    Sarah(root)


def Luffy(root):
    root.title("Webcam Live Feed")

    root.geometry("1300x500")

    video = webcam.Box(root, width=1300, height = 500)

    video.show_frames()

def fun_Luffy():
    root=Tk()
    Luffy(root)


def fun_Tom():
    root=Tk()
    Tom(root)

def Tom(root):
    root.geometry("500x450")
    root.title("Tom")
    Label(root, text= "Tom's Status", font = ('Arial', 32), width=20).grid()


def Blake(root):
    root.geometry("500x450")
    root.title("Firefighter")
    Label(root, text= "Blake's Status", font = ('Arial', 32), width=20).grid()

def fun_Blake():
    root=Tk()
    Blake(root)


def Sam(root):
    root.geometry("500x450")
    root.title("Firefighter")
    Label(root, text= "Sam's Status", font = ('Arial', 32), width=20).grid()

def fun_Sam():
    root.geomtry("500x450")
    root.title("Firefighter")
    Label(root, text= "Sam's Status", font = ('Arial', 32), width=20).grid()

def fun_Sam():
    root=Tk()
    Sam(root)


def Bob(root):
    root.geometry("500x450")
    root.title("Firefighter")
    Label(root, text= "Bob's Status", font = ('Arial', 32), width=20).grid()

def fun_Bob():
    root=Tk()
    Bob(root)


def fun_fire():
    root=Tk()
    Firefighters(root)
    root.mainloop()