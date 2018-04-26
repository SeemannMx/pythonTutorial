# while loop
x = 0
while x < 10:
    print("test while loop")
    print(x)
    x = x + 1
    
# for loop
print("")
print("List of programm languages")
print("--------------------------")
y = [ "C","\tC++","\t\tjava", "\t\t\tgo", "\t\t\t\tphyton", "\t\t\t\t\ttypescript"]

# languages is new variable which has not been created before
for language in y:
    print(language)
    
print("")
    
# range funtion
print("for / range ")
print("--------------------------")
for i in range(5):
    print(i)

print("")

# i > 5 & i < 10
for i in range(5,10):
    print(i)

print("")

# count up in steps
for i in range(0,10, 2):
    print(i)

print("")

# count down in steps
for i in range(10,5,-1):
    print(i)

print("")

# run through list
print("List of fruits")
print("--------------------------")

fruits = ["\t\tapple", "\t\torange", "lime", "kiwi", "\t\tstrawberry", "\t\tbanana"]
for j in range(len(fruits)):
    print(fruits[j])

print("")
    
def functionToTest():
    print("function from whileTest")
    