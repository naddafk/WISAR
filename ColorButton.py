import tkinter as tk
import random
from Finputname import*
root=tk.Tk
class App(tk.Frame):

    def __init__(self,):
            
        super().__init__()

        self.master.title("New Firefighters")

        self.count = 0
        self.labels = {}

        self.init_ui()

    def init_ui(self):

        self.f = tk.Frame()

        w = tk.Frame()

        tk.Button(w, text="Add Firefighter", command=self.callback).pack()
        tk.Button(w, text="Close", command=self.on_close).pack()

        w.pack(side=tk.RIGHT, fill=tk.BOTH, expand=0)
        self.f.pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    def callback(self):

        text_button = "Firefighter {}".format(self.count)
        #tk.Button(self.f,text=text_button,command=lambda which=self.count: self.change_color(which)).pack()
        tk.Button(self.f,text=text_button,command= lambda : change(Firefighters)).grid()
        self.count +=1

    
    def on_close(self):
        self.master.destroy()


def change(root):
     if root.__name__ == "Firefighters":
          fun_fire()
    

if __name__ == '__main__':
    app = App()
    app.mainloop()