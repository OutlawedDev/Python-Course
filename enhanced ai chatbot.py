print("hello i am an ai chatbot how can i help you today")

name = input("enter your name ")
print("hi", name)

chatting = True

while chatting:
    print("how are you feeling today")
    mood = input("tell me your mood ").lower()

    if mood == "happy":
        print("that is great")
    elif mood == "sad":
        print("i am sorry you feel sad")
    elif mood == "angry":
        print("being angry can be hard")
    elif mood == "tired":
        print("you should try to rest")
    else:
        print("thank you for telling me")

    print("what do you want to talk about")
    print("1 hobbies")
    print("2 school")
    print("3 weather")
    print("4 just talk")

    choice = input("pick a number ")

    if choice == "1":
        hobby = input("what is your favorite hobby ").lower()
        print("that sounds fun i like", hobby)

    elif choice == "2":
        subject = input("what subject do you like ").lower()
        print(subject, "is interesting")

    elif choice == "3":
        weather = input("how is the weather ").lower()
        print(weather, "weather can change how you feel")

    elif choice == "4":
        print("sometimes it is nice to talk")

    else:
        print("i do not understand that")

    again = input("do you want to keep talking yes or no ").lower()
    if again != "yes":
        chatting = False
        print("bye", name, "thanks for talking to me")
