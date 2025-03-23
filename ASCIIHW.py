char = input("enter a character: ")
if len(char) != 1:
    print("please enter only a single character.")
else:
    print(f"The ASCII value of '{char}' is: {ord(char)}  ")