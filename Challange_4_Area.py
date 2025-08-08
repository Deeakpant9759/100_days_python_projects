class Area():
    def __init__(self,Base,Length,Height):
        self.Base = Base
        self.Length = Length
        self.Height = Height
    def is_Valid(self):
            if not all(isinstance(x,(int,float)) for x in [self.Base,self.Length,self.Height]):
                raise TypeError("Values Can't be an Float")
            if not (self.Base >= 0 and self.Length >=0 and self.Height >=0):
                raise ValueError ("Measurement Can't Negtive")
    def measuments(self):
         def meters(self):
              num
    
    def Tringle(self):

        