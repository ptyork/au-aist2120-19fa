'''
<   Less Than
>   Greater Than
<=  LTE
>=  GTE
==  Equal
!=  Not Equal
TRUTHY
''      Falsey
'abc'   Truthy
0       Falsey
not 0   Truthy
'''
age = int(input('what is your age: '))
if age < 21:
    print('You are too young to be drinking booze!')
elif age == 21:
    print('Barely!!')
else:
    print('drink up! Don\'t drive')

# gender = input('What is yhour gender: ').lower()
gender = input('What is yhour gender: ')
gender = gender.lower()

# if age >= 21:
#     if gender == 'F':
#         print("Come on in")
#     else:
#         print("Get out!!!")
# else:
#     print("Get out!!!")

if age >= 21 and gender == 'f':
    print('Come on in')
else:
    print('Get out!!!')

# if age >= 21 print('yo') OK, But NO

