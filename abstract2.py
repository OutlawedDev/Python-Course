from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass


class Human(animal):

    def move(self):
        print("I can walk and run")

class snake(animal):
    
    def move(self):
        print("I can crawl")

class Dog(animal):

    def move(self):
        print("I can bark")


class lion(animal):

    def move(self):
        print("I can roar")


r = Human()
r.move()


K = snake()
K.move()


R = Dog()
R.move()

K = lion()
K.move()

