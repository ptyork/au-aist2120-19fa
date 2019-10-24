from contact import Contact

def load_contacts(condict):
    with open('contacts.txt','r') as fi:
        for line in fi:
            line = line.strip()
            data = line.split('\t')
            con = Contact(data[0], data[1], data[2])
            con.set_phonenumber(data[3])
            con.set_emailaddress(data[4])
            condict[data[4]] = con

def save_contacts(condict):
    fi = open('contacts.txt','w')
    for key in condict:
        con = condict[key]
        fname = con.get_firstname()
        lname = con.get_lastname()
        yob = con.get_yearofbirth()
        phone = con.get_phonenumber()
        email = con.get_emailaddress()
        line = f"{fname}\t{lname}\t{yob}\t{phone}\t{email}\n"
        fi.write(line)
    fi.close()

def add_contact(condict):
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    yob = input("Year of birth: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    con = Contact(fname, lname, int(yob))
    con.set_emailaddress(email)
    con.set_phonenumber(phone)
    condict[email] = con

def show_contacts(condict):
    #for con in condict.value():
    for key in condict:
        con = condict[key]
        fname = con.get_firstname()
        lname = con.get_lastname()
        email = con.get_emailaddress()
        print(f"{fname:20s}{lname:20s}{email:20s}")

def edit_contact(condict):
    email = input("Edit who: ")
    if email in condict:
        con = condict[email]
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        yob = input("Year of birth: ")
        newemail = input("Enter email: ")
        phone = input("Enter phone: ")
        con.set_firstname(fname)
        con.set_lastname(lname)
        con.set_yearofbirth(int(yob))
        con.set_emailaddress(newemail)
        con.set_phonenumber(phone)
    else:
        print("NOPE!!")

def del_contact(condict):
    email = input("Delete who: ")
    if email in condict:
        del condict[email]
        #condict.pop(email)
    else:
        print("NOPE!!")

all_contacts = {}

while (True):
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
        del_contact(all_contacts)
    #elif choice in 'Xx':
    #elif choice == 'X' or choice == 'x':
    elif choice.upper() == 'X':
        break
    else:
        print('INVALID CHOICE!!')

print('SEE YA!!!')
