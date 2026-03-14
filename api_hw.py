import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    

    if response.status_code == 200:
        print("Full json response: ")

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to retrieve joke."

def get_random_trivia():
    url = "https://opentdb.com/api.php?amount=1"
    response = requests.get(url)

    if response.status_code == 200:
        print("Full json response: ")

        data = response.json()
        return f"Question: {data['results'][0]['question']} | Answer: {data['results'][0]['correct_answer']}"
    else:
        return "Failed to retrieve trivia."


    
def main():
    print("welcome to random joke generator!")

    while True:
        user_input = input("Press 'j' to get a random joke or type 'exit' to quit or type 't' for a trivia: ")
        if user_input in ("q", "exit"):
            print("goodbye")
            break

        if user_input == "j":
            joke = get_random_joke()
            print(joke)

        if user_input == "t":
            trivia = get_random_trivia()
            print(trivia)


    
    

if __name__ == "__main__":
    main()


