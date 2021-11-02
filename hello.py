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
        print("Movie " + self._Name + " has " + str(len(self._Viewers)) + " viewers:")
        for viewer in self._Viewers:
            viewer.print()

    def add_viewer(self, viewer):
        self._Viewers.append(viewer)
        viewer.add_movie(self)
class Viewer:
    def __init__(self, name) -> None:
        self._Name = name
        self._Movies = []
    
    def add_movie(self, movie):
        self._Movies.append(movie)

    def print(self):
        print("Viewer Name: " + self._Name + " has viewed " + str(len(self._Movies)) + " movies")


matrix = Movie("The Matrix Resurrections", 2021, 12, 15)
matrix.print()

caner = Viewer("Caner")
tamer = Viewer("Tamer")

dune = Movie("The Dune", 2021, 9, 15)
dune.print()

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

matrix.add_viewer(caner)
matrix.print()

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

dune.add_viewer(tamer)
dune.print()

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

dune.add_viewer(caner)
dune.print()

print("caner's refcount: " + str(sys.getrefcount(caner)))
print("tamer's refcount: " + str(sys.getrefcount(tamer)))

caner.print()
tamer.print()

i = 5