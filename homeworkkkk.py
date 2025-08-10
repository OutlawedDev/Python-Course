class BMW:
    def __init__(self,model):
        self.model = model
    def start(self):
        print(f"{self.model} is starting smoothly")
    def speed(self):
        print(f"{self.model} can go up to 250 km/h")


class ferrari:
    def __init__(self,model):
        self.model = model
    def start(self):
        print(f"{self.model} starts with a roar")
    def speed(self):
        print(f"{self.model} can go up to 340 km/h")
    

obj_bmw = BMW("X5")
obj_ferrari = ferrari("488 spider")

for car in (obj_bmw, obj_ferrari):
    car.start()
    car.speed()
    print()