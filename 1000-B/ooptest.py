from oop.person import Person
from oop.contact import Contact

def show_person(p):
    print(p.FirstName, p.LastName, p.BirthYear)

# CREATE INSTANCE FROM CLASS
p1 = Person('Paul','York',1972)
p2 = Contact('Mike','Dowell',1907)

# print(p1)
# show_person(p1)
p1.show()
p2.show()

# p2.PhoneNumber = 'mike@dowell.com'

print(p2.get_emailaddress())
p2.set_emailaddress("mike.poops@pooper.edu")
print(p2.get_emailaddress())
#print(p1.PhoneNumber)
