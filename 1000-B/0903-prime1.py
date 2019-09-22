n = 23
if n % 2 == 0:
    print('not prime--is divisible by 2')
    exit()

max_num = n//2
is_prime = True
for t in range(3,max_num):
    if n % t == 0:
        print('not prime--is divisible by', t)
        is_prime = False
        break
if is_prime:
    print("it's prime")
