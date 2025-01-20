'''Create a BankAccount class with private attributes:
• __account_number
• __balance
Implement public methods to:
1. Set the account number and initialize the balance.
2. Deposit and withdraw money.
3. Implement a method add_interest(rate) to calculate and add interest to the balance.'''

class BankAccount:
    def __init__(self,account_no,balance):
        self.__account_no=account_no
        self.__balance=balance
    def check_account_no(self):
        
        print("Your account no is:",self.__account_no)
    def deposit(self):
        deposit=int(input("Enter your deposit amount:"))
        self.__balance+=deposit
        print("You deposited successfully")
    def withdraw(self):
        withdraw=int(input("Enter the withdraw amount:"))
        if self.__balance>withdraw:
            print("You have successfully withdrawn the amount")
            self.__balance-=withdraw
            print("you have withrawn successfully")
        else:
            print("You dont have sufficient balance")
    def check_balance(self):
        print(f"Your available balance is: {self.__balance}")
    def add_interest(self):
        interest=int(input("Enter the interest percentage"))
        interest_a=(interest/100)*balance
        self.__balance+=interest_a
account_no=int(input("Enter your account no:"))
balance=int(input("Enter your balanace"))
b=BankAccount(account_no,balance)
while True:
    print("1 checking account no 2.deposit 3.withdraw.4.balance 5.interest addition ")
    choice=int(input("Enter your choice:"))
    
    
    
    match choice :
        case 1:
            b.check_account_no()
        case 2:
            b.deposit()
        case 3:
            b.withdraw()
        case 4:
            b.check_balance()
        case 5:
            b.add_interest()

        
        
            
            

        
        
