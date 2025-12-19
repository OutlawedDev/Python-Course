import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Guest"

conversation_history = []

print(f"\n{Fore.CYAN}Hello, {user_name}!")
print("Type a sentence and I will analyze the sentiment.")
print(
    f"Commands: {Fore.YELLOW}reset{Fore.CYAN}, "
    f"{Fore.YELLOW}history{Fore.CYAN}, "
    f"{Fore.YELLOW}stats{Fore.CYAN}, "
    f"{Fore.YELLOW}exit{Fore.CYAN}\n"
)

def sentiment_strength(polarity):
    if abs(polarity) < 0.3:
        return "weak"
    elif abs(polarity) < 0.6:
        return "moderate"
    else:
        return "strong"

while True:
    user_input = input(f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a valid sentence.{Style.RESET_ALL}")
        continue

    command = user_input.lower()

    if command == "exit":
        print(f"\n{Fore.BLUE}Exiting Sentiment Spy. Farewell, {user_name}!{Style.RESET_ALL}")
        break

    elif command == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}Conversation history has been reset.{Style.RESET_ALL}")
        continue

    elif command == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "positive":
                    color, emoji = Fore.GREEN, "😊"
                elif sentiment_type == "negative":
                    color, emoji = Fore.RED, "😞"
                else:
                    color, emoji = Fore.YELLOW, "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"(Polarity: {polarity:.2f}, {sentiment_type})"
                )
        continue

    elif command == "stats":
        if not conversation_history:
            print(f"{Fore.YELLOW}No data to show stats.{Style.RESET_ALL}")
        else:
            positives = sum(1 for _, _, s in conversation_history if s == "positive")
            negatives = sum(1 for _, _, s in conversation_history if s == "negative")
            neutrals = sum(1 for _, _, s in conversation_history if s == "neutral")

            print(f"{Fore.CYAN}Session Stats:{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Positive: {positives}")
            print(f"{Fore.RED}Negative: {negatives}")
            print(f"{Fore.YELLOW}Neutral: {neutrals}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "positive"
        color, emoji = Fore.GREEN, "😊"
    elif polarity < -0.25:
        sentiment_type = "negative"
        color, emoji = Fore.RED, "😞"
    else:
        sentiment_type = "neutral"
        color, emoji = Fore.YELLOW, "😐"

    strength = sentiment_strength(polarity)

    conversation_history.append((user_input, polarity, sentiment_type))

    print(
        f"{color}{emoji} {sentiment_type} sentiment detected "
        f"({strength}, polarity: {polarity:.2f})"
    )
