import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["New York", "Paris", "Tokyo"]
}

jokes = [
    "Why dont programmers like nature? It has too many bugs.",
    "Why do computers go to the doctor? Because they have a virus!",
    "why do travelers always feel warm? because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains or cities?")
    prefrence = input(Fore.YELLOW +"You: ")
    prefrence = normalize_input(prefrence)

    if prefrence in destinations:
        suggestion = random.choice(destinations[prefrence])
        print(Fore.CYAN + f"TravelBot: I recommend visiting {suggestion}!")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()


        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Lets try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()

    else:
        print(Fore.RED + "TravelBot: Sorry, I didnt get that. Please choose beaches, mountains or cities.")

    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: how many days?")
    days = input(Fore.YELLOW + "You: ")


    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Comfortable clothes")
    print(Fore.GREEN + "- Toiletries")
    print(Fore.GREEN + "- Travel documents")
    print(Fore.GREEN + "- Snacks")
    print(Fore.GREEN + "- Entertainment (books, music)")


def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end the chat.\n")


def chat():
    print(Fore.CYAN + "Hello i am travelbot")
    name = input(Fore.YELLOW + "Your name?")
    print(Fore.GREEN + f"Nice to meet you {name}!")
    show_help()

    while True:
        user = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user)

        if "reccomendation" in user_input or "suggest" in user_input:
            recommend()
        elif "packing" in user_input or "pack" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif user_input in ["exit", "bye", "quit"]:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break


if __name__ == "__main__":
    chat()
