a = int(input("Enter a number (1): "))
b = int(input("Enter a number (2): "))
c = int(input("Enter a number (3): "))

temp = a
a = b
b = c 
c = temp

print(f"After swapping: a = {a}, b = {b}, c = {c}")