medical = input("Did you have a medical cause Y or N: ")
attend = int(input("Enter the attendence of the student: "))

if medical == 'Y':
    print("You are allowed")
else:
    if attend>=75:
        print("allowed")
    else:
        print("Not allowed")