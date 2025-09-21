import tkinter as tk

root = tk.Tk()
root.title("root window")
root.geometry("300x200")


def new_window():
    top = tk.Tk()
    top.title("new window")
    top.geometry("200x100")

    top.mainloop()



btn = tk.Button(root, text= "click this to open a new window", command=new_window)

btn.pack()
root.mainloop()