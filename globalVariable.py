# define global variables with key word global, only within nested functions
def setVariable():
    def cout():
        global text 
        text = "Iam a global variable"
    # exectute fuction to make variable text accessable
    cout()    
    print(text)

# call function
setVariable()
