string = input("Enter your string to be reversed")

string2 = ('')

for i in string:
    string2 = i + string2

print("The original string", string)
print("The reversed string is", string2)