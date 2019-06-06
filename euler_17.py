from num2words import num2words

limit = range(1,1001)
words = ""

for i in limit:
    words = words + num2words(i).replace(' ', '').replace('-', '')

print(len(words))
# print(words)
# print(num2words(142).replace(' ', '').replace('-', ''))
