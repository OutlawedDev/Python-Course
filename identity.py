x = 5

if (type(x) is int):
    print("true")
else:
    print("false")

x = 5.0

if (type(x) is not float):
    print("true")
else:
    print("false")

a = 20
b = 20

if (a is b):
    print("a and b have the same identity")

o = 30

if (a is not o):
    print("a and o have DIFFERENT identity")