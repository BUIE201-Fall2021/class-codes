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
        # This is possible, but not good
        #self._ReleaseYear = release_year
        #self._ReleaseMonth = release_month
        #self._ReleaseDay = release_day
        self._ReleaseDate = Date(release_year, release_month, release_day)
    
    def print(self):
        # Violation of data encapsulation principle: _Year should not be accessed from outside of Date class
        # print("Movie " + self._Name + " was released on year " + str(self._ReleaseDate._Year))
        print("Movie " + self._Name + " was released on")
        self._ReleaseDate.print()

m = Movie("The Matrix Resurrections", 2021, 12, 15)
m.print()

m2 = Movie("The Dune", 2021, 9, 15)
m2.print()

i = 4