# Definition of the class
class Date:
    
    # initalizer / constructor
    def __init__(self):
        self._Year = 1970
        self._Month = 1
        self._Day = 1
    
    def set_date(self, Year, Month, Day):
        if Year > 0 and Month > 0 and Month <= 12 and Day > 0 and Day <= 31:
            self._Year = Year
            self._Month = Month
            self._Day = Day
        else:
            print("Invalid date!")

# instances/objects of Date class
today = Date()
# accessing/modifying class member fields from outside of the
# class violates data encapsulation/data hiding principle
# today.Year = 2021
# today.Month = -10
# today.Day = 21
today.set_date(2021, 10, 21)

# equivalent to:
# Date.set_date(today, 2021, 10, 21)

today.set_date(2021, -10, 21)


tomorrow = Date()
# tomorrow.Year = 2021
# tomorrow.Month = 10
# tomorrow.Day = 22
tomorrow.set_date(2021, 10, 22)

i = 3