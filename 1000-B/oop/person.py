class Person:
    # state variables / attributes / "properties"
    FirstName = ''
    LastName = ''
    BirthYear = 1990

    def __init__(self, first, last, year):
        self.FirstName = first
        self.LastName = last
        self.BirthYear = year

    def show(self):
        print(self.FirstName,self.LastName,self.BirthYear)
    
    def get_age(self):
        return 2019 - self.BirthYear
    