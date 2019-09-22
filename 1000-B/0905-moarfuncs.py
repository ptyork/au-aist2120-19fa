print('Here!! #1')

'''
public void doStuff() {
    ..........
    return; // Optional / Implied
}
public string getName() {
    .........
    return "Paul";
}
public int add(int num1, int num2) {
    int sum = num1 + num2;
    return sum;
}

'''

def doStuff():
    print('I did stuff')
    return  # IMPLIED thus OPTIONAL

def getName():
    return "Paul"


print('Here!! #2')

#doStuff()

hisMajesty = getName()

print("hisMajesty=" + hisMajesty)

print('Here!! #3')

def add(num1, num2):
    summie = num1 + num2
    return summie
summie = add(1,2)
print(summie)
conc = add("hello", "world")
print(conc)
#goof = add("hello", 1)
#print(goof)

def div(num1, num2):
    # ACTIVE ERROR CHECKING
    if num2 == 0:
        print('Cannot divide by 0')
        return
    val = num1 / num2
    return val

def div2(num1, num2):
    # PASSIVE ERROR CHECKING / EXCEPTION HANDLING
    try:
        val = num1 / num2
        return val
    except:
        print('An error occurred')

xyz = div(5,3)
print(xyz)
xydarn = div(6,0)
print(xydarn)

zyx = div2(6,3)
print(zyx)
yzdarn = div2(6,0)
print(yzdarn)

def div3(num1, num2, num3):
    try:
        return (num1+num2)/num3
    except ZeroDivisionError:
        print('Don\'t cause black holes')
    except TypeError:
        print('I can\'t math with strings doofus')

print(div3(3,3,3))

try:
    val1 = div3(6,3,0)
    val2 = div3('6', 3, 0)
    print(val1, val2)
except:
    print('badness')

