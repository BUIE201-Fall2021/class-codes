import sys

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

class Movie:
    def __init__(self, name, release_year, release_month, release_day) -> None:
        self._Name = name
        self._ReleaseDate = Date(release_year, release_month, release_day)
    
    def print(self):
        print("Movie " + self._Name + " was released on")
        self._ReleaseDate.print()

# print("temp refcount: " + str(sys.getrefcount([])))

m = Movie("The Matrix Resurrections", 2021, 12, 15)
m.print()

print("m: " + str(id(m)))
print("m refcount: " + str(sys.getrefcount(m)))

matrix = m

print("matrix: " + str(id(matrix)))
print("m refcount: " + str(sys.getrefcount(m)))
print("matrix refcount: " + str(sys.getrefcount(matrix)))

matrix = None

print("matrix: " + str(id(matrix)))
print("m refcount: " + str(sys.getrefcount(m)))
print("matrix refcount: " + str(sys.getrefcount(matrix)))

m2 = Movie("The Dune", 2021, 9, 15)
m2.print()

i = 4
print("i refcount: " + str(sys.getrefcount(i)))
