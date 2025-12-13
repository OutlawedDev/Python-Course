print("Hello i am an AI chatbot. How can I assist you today?")

name = input("Please enter your name: ")

print(f"Hello, {name}")


print("How are you feeling today?")

print("Please describe your mood: ")
mood = input().lower()

if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I'm sorry to hear that")
else:
    print("Thank you for sharing your feelings with me.")