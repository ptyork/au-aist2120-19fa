class Person:
    # define attributes
    FirstName = ''
    LastName = ''
    YearOfBirth = 1900

    def __init__(self,first,last,year):
        self.FirstName = first
        self.LastName = last
        self.YearOfBirth = year

    def show(self):
        print(self.FirstName, self.LastName, self.YearOfBirth)

    def get_age(self,curryear):
        return curryear - self.YearOfBirth

    def get_firstname(self):
        return self.FirstName

    def set_firstname(self, newval):
        self.FirstName = newval

    def get_lastname(self):
        return self.LastName

    def set_lastname(self, newval):
        self.LastName = newval

    def get_yearofbirth(self):
        return self.YearOfBirth

    def set_yearofbirth(self, newval):
        self.YearOfBirth = newval
