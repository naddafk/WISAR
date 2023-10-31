import tkinter as tk 
from tkinter_webcam import webcam
from tkinter import*



root= Toplevel()

root.title("Webcam Live Feed")

root.geometry("500x450")

video = webcam.Box(root, width=500, height = 450)

video.show_frames()

root.mainloop()
