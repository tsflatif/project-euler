natural_numbers = range(1,101)

sum_of_squares = 0
square_of_sums = sum(natural_numbers) * sum(natural_numbers)

for i in natural_numbers:
    sum_of_squares = sum_of_squares + (i * i)

print(sum_of_squares)
print(square_of_sums)
print(square_of_sums - sum_of_squares)
