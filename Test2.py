from tkinter import*
from TkinterRadar import*
from TkinterFire import*
from tkinter import*
#from Jimmy import*


def start(root):
    root.geometry("500x450")
    root.title("Welcome to WISAR")

    #win = root
    #win.geometry("500x450")
    #win.title("Welcome to WISAR")

    #label1=Label(win, text="   ", font=('Maiandra GD', 32), fg='black')
    #label1.pack(side=LEFT, pady=15)

    #label2=Label(win, text="WISAR!", font=('Maiandra GD', 32), fg= "SpringGreen4")
    #label2.pack(side=RIGHT, pady=15)

    #label3=Label(win, text="Welcome to ", font=("Times",30,"bold"), bg='green')
    #label3.pack(side=LEFT, pady=15)
    
    #lab1 = Label(root, fg= "black" ,text= "Welcome to", font = ('Maiandra GD', 32), width=12, height=1).grid(row=0, column=0, pady = 0)
    lab1 = Label(root, fg= "black" ,text= "Welcome to", font = ('Maiandra GD', 32)).place(x=130, y=45)
    #lab1.pack(side='left', anchor='e', expand=True)
    #lab2 = Label(root, fg= "SpringGreen4" ,text= "WISAR!", font = ('Maiandra GD', 32), width=2, height=1).grid(row=0, column=1, pady = 0)
    lab2 = Label(root, fg= "SpringGreen4" ,text= "WISAR!", font = ('Maiandra GD', 32)).place(x=180, y=95)
    #lab2.pack(side='right', anchor='w', expand=True)
    but1 = Button(root, bg = "floralwhite", text= "View Radars", font= ('Maiandra GD', 32), width=13 , command= lambda : change(Tabs)).place(x=80, y=180)
    #but1.pack(side="bottom")
    but2 = Button(root, bg = "floralwhite", text= "Find Firefighters", font = ('Maiandra GD', 32) , width=13 , command= lambda : change(Firefighters)).place(x=80, y=300)
    #tagName = Text.tag_configure("red", fg = "red")
    #tagName = Text.highlight_pattern("Welcome", "red")

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