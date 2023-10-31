from tkinter import *
import cv2 
from PIL import Image, ImageTk 
  
 
vid = cv2.VideoCapture(0) 
  

width, height = 800, 600
  

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 
  
app = Tk() 
  
app.bind('<Escape>', lambda e: app.quit()) 
  

label_widget = Label(app) 
label_widget.pack() 
  
  
  
def Webcam(): 
  
    
    _, frame = vid.read() 
  
    
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
  
    
    captured_image = Image.fromarray(opencv_image) 
  
    
    photo_image = ImageTk.PhotoImage(image=captured_image) 
  
    
    label_widget.photo_image = photo_image 
  
    
    label_widget.configure(image=photo_image) 
  
     
    label_widget.after(10, Webcam) 
  

button1 = Button(app, text="Jimmy", command=Webcam) 
button1.pack() 
  
app.mainloop() 