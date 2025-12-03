import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.ints2d)
ans1 = 0
ans2 = 0


def solve(bank, num_dig):
    digits = [i for i in range(num_dig)]
    for i in range(1, len(bank)):
        for j in range(num_dig):
            if bank[i] > bank[digits[j]] and i < len(bank) - (num_dig - 1 - j):
                for k in range(j, num_dig):
                    digits[k] = i + k - j
                break
            elif i == digits[j]:
                break

    jolts = 0
    for i in range(num_dig):
        jolts *= 10
        jolts += bank[digits[i]]

    return jolts


for bank in data:
    ans1 += solve(bank, 2)
    ans2 += solve(bank, 12)

print(ans1, ans2)
