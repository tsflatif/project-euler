seed = 12
longest_seed = 0

sequence = []
longest_sequence = []


def odd_even(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return int((3 * num) + 1)


def do_sequence():
    while sequence[-1] != 1:
        sequence.append(odd_even(sequence[-1]))


while seed < 1000000:
    sequence.append(seed)
    do_sequence()

    if len(longest_sequence) < len(sequence):
        longest_sequence = sequence
        longest_seed = seed

    seed += 1
    sequence = []

# print(longest_sequence)
print(longest_seed)
