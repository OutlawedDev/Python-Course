class Dog:

    species = "animal"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

blu = Dog("pug", 10)
woo = Dog("Bulldog", 15)

print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

print("{} is {} years old".format(blu.breed, blu.age))
print("{} is {} years old".format(woo.breed, woo.age))