smallest_num = 2
my_range = [11, 13, 14, 16, 17, 18, 19, 20]


def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in my_range):
            return num
    return None


solution = find_solution(20)
if solution is None:
    print("No answer found")
else:
    print("found an answer:", solution)
