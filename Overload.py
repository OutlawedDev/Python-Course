class a:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        
        else:
            return "ob2 is less than ob1"
    
    def __eq__(self, other):
        if(self.a == other.a):
            return "both are equal"
        else:
            return "both are not equal"
        
obj1 = a(2)
obj2 = a(3)
print("passed value: ", obj1.a, obj2.a)
print(obj1 < obj2)


obj3 = a(4)
obj4 = a(4)
print("passed values :", obj3.a, obj4.a)
print(obj3 == obj4)