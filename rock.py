import random

def play_rps():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    

    while True:
        player = input("Enter your rock, paper, or scissors (or 'q' to quit): ").lower()

        if player == 'q':
            print("👋 Thanks for playing!")
            break

        if player not in choices:
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"🤖 Computer chose: {computer}")

        if player == computer:
            print("🤝 It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("🎉 You win!")

        else:
            print("😢 You lose!")

play_rps()