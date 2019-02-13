def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


current_term = 0
largest_term = 0
i = 0
total = 0

while largest_term < 4000000:
    current_term = fibonacci(i)
    if current_term < 4000000:
        if current_term % 2 == 0:
            total = total + current_term
        largest_term = current_term
    else:
        break
    i = i + 1

print(largest_term)
print(total)
