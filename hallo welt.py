print("")
print("Hallo World")

x = 42
y = True

if x < 52: 
    print("if x: Hello World")
    x = 52
    
if y: 
    print("if y: Hello World")
    y = False
else:
    print("else: exception")
    
if y: 
    print("if y: Hello World")
    y = False
    x = 42
elif x == 42:
    print("elif: Antwort 42")
else:
    print("else: exception")

print("")

