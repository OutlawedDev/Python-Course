actual_cost = float(input("Please Enter The actual Cost"))

Selling_Cost = float(input("Enter the Selling Cost"))


if (Selling_Cost > actual_cost):
   amount = Selling_Cost - actual_cost
   print("Profit = {0}".format (amount))
else:
 print("You Have No profit")