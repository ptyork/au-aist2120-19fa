from person import Person

def show_person(p):
    print(p.FirstName, p.LastName, p.BirthYear)

# CREATE INSTANCE FROM CLASS
p1 = Person()
p1.FirstName = 'Paul'
p1.LastName = 'York'
p1.BirthYear = 1972

p2 = Person()
p2.FirstName = 'Mike'
p2.LastName = 'Dowell'
p2.BirthYear = 1907

# print(p1)
# show_person(p1)
p1.show()
p2.show()
