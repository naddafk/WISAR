import tkinter as tk
from tkinter import*
root=tk.Tk()
import tkinter as tk                     
from tkinter import ttk 
from tkinter import*
from tkinter_webcam import webcam


def move_next_page():
    global count

    if not count > len(pages) - 2:

        for p in pages:
            p.pack_forget()
    
        count += 1
        page = pages[count]
        page.pack(pady=100)

def move_back_page():
    global count

    if not count == 0:

        for p in pages:
            p.pack_forget()
    
        count -= 1
        page = pages[count]
        page.pack(pady=100)


bottom_frame = tk.Frame(root)




root.geometry("500x400")
root.title("Tkinter Hub")

main_frame = tk.Frame(root, bg= "white")

page_1 = tk.Frame(main_frame)

Label(page_1, text= "Welcome To", bg= "white", font=("Maiandra GD", 20))
Label(page_1, text= "WISAR", bg = "white", font= ("Maiandra GD", 20))

page_2 = tk.Frame(main_frame)
page_2_lb = tk.Label(page_2, text= "Radar1", bg= "white", font= ("Maiandra GD", 80))
def Tabs(root):
    root.geometry("500x450")
    root.title("Radars") 
    tabControl = ttk.Notebook(root) 
  
    Radar1 = ttk.Frame(tabControl) 
    Radar2 = ttk.Frame(tabControl) 
    Radar3 = ttk.Frame(tabControl) 
    Radar4 = ttk.Frame(tabControl) 
  
    tabControl.add(Radar1, text ='Radar1') 
    tabControl.add(Radar2, text ='Radar2') 
    tabControl.add(Radar3, text ='Radar3') 
    tabControl.add(Radar4, text ='Radar4') 
    tabControl.pack(expand = 1, fill ="both") 
   


    ttk.Label(Radar1, text ="House On Fire", font = ('Maiandra GD', 32), width=20).grid(column = 0,  row = 0, padx = 30, pady = 30)
    ttk.Label(Radar2, text ="House Not On Fire", font = ('Maiandra GD', 32), width=20).grid(column = 0, row = 0,  padx = 30, pady = 30) 
    ttk.Label(Radar3, text ="House On Fire", font = ('Maiandra GD', 32), width=20).grid(column = 0,  row = 0, padx = 30, pady = 30)   
    ttk.Label(Radar4, text ="House Not On Fire", font = ('Maiandra GD', 32), width=20).grid(column = 0, row = 0,  padx = 30, pady = 30)




def fun_Tabs():
    root=Tk()
    Tabs(root)
    root.mainloop() 
page_2_lb.pack()

page_3 = tk.Frame(main_frame)
page_3_lb = tk.Label(page_3, text = "Menu", bg = "white", font= ("Maiandra GD", 20))
page_3_lb.pack()

page_4 = tk.Frame(main_frame)
page_4_lb = tk.Label(page_4, text= "About", bg= "white", font= ("Maiandra GD", 20))
page_4_lb.pack()

main_frame.pack(fill=tk.BOTH, expand=True)

pages = [page_1, page_2, page_3, page_4]
count = 0


def move_next_page():
    global count

    if not count > len(pages) - 2:

        for p in pages:
            p.pack_forget()
    
        count += 1
        page = pages[count]
        page.pack(pady=100)

#def move_back_page():
   #global count

    #if not count == 0:

     #   for p in pages:
         #   p.pack_forget()
    
        #count -= 1
        #page = pages[count]
        #page.pack(pady=100)


#bottom_frame = tk.Frame(root)

#back_btn = tk.Button(text= "Back", font=("Maiandra GD", 12),bg="white", fg= "black", width= 8,command=move_back_page) 
#back_btn.pack(side=tk.LEFT, padx=10)
#back_btn.place(x=27,y=70, height = 45, width=140)


Radar_btn = tk.Button(text= "View Radars", font=("Maiandra GD", 12),bg= "white", fg= "black", width= 8,command=move_next_page)
Radar_btn.pack(side=tk.RIGHT, padx=10)
Radar_btn.place(x=115, y=150, height = 45, width= 300)

Fire_btn = tk.Button(text= "Find Firefighters", font=("Maiandra GD", 12),bg= "white", fg= "black", width= 8,command=move_next_page)
Fire_btn.pack(side=tk.RIGHT, padx=10)
Fire_btn.place(x=115, y=230, height = 45, width= 300)

bottom_frame.pack(side=tk.BOTTOM, pady=10)

root.mainloop()

