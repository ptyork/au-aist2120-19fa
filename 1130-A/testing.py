'''
Boolean Expressions
Comparison Operators
<   LT
>   GT
<=  LTE
>=  GTE
==  Equality
!=  Not Equal

Truthy
Non empty strings
Non empty collections
Non-zero numbers
Opposite of this is Falsey

Boolean Modifiers
and
or
not
'''
#age = 21
age = int(input('age: '))
if age < 21:
    print('You are underage')
    print('haha!!')
elif age == 21:
    print('Just made it')
else:
    print('Go on in.')


# inCollege = True
# yn = input('in college (y/n): ')
yn = input('in college (y/n): ').lower()
inCollege = True
if yn != 'y':
    inCollege = False

if age >= 21:
    if inCollege == True:
        print("come in!!!")
    else:
        print('NO DOGS ALLOWED!!')
else:
    print('NO DOGS ALLOWED!!')

if age >= 21 and inCollege == True:
    print("come in!!!")
else:
    print('NO DOGS ALLOWED!!')

if age >= 21 or inCollege == True:
    print("come in!!!")
else:
    print('NO DOGS ALLOWED!!')

if not (age >= 21 or inCollege == True):
    print("come in!!!")
else:
    print('NO DOGS ALLOWED!!')


# inCollge == True is the SAME as JUST inCollege
if age >= 21 and inCollege:  
    print("come in!!!")
else:
    print('NO DOGS ALLOWED!!')





