print("Enter Marks in all subjects")

english = int(input("English :"))
maths = int(input("math"))
science = int(input("science"))
SST = int(input("SST"))

sum = english+maths+science+SST
print("The sum of all subject is", sum)

perc = (sum/400)*100

print("The percentage of all of the subjects are", perc)