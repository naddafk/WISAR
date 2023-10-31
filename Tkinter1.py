import tkinter as tk
root = tk.Tk()
root.geometry("500x450")
root.title("Tkinter # 1")

label = tk.Label(root, text="Welcome To WISAR", font = ('Times', 35))
label.pack(padx=6, pady=6)

radarbtn= tk.Button(root,text="View Radar", font= ('Times', 25))
radarbtn.place(x=90, y=130, height = 45, width= 300)


firebtn= tk.Button(root,text="Find Firefighters", font= ('Times', 25))
firebtn.place(x=90, y=200, height = 45, width= 300)

backbtn= tk.Button(root,text="Back", font= ('Times', 25))
backbtn.place(x=27, y=70, height = 45, width= 140)

root.mainloop()