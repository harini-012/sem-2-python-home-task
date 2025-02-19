'''.Create a payment system where different payment methods (CreditCard, PayPal, UPI) can be used interchangeably.
Each payment method should have a pay(amount) method that prints how the payment is processed.
Use polymorphism to process multiple payment methods dynamically.
Output:
Paid 500 using Credit Card. 
Paid 500 using PayPal. 
Paid 500 using UPI.'''

class CreditCard:
  def pay(self,amount):
      return f" Paid {amount} using Credit Card"
class PayPal:
  def pay(self,amount):
      return f" Paid {amount} using Paypal Card"

class Upi:
  def pay(self,amount):
      return f" Paid {amount} using Upi"
def process_payment(ccp,amount):
    print(ccp.pay(amount))
amount=int(input("Enter the amount"))
cc=CreditCard()
process_payment(cc,amount)
pp=PayPal()
process_payment(pp,amount)
dc=Upi()
process_payment(dc,amount)


'''Given a list of numbers, find the first duplicate element. If no duplicates exist, return -1.
Use a set to optimize performance.
Sample input:
[3, 1, 4, 2, 5, 3, 2]
Sample Output:
3'''


n=int(input("Enter the number of elements in the array"))
l=[]
new=[]
for i in range(n):
    e=int(input("Enter the element of the list"))
    l.append(e)
for i in l:
    if i not in new:
        new.append(i)
    else:
        print(i)
        break
if len(l)==len(new):
    print("-1")
    
    


      
