# create classes in python top down 
print("")
print("create class in python")
print("--------------------------")

class TestClass:
    number = 15
    symbol = "symbol as a string"
    
    # constructor with default value
    def __init__(self, x="constructor variable"):
        self.something = x
        print("Iam the constructor to TestClass\n ", self.something)
    
    # defined function always with self access variables with self keyword
    def functionInClass(self, otherNumber):
        result = otherNumber + self.number
        print("Result TestClass:  ",result)
        

        return result
        
some_instance = TestClass()
print("TestClass number:  ",some_instance.number)
print("TestClass sysmbol: ",some_instance.symbol)
some_instance.functionInClass(42)


    