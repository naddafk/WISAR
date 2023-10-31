import tkinter as tk

class ForwardBack:



def __init__(self, root):
    self.root=root
    self.frame_list=[]
    self.frame_ctr=0
    for ctr in range(5):
    self.create_frame(ctr)

    btn_frame=tk.Frame(root)
    btn_frame.grid(row=50, column=0)
    tk.Button(btn_frame, text="Forward", bg="lightgreen",
    command=self.forward).grid(row=0, column=0)
    tk.Button(btn_frame, text="Previous", bg="pink",
    command=self.previous).grid(row=0, column=1)

    tk.Button(root, text="Quit", bg="orange",
    command=self.root.quit).grid(row=99, column=0,
    sticky="nsew")

    self.forward()  ## display beginning frame

def create_frame(self, ctr):
        bg_color=["yellow", "lightblue", "white",
                  "blue violet", "brown2"]
        fr=tk.Frame(root)
        tk.Label(fr, text="Label %d" % (ctr), width=10,
                 bg=bg_color[ctr]).grid(sticky="nsew")
        self.frame_list.append(fr)

def forward(self):
        for fr in self.frame_list:
            fr.grid_forget()
        self.frame_ctr += 1
        if self.frame_ctr > 4:
            self.frame_ctr = 0
        self.frame_list[self.frame_ctr].grid(row=0, column=0)

def previous(self):
        for fr in self.frame_list:
            fr.grid_forget()
        self.frame_ctr -= 1
        if self.frame_ctr < 0:
            self.frame_ctr = 4
        self.frame_list[self.frame_ctr].grid(row=0, column=0)

root=tk.Tk()
fb=ForwardBack(root)
root.mainloop()


