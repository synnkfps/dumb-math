P = [2, 3, 5, 7]
primes = []

# yet another prime numbers algorithm
for i in range(7, 500000):
    number_count = 0
    for j in P:
        number_count += bool(i%j)
    else:
        if number_count == 4:
            primes.append(i)
else:
    P += primes

# for i,j  in zip(range(4000), primes):
#   if j < 4000: print(j)
    
def factorize(number):
    n = number
    for i in P:
        if n == 1: break
        while n % i == 0:
            print(f'{int(n)}'.rjust(20),'|', i)
            n/=i
        
factorize(123124413)
