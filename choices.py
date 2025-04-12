print("Please Select Your Ride")
print("1.Bike")
print("2.Car")

choice = int(input("Enter Your Choice"))

if(choice == 1):
    print("What type of bike?")
    print("1.Scooty \n")
    print("2.Scooter \n")
    choice2 = int(input("Enter Your Choice"))
    if(choice2 == 1):
     print("You have selected scooty")
    else:
     print("You have selected scooter")
elif(choice == 2):
    print("What type of car?")
    print("1. Sedan")
    print("2.XUV")

    choice3 = int(input("enter your choice3 : "))
    if choice3 == 1:
       print("Your have selected sedan")
    else:
       print("You have selected XUV")

else:
   print("Wrong Choice")


  




