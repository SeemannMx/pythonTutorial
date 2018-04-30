# exceptions
def pre():
    print("")
    print("Exceptions in Python")
    print("--------------------------------------------------------")
pre()

# create the exception class
class Ex(Exception):
    pass
    
def testException():    
    # try / raise / except
    try:
                
        a = 10
        b = 20
        while b == 20:
            if a == 10: 
                a = 0
        
            else: 
                raise Ex()
                b = 21
                
    except Ex:
        print("exception raised")
        print("")
    
    else: 
        print("no exception raised")
        

testException()

        
        
    