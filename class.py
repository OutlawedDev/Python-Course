class employee:

    def __init__(self):
        print("employee created")
    
    def __del__(self):
        print("destructor called")


def create_obj():
    print("creating object")
    obj = employee()
    print("object created")
    return obj

print("calling create_onj() function")
obj = create_obj()
print("end")