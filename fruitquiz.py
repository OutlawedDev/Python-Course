import random

class FruitQuiz:

    def __init__(self):

        self.fruits={'apple': 'red', 'orange': 'orange', 'banana': 'yellow', 'grape': 'purple', 'kiwi': 'brown'}

    def quiz(self):

        while (True):

            fruit, color = random.choice(list(self.fruits.items()))

            print("what is the color of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct!")
            else:
                print("wrong answer!")
                

            option = int(input("enter 0, if you want to continue or enter 1 to exit: "))
            if(option):
                    break


print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()