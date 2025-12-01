import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.lines)

res1, res2 = 0, 0
dial = 50
for d in data:
    num = int(d[1:])
    sign = -1 if d[0] == "L" else 1

    for i in range(num):
        dial = (dial + sign) % 100
        res2 += dial == 0

    res1 += dial == 0

print(res1, res2)
