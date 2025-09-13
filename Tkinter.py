import tkinter as tk

window = tk.Tk()
window.geometry('250x300')


nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
   window.rowconfigure(i, weight=1, minsize = 50)
for j in range(3):
   window.columnconfigure(j, weight=1, minsize = 75)


for i in range(4):
   for j in range(3):
      frame = tk.Frame(
         master=window,
         relief=tk.SUNKEN,
         borderwidth=1
      )
      frame.grid(row=i, column=j, sticky="nsew")
      label = tk.Label(master=frame, text=str(nums[i][j]), bg = "#d0efff")
      label.pack(padx=3, pady=3, expand = True, fill ="both")

window.mainloop()
