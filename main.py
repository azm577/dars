import os
import math
os.system("cls")

def is_prime(son):
    if isinstance(son,float):
        return son
    return 0
        
    

count = 0
a = [1, 3, 74.5, 5, 1.5]
primes = list(map(is_prime, a))
for i in primes:
    count += i
print(count)
