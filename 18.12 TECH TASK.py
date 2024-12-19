class Calculator:
    def operation(self,a,b=None,c=None):
        result=0
        if not all(isinstance(x,(int,float)) for x in [a,b,c] if x is not None):
            raise ValueError("The given datatype is wrong")
        if a!=None and b==None and c==None:
            result=a*a
            return result
        elif a!=None and b!=None and c==None:
            result=a+b
            return result
        elif a!=None and b!=None and c!=None:
            result=a*b*c
            return result
c=Calculator()
try:
    ans=c.operation(2)
    print(ans)
    ans1=c.operation(2,4)
    print(ans1)
    ans2=c.operation(2,3,"three")
    print(ans2)
except ValueError as e:
    print(e)
        
