import tkinter as tk
from datetime import date
root = tk.Tk()
root.title("simple gui")
root.geometry('300x200')

lvl = tk.Label(root, text = "hello", fg = "white", bg = "#74A4F2", height = 1, width = 30)
lvl.pack()



name_lvl = tk.Label(root, text = "full name: ", bg = "#EF9D47", fg = "white")
name_lvl.pack()

name_entry= tk.Entry(root)
name_entry.pack()

def display():
    name = name_entry.get()
    global message
    message ="welcome to my rlly good User Interface \nToday's date is: "
    greet = "Hello" + name + "\n"

    text_box.insert(tk.END, greet)
    text_box.insert(tk.END, message)
    text_box.insert(tk.END, date.today())


text_box = tk.Text(root, height = 3)
text_box.pack()


btn = tk.Button(root, text = "begin", command = display, bg = "#B3F7BD")
btn.pack()


root.mainloop()
