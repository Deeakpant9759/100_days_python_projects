class Number_Check():
    def __init__(self,number):
        self.number = number
    def valid_input(self):
        try:
            if not isinstance(self.number, (int, float)):
                raise TypeError
        except TypeError:
            print("Enter a number only")
    def even_check(self):
        if self.number%2==0:
            return print("Number is Even")
    def odd_Check(self):
        if self.number%2!=0:
            return print("Number is odd")
    def Prime_Checkk(self):
        if self.number <=2:
            return print("Number is Not Prime")
        for i in range(2,self.number-1):
            if self.number%i==0:
                return print("Number is Not Prime")
        return print("Number is not prime")
            

        
        
    