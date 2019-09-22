'''
C#
public void DoStuff() {
    ...........
    return; // If you have this, I get to laugh at you
}

def DoStuff():
    return # Should be used only to do "EARLY" termination

public int Add(int num1, int num2) {
    val = num1 + num2;
    return val;
}
def Add(num1,num2):
    val = num1 + num2
    return val

'''
print("Here 1")

def DoStuff():
    print("My name is Paul")

print("Here 2")
DoStuff()
print("Here 3")

def GetName():
    return "Snuffaluffagous"

name = GetName()
print("The name is", name)

def Add(num1,num2):
    val = num1 + num2
    return val

def Div(num1,num2):
    # Proactive Error Checking
    # (input validation)
    if num2 == 0:
        print("sorry baby, can't divide by 0")
        return

    val = num1 / num2
    return val

def Div2(num1,num2):
    # Passive Error Handling
    # (exception handling)
    try:
        val = num1 / num2
        return val
    except:
        print('Awww. Sorry baby. Something bad happened')

# catch(Exception e)
def Div3(num1,num2):
    # Passive Error Handling
    # (exception handling)
    try:
        val = num1 / num2
        return val
    except TypeError:
        print('Awww. Sorry baby. I don\'t do strings')
    except ZeroDivisionError as zde:
        print("Awww. Sorry baby. I don't divide by zeroes", zde)

val = Add(3,6)
print(val)
val2 = Add("3", "6")
print(val2)
# val3 = Add(3, "6")
# print(val3)

print("No really, the name is", name)

val4 = Div(6,3)
print(val4)
val5 = Div(6,0)
print(val5)
val6 = Div2("6",3)
print(val6)
print(Div2(6,0))
print(Div3(6,0))
print(Div3("6",3))
