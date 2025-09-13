import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Multiply Two Numbers")

tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate", command=calculate_product).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
