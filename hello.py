
# instr = input("Please enter a value")
# i = int(instr)

# if i == 5:
#     print("i is five")
# elif i == 10:
#     print("i is ten")
# else:
#     print("i is neighter")

print("range(10)")
for i in range(10):
    if i == 5:
        continue
    elif i == 8:
        break
    else:
        print (i)

print("range(5, 15)")
for i in range(5, 15):
    print (i)

print("range(5, 15, 3)")
for i in range(5, 15, 3):
    print (i)

sum = 0
w = 15
while w <= 20:
    sum = sum + w
    w = w + 1

print (sum)
