import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Demoination Counter")
root.configure(bg="lightblue")
root.geometry("650x400")

upload = Image.open("cash.png")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)


label = tk.Label(root, image=image, bg="lightblue")
label.place(x=180, y=20)


label1 = tk.Label(root, text="hey welcome to denomination counter app", font=("Arial", 15), bg="lightblue")

label1.place(relx=0.5, y=340, anchor=tk.CENTER)

def msg():
    MsgBox = messagebox.showinfo("alert", "do you want to calculate denomination count?")
    if MsgBox == "ok":
        topwin()



button1 = tk.Button(root, text="let get started", command = msg, bg="brown", fg = "white")


button1.place(x=260, y = 360)


def topwin():
    top = tk.Toplevel()
    top.title("denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = tk.Label(top, text="Enter total amount", bg = "light grey", font=("Arial", 15))
    entry = tk.Entry(top)
    lbl = tk.Label(top, text = "here are number of notes for each denomination", bg = 'light grey', font=("Arial", 15))

    l1 = tk.Label(top, text = "2000", bg = "light grey", font=("Arial", 15))
    l2 = tk.Label(top, text = "500", bg = "light grey", font=("Arial", 15))
    l3 = tk.Label(top, text = "200", bg = "light grey", font=("Arial", 15))

    t1 = tk.Entry(top)
    t2 = tk.Entry(top)
    t3 = tk.Entry(top)


    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, tk.END)
            t2.delete(0, tk.END)
            t3.delete(0, tk.END)

            t1.insert(tk.END, str(note2000))
            t2.insert(tk.END, str(note500))
            t3.insert(tk.END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = tk.Button(top, text="calculate", command=calculator, bg="brown", fg="white")

    label.place(x=200, y= 50)
    entry.place(x=200, y= 80)
    btn.place(x=250, y=120)
    lbl.place(x=150, y=160)
    l1.place(x=150, y=200)
    l2.place(x=250, y=200)
    l3.place(x=350, y=200)
    t1.place(x=150, y=240)
    t2.place(x=250, y=240)
    t3.place(x=350, y=240)

    top.mainloop()

root.mainloop()

