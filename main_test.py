import functions
print("")
print("define modules only with function and not with bare code")
print("--------------------------------------------------------")

def calculate():
    return 42


# defines a main function like in java, but python executes all code outside from this if
# clauses    
if __name__ == "__main__": 
    if calculate() == 42:
        functions.some_function_with_String("main test function callback")
        print("result is 42")
        
        print("")
        
        # call input from user and save input in variable text
        text = input("whats up?")
        
        print("echo: ", text)    
        print("")
        
        # type <class str>
        number = input("present year ist:")
        print(type(number))
        
        # cast type to integer, return <class int>
        print(type(int(number)))
        