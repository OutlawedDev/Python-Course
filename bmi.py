height = float(input("enter ur height in cm: "))
weight = float(input("Enter ur weight in kg"))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are over weight")
elif BMI <= 34.9:
    print("You are severely over weight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severely obese")