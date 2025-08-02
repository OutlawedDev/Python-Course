class vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def display(self):
        print(f"vehicle name: {self.name}")
        print(f"capacity name: {self.capacity}")

class bus(vehicle):
    def __init__(self, name, capacity, fare):
        super().__init__(name, capacity)
        self.fare = fare

    def calculate(self):
        print(f"Total fare for {self.capacity} passengers is: {self.fare * self.capacity}")
    

school_bus = bus("bus", 120, 50)
school_bus.display()
school_bus.calculate()