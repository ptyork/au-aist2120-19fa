s = 'John, Paul, George, Ringo'
beats = s.split(', ')

print(beats)

newstring = '...'.join(beats)
print(newstring)


s = "John, Paul, George and Ringo"
beats = s.split(', ')

print(beats)

firstbeats = beats[0:2]              # ['John', 'Paul']
lastbeats = beats[2].split(' and ')  # ['George', 'Ringo']
beats = firstbeats + lastbeats

print(beats)


s = "John, Paul, George, Ringo and Dead Paul"

beats = s.split(', ')
firstbeats = beats[0:-1]              # ['John', 'Paul']
lastbeats = beats[-1].split(' and ')  # ['George', 'Ringo']
beats = firstbeats + lastbeats

print(beats)

beats = s.split(', ')
beats = beats[-2::-1] + beats[-1].split(' and ')
print(beats)



grades = [77,35,93,88,97,73,92,100,0]
agrades = []
for grade in grades:
    if grade >= 90:
        agrades.append(grade)

print(grades)
print(agrades)

grades = [77,35,93,88,97,73,92,100,0]
badgrades = []
for grade in grades:
    if grade < 90:
        badgrades.append(grade+10)

print(grades)
print(badgrades)
print("I had " + str(len(agrades)) + " A's.")

# LIST COMPREHENSIONS
# Done interactively



# ljust(), rjust() and center()

print('name'.ljust(20), 'grade'.rjust(5))
print('=' * 26)
print('Paul'.ljust(20, '.'),str(100).rjust(5, '.'))
print('George'.ljust(20, '.'), str(92).rjust(5, '.'))
print('Ringo'.ljust(20, '.'), str(77).rjust(5, '.'))


temp = 92
humidity = 88.42
forecast = 'cloudy'
time = 'afternoon'

# STRING INTERPOLATION
# f-string

report = f"Good {time}, the current temp is {temp+5} with a relative humidity of {humidity:10.2f}%. It is {forecast}."
print(report)