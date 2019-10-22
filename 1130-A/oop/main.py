from person import Person
from contact import Contact

# def show_person(p):
#     print(p.FirstName, p.LastName, p.YearOfBirth)



p1 = Person('Paul','York',1972)
p2 = Person('Mike','Dowell',1968)
p3 = Contact('Harley','Eades',1990)

p1.show()
p2.show()
p3.show()
print(p1.get_age(2019))

# print(p1.EmailAddress)
# print(p2.EmailAddress)
print(p3.get_emailaddress())
#p3._Contact__EmailAddress = "867-5309"
p3.set_emailaddress('867-5310')
print(p3.get_emailaddress())

