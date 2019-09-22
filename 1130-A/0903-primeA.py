n = 2
max_factor = n//2

is_prime = True # ASSUME it is prime
for f in range(2, max_factor + 1):  # INCLUDE max_factor by adding 1
    if n % f == 0:
        print(n, "is not prime--it is divisible by", f)
        #exit()
        is_prime = False
        break

if is_prime:
    print(n, "is prime")
