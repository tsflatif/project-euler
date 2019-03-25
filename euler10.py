from math import sqrt, floor

prime_limit = 2000000
prime_sum = 0


def is_prime(n):
    if n == 1:
        return False  # 1 is not a prime Number
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        maxdivisor = int(floor(sqrt(n)) + 1)
        for divisor in range(3, maxdivisor, 2):
            if n % divisor == 0:
                return False
        return True


for i in range(prime_limit):
    if is_prime(i):
        prime_sum = prime_sum + i

print(prime_sum)
