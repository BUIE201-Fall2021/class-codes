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

def foo(theDate):
    print("Before modification")
    theDate.print()
    print(id(theDate))
    print("After modification")
    theDate.set_date(1981, 1, 1)
    theDate.print()

today = Date(2021, 10, 26)
today.print()
print(type(today))
print(id(today))

today2 = today
print(type(today2))
print(id(today2))

tomorrow = Date(2021, 10, 27)
tomorrow.print()
print(type(tomorrow))
print(id(tomorrow))

print("Before function call:")
tomorrow.print()
foo(tomorrow)
print("After function call:")
tomorrow.print()
