class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'(' +self.meaning+')'
    
flash = []
print("welcome to flashcard app")

while(True):
    word = input("enter the word you want to add to the flashcard: ")
    meaning = input("enter the meaning of the word: ")


    flash.append(flashcard(word, meaning))
    option = int(input("press 0 to add another flashcard or press 1 to exit: "))
    if(option):
        break


print("\n your flashcards")
for i in flash:
    print(">", i)