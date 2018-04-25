# define functions
print("")
print("define functions in python")
print("--------------------------")
# function / def is skipped until function call
def some_function():
    for i in range(0,20):
        print("define a function")
        
print("")        
def some_funtion_with_param(param):
    for i in range(0 , param):
        print("define a function with param")

some_function()
some_funtion_with_param(10)

# recursive function
print("")
print("define recursive functions in python")
print("------------------------------------")

def fib(n):
    
    result = 0
    if n < 2:
        result = n
    else:
        result =  fib(n - 1) + fib(n - 2)
        
    return result

some_var = fib(10)
print(some_var)