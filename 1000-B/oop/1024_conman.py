from contact import Contact  # IMPORT CONTACT CLASS

def add_contact(cons):
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    yob = input("Year of birth: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    con = Contact(fname, lname, yob)
    con.set_emailaddress(email)
    con.set_phonenumber(phone)
    cons[email] = con

def show_contacts(cons):
    for email in cons:
        con = cons[email]
        fname = con.get_firstname()
        lname = con.get_lastname()
        email = con.get_emailaddress()
        print(f"{fname:20s}{lname:20s}{email:30s}")

def load_contacts(cons):
    cons.clear()
    with open('contacts.txt','r') as fi:
        for line in fi:
            line = line.strip()
            parts = line.split('\t')
            con = Contact(parts[0], parts[1], parts[2])
            con.set_emailaddress(parts[3])
            con.set_phonenumber(parts[4])
            cons[parts[3]] = con

def save_contacts(cons):
    fi = open('contacts.txt','w')
    for email in cons:
        con = cons[email]
        fname = con.get_firstname()
        lname = con.get_lastname()
        yob = con.get_birthyear()
        email = con.get_emailaddress()
        phone = con.get_phonenumber()
        line = f"{fname}\t{lname}\t{yob}\t{email}\t{phone}\n"
        fi.write(line)
    fi.close()

def delete_contact(cons):
    email = input("Delete which email: ")
    if email in cons:
        del cons[email]
        #cons.pop(email)
    else:
        print('Email doesn\'t exist')


def edit_contact(cons):
    key = input("Edit which email: ")
    if key in cons:
        con = cons[email]
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        yob = input("Year of birth: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        con.set_firstname(fname)
        con.set_lastname(lname)
        con.set_birthyear(yob)
        con.set_emailaddress(email)
        con.set_phonenumber(phone)
        if key != email:
            del cons[key]
            cons[email] = con
    else:
        print('Email doesn\'t exist')

all_contacts = {}

while (True):
    print()
    print('+' * 60)
    print('ConMan - Contact Manager'.center(60))
    print('+' * 60)
    print('1) Load Contacts')
    print('2) Save Contacts')
    print('3) Show Contacts')
    print('4) Add Contact')
    print('5) Edit Contact')
    print('6) Delete Contact')
    print('X) Exit')

    choice = input('Enter Choice: ')

    if choice == '1':
        load_contacts(all_contacts)
    elif choice == '2':
        save_contacts(all_contacts)
    elif choice == '3':
        show_contacts(all_contacts)
    elif choice == '4':
        add_contact(all_contacts)
    elif choice == '5':
        edit_contact(all_contacts)
    elif choice == '6':
        delete_contact(all_contacts)
    elif choice.upper() == 'X':
        break
    else:
        print('INVALID CHOICE!!')
    input('Press ENTER to contine')

print('SEE YA!!!')
