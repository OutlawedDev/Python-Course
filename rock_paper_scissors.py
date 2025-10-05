import tkinter as tk
import random

def play(choice):
    user = choice
    comp = random.choice(["rock", "paper", "scissors"])
    if user == comp:
        result = "its a tie"
    elif (user == "Rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        result = "you win"
    else:
        result = "computer wins"
    result_label.config(text=f"You: {user}\nComputer: {comp}\n{result}")

win = tk.Tk()
win.title("rock paper scissors")

tk.Label(win, text="Choose one:").pack()

tk.Button(win, text="Rock", command=lambda: play("rock")).pack()
tk.Button(win, text="Paper", command=lambda: play("paper")).pack()
tk.Button(win, text="Scissors", command=lambda: play("scissors")).pack()

result_label = tk.Label(win, text="")
result_label.pack()

win.mainloop()
