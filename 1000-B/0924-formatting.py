grades = [75, 92, 39, 55, 84, 97, 100, 0]

agrades = []

for grade in grades:
    if grade >= 90:
        agrades.append(grade)
        
print(agrades)

sgrades = '100 95 84 93 77 0'

newgrades = []

sgradeslist = sgrades.split(' ')
for sgr in sgradeslist:
    ngrade = int(sgr)
    if ngrade >= 90:
        newgrades.append(ngrade)

print(newgrades)


# LIST COMPREHENSIONS
#PSYCHE

print()
print()
print("Name", "Grad")
print("-----------")
print('Paul', 100)
print('George', 85)
print('Ringo', 23)


print()
print()
print("Name".ljust(20), "Grade".rjust(5))
print("-" * 26)
print('Paul'.ljust(20), str(100).rjust(5))
print('George'.ljust(20), str(85).rjust(5))
print('Ringo'.ljust(20), str(23).rjust(5))
print("TOTAL".center(26, '='))

tod = 'morning'
weather = 'cloudy'
temp = 91
humidity = 94.7

report = f"Good {tod}. Today it is {weather:15s} with a temp of {temp+5} and a relative humidity of {humidity:3.2f}%"
print(report)

