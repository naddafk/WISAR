from tkinter import*
from TkinterTabs import*
from TkinterFire import*
#from Jimmy import*


def start(root):
    root.geometry("500x450")
    root.title("Welcome to WISAR")

    Button(root, text= "View Radars", font= ('Arial', 32), width=20 , command= lambda : change(Tabs)).grid()
    Button(root, text= "Find Firefighters", font = ('Arial', 32) , width=20 , command= lambda : change(Firefighters)).grid()



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