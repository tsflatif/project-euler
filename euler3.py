number = 600851475143

def largest_prime_factor(x):
    current_divisor = 2
    while (x > current_divisor):
        if(x % current_divisor == 0):
            x = x /current_divisor
            current_divisor = 2
        else:
            current_divisor += 1

    return current_divisor


x = largest_prime_factor(number)

print(x)
