import tkinter as tk

root = tk.Tk()
root.title("login app")
root.geometry("400x400")


frame = tk.Frame(master = root, height = 200, width = 360, bg="#35b5f5")


lbl1 = tk.Label(frame, text = "Full name", bg = "#3895D3", fg = "white", width = 12)
lbl2 = tk.Label (frame, text = "Email", bg = "#3895D3", fg = "white", width = 12)
lbl3 = tk.Label (frame, text = "Password", bg = "#3895D3", fg = "white", width = 12)


name_entry = tk.Entry(frame)
email_entry = tk.Entry(frame)
pass_entry = tk.Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "hey" +name
    message = "\nCongradulations! you have logged in"
    textbox.insert(tk.END, greet)
    textbox.insert(tk.END, message)

textbox = tk.Text(bg = "#ACE3FF", fg="black")

btn = tk.Button(text = "Create Account", command=display, bg="red") 

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()
