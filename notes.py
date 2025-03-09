amount = int(input("Enter the Amount to be withdraw :"))

note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("The 100 rupees note = to", note1)
print("The 50 rupees note = to", note2)
print("The 10 rupees note = to", note3)
