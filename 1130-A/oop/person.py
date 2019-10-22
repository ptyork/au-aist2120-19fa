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
