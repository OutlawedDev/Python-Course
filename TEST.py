import tkinter as tk

window = tk.Tk()
window.title("Eventss")
window.geometry("250x150")

def handle_keypess(event):
    print("Key pressed:", event.char)


window.bind("<Key>", handle_keypess)

def handle_Click(event):
    print("\nThe Button was clicked!")


button = tk.Button(window, text = "Click me!")
button.pack(pady=20)

button.bind("<Button-1>", handle_Click)

window.mainloop()