from tkinter import*
def Radars(root):
    root.geometry("500x450")
    root.title("Radars")
    Label(root, text= "Radars", font = ('Arial', 32), width=20).grid()
    Button(root, text= "Radars +", font= ('Arial', 20) , width=20 , command= lambda: change(root)).grid()
    Button(root, text= "Radars 1 \_/", font= ('Arial', 17) , width=20 , command= lambda: change(root)).grid()
    Button(root, text= "Radars 2 \_/", font= ('Arial', 17) , width=20 , command= lambda: change(root)).grid()
    Button(root, text= "Radars 3 \_/", font= ('Arial', 17) , width=20 , command= lambda: change(root)).grid()



    def fun_radars():
        root=Tk()
        Radars(root)
        root.mainloop()