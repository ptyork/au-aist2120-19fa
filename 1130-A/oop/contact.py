from person import Person

class Contact(Person):
    __PhoneNumber = '555-1212'
    __EmailAddress = 'bob@the.builder'

    def get_emailaddress(self):
        return self.__EmailAddress
    
    def set_emailaddress(self,newaddr):
        isvalid = True
        if (newaddr.count('.') != 1): isvalid = False
        if (newaddr.count('@') != 1): isvalid = False
        if isvalid:
            self.__EmailAddress = newaddr
        else:
            raise Exception('INVALID EMAIL')
    

