from math import sqrt, floor


# for a in range(1000):
#     for b in range(1000):
#         for c in range(1000):
#             if a < b and b < c:
#                 if (c * c) == ((a * a) + (b * b)):
#                     if (a + b + c) == 1000:
#                         print(a, b, c)
#                         print((a*b*c))

for a in range(1000):
    for b in range(1000):
        c = sqrt(((a * a) + (b * b)))
        if a < b and b < c:
            if (a + b + c) == 1000:
                print(a, b, c)
                print((a * b * c))
