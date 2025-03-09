import math

num = float(input("Enter Your Number"))

if num < 0:
    print("The square root of a negative number is complex number")
else:
    s = math.sqrt(num)
    print("the square root of the number is = to", s)