class InsufficeentFunds(Exception):
    """Custom Exception for insufficient balance"""
    pass

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw (self, amount):
        try:
            print(f"\nAttempting to withdraw ${amount} from {self.owner}'s account")

            if not isinstance(amount, (int, float)):
                    raise TypeError("Amount must be a number")
                
            if amount <= 0:
                    raise ValueError("Amount must be a positive number")
                
            if amount > self.balance:
                    raise InsufficeentFunds("Insufficient Balance in your account")
                
            self.balance -= amount
            print(f"Withdrawal Successful. New balance is ${self.balance}")

        except TypeError as te:
                print("Type Error:", te)

        except ValueError as ve:
                print("Value Error:", ve)
            
        except InsufficeentFunds as ie:
                print("Insufficient Funds:", ie)
            
        except Exception as e:
                print("An error occured: ", e)
            
        finally:
                print("Transaction Attempt Complete")


account = BankAccount("Amit", 5000)

account.withdraw(1500)
account.withdraw("two")
account.withdraw(-200)
account.withdraw(10000)