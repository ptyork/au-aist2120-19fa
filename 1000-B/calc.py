running_total = 0 # accumulator
running_prod = 1

while True:
    print("The total so far is", running_total)
    print("The prod so far is", running_prod)
    num = int(input("enter a number: "))
    # num = input("enter a number: ")
    # num = int(num)
    if num == 0:
        break
    else:
        running_total = running_total + num
        running_prod = running_prod * num

print("The final total is", running_total)
print("The final prod is", running_prod)
