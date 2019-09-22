subtotal = 0 # accumulator
subprod = 1

while True:
    print('current sum is', subtotal)
    print('current prod is', subprod)
    num = int(input("enter num: "))
    if num == 0:
        break
    else:
        subtotal += num
        subprod *= num

print('final sum is', subtotal)
print('final prod is', subprod)

