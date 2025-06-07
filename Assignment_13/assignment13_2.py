# Write a program which contains one class named as BankAccount. 
# BankAccount class contains two instance variables as Name & Amount. 
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user. 
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount. After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5 

    def __init__(self):
        print("enter your name: ")
        self.Name = input()
        print("enter initial amount: ")
        self.Amount = float(input())

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Balance: {self.Amount}")
    
    def Deposit(self):
        print("enter deposit amount: ")
        deposit_amount = float(input())
        self.Amount += deposit_amount
        print(f"Deposited: {deposit_amount}")
    
    def Withdraw(self):
        print("enter withdraw amount: ")
        withdraw_amount = float(input())
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print(f"Withdrawn: {withdraw_amount}")
        else:
            print("insufficient balance.")
    
    def CalculateIntrest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated at {BankAccount.ROI}%: {interest}")
        self.Amount += interest
        print(f"New Balance after interest: {self.Amount}")
              
account1 = BankAccount()
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateIntrest()
account1.Display()

print()

account2 = BankAccount()
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateIntrest()
account2.Display()
