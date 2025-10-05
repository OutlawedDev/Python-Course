import tkinter as tk

def calculate_interest():
    money = float(money_box.get())
    rate = float(rate_box.get())
    time = float(time_box.get())
    simple = (money * rate * time) / 100
    comp = money * ((1 + rate / 100) ** time) - money
    result_label.config(text=f"Simple Interest: {simple:.2f}\nCompound Interest: {comp:.2f}")

win = tk.Tk()
win.title("Interest Calculator")

tk.Label(win, text="Money").grid(row=0, column=0)
tk.Label(win, text="Rate").grid(row=1, column=0)
tk.Label(win, text="Time").grid(row=2, column=0)

money_box = tk.Entry(win)
rate_box = tk.Entry(win)
time_box = tk.Entry(win)

money_box.grid(row=0, column=1)
rate_box.grid(row=1, column=1)
time_box.grid(row=2, column=1)

tk.Button(win, text="Calculate", command=calculate_interest).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(win, text="")
result_label.grid(row=4, column=0, columnspan=2)

win.mainloop()
