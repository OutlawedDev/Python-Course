class bird:
    def __init__(self):
        print("bird is ready")

    def whoisthis(self):
        print("bird")

    def fly(self):
        print("fly faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
       
    def whoisthis(self):
        print("penguin")

    def run(self):
        print("run faster")

peggy = penguin()
peggy.whoisthis()
peggy.fly()
peggy.run()
