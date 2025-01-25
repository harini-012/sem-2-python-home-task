'''Create a Python class HotelRoom to manage details of a hotel room. The class should have the
following:
Attributes:
A private attribute __room_number (an integer).
A private attribute __is_occupied (a boolean to indicate if the room is occupied).
A private attribute __rate_per_night (a float to store the rate for the room).
Methods:
A getter and setter for room_number with validation to ensure it is always a positive integer.
A getter and setter for rate_per_night with validation to ensure the rate is greater than zero.
A method check_in() to mark the room as occupied. Raise an exception if the room is already
occupied.
A method check_out() to mark the room as unoccupied. Raise an exception if the room is already
vacant.
A method display_details() to print the room details in the format:
Input:
# Create a room instance
room = HotelRoom()
# Set room details
room.set_room_number(101)
room.set_rate_per_night(200.50)
# Display details5
room.display_details()
Output:
Room Number: 101
Rate per Night: $200.50
    Occupied: No
'''

class Hotel:
                
                def __init__(self,room_no,rate_per):
                    self.__room_no=room_no
                    self.__is_occupied=False
                    self.__rate_per=rate_per
                    self.occupied_rooms=[100,101,102]
                    
                def get_room_no(self):
                    if self.__room_no>0:
                        return self.__room_no
                    else:
                        print("enter valid room no:")
                def get_rate_per_night(self):
                    if self.__rate_per>0:
                        return self.__rate_per
                    else:
                        print("valid cost")
                def set_room_no(self,room_no):
                    self.__room_no=room_no
                def set_cost(self,rate_per):
                    self.__rate_per=rate_per
                def check_in(self):
                    
                    if self.__room_no in self.occupied_rooms or self.__is_occupied:
                        raise ValueError("The room is occupied")
                    
                        
                    self.occupied_rooms.append(self.__room_no)
                    self.__is_occupied=True
                    print("The room is ready to check in")
                        
                def check_out(self):
                
                    if self.__room_no  not in self.occupied_rooms or  not self.__is_occupied:
                        raise ValueError("The room is vacant")
                    
                        
                    self.occupied_rooms.remove(self.__room_no)
                    self.__is_occupied=False
                    print("The room is ready to check out")
                        
                def display(self):
                    
                    print("Room no:",h.get_room_no())
                    print("Rate Per night:",h.get_rate_per_night())
                    


try:
    
    while True:
           choice=input("Enter the ci or co")
           room_no=int(input("Enter the room no:"))
           rate_per=float(input("enter the rate per night"))
           h=Hotel(room_no,rate_per)
           h.set_room_no(room_no)
           h.set_cost(rate_per)
           if choice=="ci":
               h.check_in()
               h.display()
           if choice=="co":
              
               h.check_out()
               h.display()
        
except ValueError as e:
        print(e)

