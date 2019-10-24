class Person:
    # state variables / attributes / "properties"
    FirstName = ''
    LastName = ''
    BirthYear = 1990

    def __init__(self, first, last, year):
        self.FirstName = first
        self.LastName = last
        self.BirthYear = int(year)

    def show(self):
        print(self.FirstName,self.LastName,self.BirthYear)
    
    def get_age(self):
        return 2019 - self.BirthYear

    def get_firstname(self):
        return self.FirstName
    
    def set_firstname(self, newname):
        self.FirstName = newname
    
    def get_lastname(self):
        return self.LastName

    def set_lastname(self, newname):
        self.LastName = newname
    
    def get_birthyear(self):
        return self.BirthYear

    def set_birthyear(self, newyear):
        self.BirthYear = int(newyear)
    
