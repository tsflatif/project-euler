from math import sqrt, floor


prime_count = 0
largest_prime = 0
count = 0


def is_prime(n):
    if n == 1:
        return False  # 1 is not a prime Number
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        maxdivisor = floor(sqrt(n)) + 1
        for divisor in range(3, maxdivisor, 2):
            if n % divisor == 0:
                return False
        return True


while prime_count < 10001:
    if is_prime(count):
        largest_prime = count
        prime_count += 1

    count += 1

print(largest_prime)
