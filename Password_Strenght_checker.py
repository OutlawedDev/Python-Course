import tkinter as tk

def check_password():
    pwd = box_pass.get()
    new = tk.Toplevel(win)
    new.title("Password Check")
    if len(pwd) < 5:
        msg = "Weak Password"
    elif len(pwd) < 8:
        msg = "Medium Password"
    elif any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd) and any(not c.isalnum() for c in pwd):
        msg = "Strong Password"
    else:
        msg = "Medium Password"
    tk.Label(new, text=msg).pack(padx=30, pady=20)

win = tk.Tk()
win.title("Password Strength Checker")

tk.Label(win, text="Enter Password").grid(row=0, column=0)
box_pass = tk.Entry(win, show="*")
box_pass.grid(row=0, column=1)

tk.Button(win, text="Check", command=check_password).grid(row=1, column=0, columnspan=2)

win.mainloop()
