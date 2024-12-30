class Calculator:
    def __init__(self,operator1,operator2):
        self.operator1=operator1
        self.operator2=operator2
    def options(self):
             if not isinstance(operator1,int) or not isinstance(operator2,int):
                 raise ValueError("operator data type is wrong,retry again")
             else:
                 
                    
                    if choice>4:
                        raise KeyError("the options are not valid")
                    else:
                        match choice:
                            case 1:
                                
                                result=self.operator1+self.operator2
                                return result
                            case 2:
                                result=self.operator1-self.operator2
                                return result
                            case 3:
                                result=self.operator1*self.operator2
                                return result
                            case 4:
                                if  self.operator2==0:
                                    raise ZeroDivisionError ("The operator should not be zero")
                                else:
                                    result=self.operator1/self.operator2
                                    return result
                
                  

try:
    
    while True:
            print("1)addition 2)subtraction 3)multiplication 4)division")
            choice=int(input("Enter the choice"))
            operator1=int(input("Enter the first number"))
            operator2=int(input("Enter the second number"))
            c=Calculator(operator1,operator2)
            result=c.options()
            print(result)
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
                    
                    
                    
                    
