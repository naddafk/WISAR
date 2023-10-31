import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       button = tk.Button(self, text="Radar 1")
       button.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       button = tk.Button(self, text="Jimmy")
       button.pack(side="top", fill="both", expand=True)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       Label = tk.Label(self, text="Jimmy Status")
       Label.pack(side="top", fill="both", expand=True)       


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=100, y=250, height = 45, width= 300)
        p2.place(in_=container, x=100, y=250, height = 45, width= 300)
        p3.place(in_=container, x=100, y=250, height = 45, width= 300)
        
        radarbtn= tk.Button(root,text="View Radar", font= ('Arial', 25), command=p1.show)
        radarbtn.place(x=100, y=140, height = 45, width= 300)
        
        firebtn= tk.Button(root,text="Find Firefighters", font= ('Arail', 25),command=p2.show )
        firebtn.place(x=100, y=200, height = 45, width= 300)


        p1.show()



if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x450")
    root.mainloop()