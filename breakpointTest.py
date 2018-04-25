# loop directly
for i in range(0,10):
    if i % 2 == 0:
        print(i+100)
        break
    else:
        print(i)

# break to leave loop directly continue / break like return and break
for i in range(0,10):
    if i % 2 == 0:
        print(i+100)
        continue
    else:
        print(i)
