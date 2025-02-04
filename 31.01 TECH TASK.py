'''1.Zampa is required to handle his book stall with certain information. He is trying to formulate his
information and also automize the discount process. To do this he has to get the following information
from the customer. [Use class and methods]
INPUT:
Enter your Book Name:
Enter your Customer ID:
OUTPUT:
Price of the Book is <<XYX>> MRP
You are eligible for Discounted of <<X>>%
Your discounted Price for the Book is <<XXX>> MRP
Do you want to continue?
Note: This Output is the basic output. But will vary based on the need.
CONDITION:
1. Do the basic validation of the input before accepting it from the user
2. Based on the discount and the price calculate the discounted price to display to the user.
3. Based on the Customer ID Discount is created.
a. 1-100 – 50% discount
b. 101-300 – 30% discount
c. 301-400 – 20% discount
d. 401-500 – 10% discount
e. >500 – No Discount
4. Customer should not enter the details in the output screen'''


class Customer:
    
    def __init__(self,bookname,cus_id):
        self.bookname=bookname
        self.cus_id=cus_id
        
        
    def validate(self):
        if not isinstance(cus_id,int):
            raise ValueError("Customer id should be positive")
        else:
            print("Valid customer id")
    
    def discount(self,book,dis):
        
        if self.cus_id>=1 and self.cus_id<=100:
            if self.bookname in book:
                price=(50/100)*book.get(bookname)
                total=book.get(bookname)-price
                d=True
                dis+=50
                print("You are eligible for discount",dis,"%")
                print("Your discounted amount is:",total,"MRP")
              
            else:
                print("No book")
       
        elif self.cus_id>100 and self.cus_id<=300:
            
            if self.bookname in book:
                 price=(30/100)*book.get(bookname)
                 total=book.get(bookname)-price
                 d=True
                 dis+=30
                 print("You are eligible for discount",dis,"%")
                 print("Your discounted amount is:",total,"MRP")
                 
            else:
                print("No book")
        elif self.cus_id>300 and self.cus_id<=400:
           
            if self.bookname in book:
            
                 price=(20/100)*book.get(bookname)
                 total=book.get(bookname)-price
                 d=True
                 dis+=20
                 print("You are eligible for discount",dis,"%")
                 print("Your discounted amount is:",total,"MRP")
                 
            else:
                print("No book")
        elif self.cus_id>400 and self.cus_id <=500:
            
            if self.bookname in book:
                 price=(10/100)*book.get(bookname)
                 total=book.get(bookname)-price
                 d=True
                 dis+=10
                 print("You are eligible for discount",dis,"%")
                 print("Your discounted amount is:",total,"MRP")
                 
            else:
                print("No book")

        else:
             total=book.get(bookname)
             d=False
             dis+=0
             print("You are not eligible for discount",dis)
             print("Your amount is:",total,"MRP")
   
try:
    bookname=input("Enter the book name:")
    cus_id=int(input("Enter the customer id"))
    book={"Ponniyin selvan":1000 ,"Silapathigaram":1500 ,"HarryPotter":1000}
   
    dis=0
    c=Customer(bookname,cus_id)
    c.validate()
    
    c.discount(book,dis)
    
except ValueError as e:
    print(e)
