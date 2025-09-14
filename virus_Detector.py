import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Virus detector")
window.geometry("200x200")


def msg():
    messagebox.showwarning("Warning", "ALERT! STOPPPP VIRUS FOUND!!!!!!")


btn = tk.Button(window, text="Scan for virus", command= msg)
btn.pack(pady=20)

window.mainloop()