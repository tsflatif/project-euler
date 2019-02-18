min_num = 100
max_num = 1000
largest_palindrome = 0
count = 0


def is_palindrome(num1, num2):
    product = num1*num2
    if str(product) == str(product)[::-1]:
        return True
    else:
        return False


for x in range(min_num, max_num):
    for y in range(min_num, max_num):
        if is_palindrome(x, y):
            count = count + 1
            if x * y > largest_palindrome:
                largest_palindrome = x * y


print(largest_palindrome)
print(count)
