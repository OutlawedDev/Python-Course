import re
import tkinter as tk

def check_password_strength(password):
    length = len(password)
    
    if length == 0:
        return ""

    if length < 6:
        return "Very Weak"
    
    requirements_met = 0
    if length >= 8:
        requirements_met += 1
    if re.search(r"[a-z]", password):
        requirements_met += 1
    if re.search(r"[A-Z]", password):
        requirements_met += 1
    if re.search(r"\d", password):
        requirements_met += 1
    if re.search(r"[^a-zA-Z0-9]", password):
        requirements_met += 1

    if requirements_met == 5:
        return "Excellent"
    elif requirements_met == 4:
        return "Strong"
    elif requirements_met >= 2:
        return "Moderate"
    else:
        return "Weak"

def setup_gui():
    root = tk.Tk()
    root.title("Password Checker")
    root.geometry("350x150")
    root.resizable(False, False)

    def update_strength(event=None):
        password = password_entry.get()
        strength = check_password_strength(password)
        
        strength_label.config(text=strength)
        
        if not password:
            strength_label.config(text="Enter Password")

    header_label = tk.Label(root, text="Password Strength checker")
    header_label.pack(pady=10)

    input_frame = tk.Frame(root)
    input_frame.pack(pady=5)

    input_label = tk.Label(input_frame, text="Password:")
    input_label.pack(side=tk.LEFT, padx=5)

    password_var = tk.StringVar()
    password_entry = tk.Entry(input_frame, textvariable=password_var, show="*", width=30, relief=tk.SUNKEN)
    password_entry.pack(side=tk.LEFT, padx=5)
    password_entry.bind("<KeyRelease>", update_strength)

    strength_frame = tk.Frame(root)
    strength_frame.pack(pady=10)

    strength_title_label = tk.Label(strength_frame, text="Strength:")
    strength_title_label.pack(side=tk.LEFT, padx=10)

    strength_label = tk.Label(strength_frame, text="Enter Password", width=15, relief=tk.RIDGE)
    strength_label.pack(side=tk.LEFT, padx=10)

    update_strength()
    root.mainloop()

setup_gui()
