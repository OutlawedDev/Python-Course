a = input("Enter a string: ")

for i in a:
    if (i == 'A' or i == 'a'):
        print("A is present")
        break
    else:
        print("A or a is not present")