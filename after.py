import tkinter as tk


window = tk.Tk()
window.title("After class project")
window.geometry("300x300")

def convert():
    inches = entry.get()
    cm = float(inches) * 2.54
    label2 = tk.Label(window, text=f"{cm} cm")
    label2.pack(pady=10)


label1 = tk.Label(window, text="Enter length in inches:")
label1.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

btn = tk.Button(window, text="Convert", command=convert)
btn.pack(pady=10)


window.mainloop()
