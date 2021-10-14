
# instr = input("Please enter a value")
# i = int(instr)

# if i == 5:
#     print("i is five")
# elif i == 10:
#     print("i is ten")
# else:
#     print("i is neighter")

# in C there is also switch statement
# match introduced to Python 3.10

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
#    sum = sum + w
    sum += w
#    w = w + 1
    w += 1

print (sum)

# operators
# +, -, *, /, %

i = 12 / 5
print(i)

j = 12 // 5
print(j)

k = 2 ** 5
print (k)

# =, ==, !=, <=, <, >=, >

# logical operators
# && -> C
# and 
# || -> C
# or 
# not 

if k > 30 and k < 50:
    print ("looks good")

# in  
l = [3, 5, 10, 34] 

if 5 in l:
    print("found!")
else:
    print ("not found")

d = {
    "IE 201": "Z. Caner Taskin", 
    "IE 203": "Necati Aras"
}

check = "IE 201"
if check in d:
    print ("I am taking " + check + " from " + d[check])
else:
    print ("I am not taking " + check + " this semester")

my_string = "domates"

if "d" in my_string:
    print ("I found it!")
