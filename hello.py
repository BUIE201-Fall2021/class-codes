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
        self._Viewers = []
    
    def print(self):
        print("Movie " + self._Name + " was released on")
        self._ReleaseDate.print()

    def add_viewer(self, viewer):
        self._Viewers.append(viewer)
class Viewer:
    def __init__(self, name) -> None:
        self._Name = name

matrix = Movie("The Matrix Resurrections", 2021, 12, 15)
matrix.print()

caner = Viewer("Caner")
tamer = Viewer("Tamer")

dune = Movie("The Dune", 2021, 9, 15)
dune.print()

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

matrix.add_viewer(caner)

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

dune.add_viewer(tamer)

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

dune.add_viewer(caner)

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

i = 5