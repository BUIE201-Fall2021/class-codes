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
 #       print("The date is: " + str(self._Day) + "/" + str(self._Month) + "/" + str(self._Year))

# instances/objects of Date class
today = Date(2021, 10, 21)
# accessing/modifying class member fields from outside of the
# class violates data encapsulation/data hiding principle
# today.Year = 2021
# today.Month = -10
# today.Day = 21
# today.set_date(2021, 10, 21)
today.print()

# equivalent to:
# Date.set_date(today, 2021, 10, 21)

# today.set_date(2021, -10, 21)


tomorrow = Date(2021, 10, 22)
# tomorrow.Year = 2021
# tomorrow.Month = 10
# tomorrow.Day = 22
# tomorrow.set_date(2021, 10, 22)

tomorrow.print()

i = 3