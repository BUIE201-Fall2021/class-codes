# Definition of the class
class Date:
    # initalizer / constructor
    def __init__(self, Year, Month, Day):
        self._Year = 1970
        self._Month = 1
        self._Day = 1
        self.set_date(Year, Month, Day)
    
    def set_date(self, Year, Month, Day):
        if Year > 0 and Month > 0 and Month <= 12 and Day > 0 and Day <= 31:
            self._Year = Year
            self._Month = Month
            self._Day = Day
        else:
            print("Invalid date!")
    
    def print(self):
        print("The date is: {}/{}/{}".format(self._Day, self._Month, self._Year))

today = Date(2021, 10, 26)
today.print()
print(type(today))
print(id(today))

today2 = today
print(type(today2))
print(id(today2))

today2.set_date(1980, 1, 1)

today.print()


# Everything  is an object in Python
i = 5
print(type(i))
print(id(i))

j = i
print(type(j))
print(id(j))

# Copy-on-assignment creates a new int object for i
# so that the value of j is not modified 
# int -> immutable
# https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a
i += 5

print(type(i))
print(id(i))
print(i)

print(type(j))
print(id(j))
print(j)

f = 4.5
g = 3.0

print("f: " + str(f.is_integer()))
print("g: " + str(g.is_integer()))

s = "IE 201"
print(s.lower())

s_lower = s.lower()

print (type(s))
print (id(s))
print (s)

print (type(s_lower))
print (id(s_lower))
print (s_lower)

weather_temp = 16
fmt = "Hello, today the weather is {} degrees".format(weather_temp)
print(fmt)

student_ids = ["5435", "34535", "32424", "65435"]
concat = ",".join(student_ids)
print(concat)

