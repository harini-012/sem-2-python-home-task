#1) CREATE A BANK ACCOUNT CLASS THAT HANDLES COMMON OPERATIONS LIKE DEPOSITING WITHDRAWING MONEY , AND CHECKING THE BALANCE
class Bank:
    def __init__(self,holder_name,acc_num,initial_bal=0):
        self.holder_name=holder_name
        self.acc_num=acc_num
        self.balance=initial_bal
    def deposit(self,amount):
        if amount>0:
            print(f"you have deposited {amount} successfully")
            self.balance+=amount
        else:
            print("your deposit is invalid")
    def withdraw(self,amount):
        if amount<self.balance:
            print(f"you have with drawn {amount} successfully")
            self.balance-=amount
        else:
            print("you do not have sufficient fund")
    def check_balance(self):
        print(f"your available balance is {self.balance}")
user=Bank("Harini",9841031623,8000)
user.deposit(9000)
user.withdraw(1000)
user.check_balance()
print("*************************")
user=Bank("Ranjani",9841081623,10000)
user.deposit(1000)
user.withdraw(12000)
user.check_balance()

#2) SCENARIO: COSMETICS PRODUCT INFORMATION (DEFAULT CONSRUCTOR)
class Cosmetics:
    def __init__(self,prod_name="lipstick",price=280,brand="lakme",category="makeup"):
        self.prod_name=prod_name
        self.price=price
        self.brand=brand
        self.category=category
    def display(self):
        print(f"The product name is {self.prod_name}")
        print(f"The price is {self.price}")
        print(f"The brand is {self.brand}")
        print(f"The category is {self.category}")
user=Cosmetics()
user.display()
