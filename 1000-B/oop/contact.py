from .person import Person
import re

class Contact(Person):
    __EmailAddress = 'poop@poop.org'
    __PhoneNumber = '555-1212'

    def get_emailaddress(self):
        return self.__EmailAddress

    def set_emailaddress(self, addr):
        rx = re.compile(r"\w+@\w+.\w+")
        if rx.match(addr):
            self.__EmailAddress = addr
        else:
            raise Exception("your're a punk")

    def get_phonenumber(self):
        return self.__PhoneNumber
    
    def set_phonenumber(self, newphone):
        self.__PhoneNumber = newphone


