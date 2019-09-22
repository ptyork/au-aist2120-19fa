for n in range(1,500):
    if n % 2 == 0:
        print(n, 'is not prime--is divisible by 2')
        continue

    max_num = n//2
    is_prime = True
    for t in range(3,max_num):
        if n % t == 0:
            print(n, 'is not prime--is divisible by', t)
            is_prime = False
            break
    if is_prime:
        print(n, "is prime")
