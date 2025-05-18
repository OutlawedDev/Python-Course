def calculate():
    print("=== Welcome to the VortexOS Bill Calculator ===")

    try:
        total_bill = float(input("Enter the total bill amount: "))
        amount_paid = float(input("Enter the amount paid: "))
        
        if amount_paid > total_bill:
            print("Customer has overpaid. No due amount")
            overpaid = amount_paid - total_bill
            print(f"Overpaid amount: ${overpaid:.2f}")

        else:
            due_amount = total_bill - amount_paid
            print(f"Customer's due amount: ${due_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculate()
