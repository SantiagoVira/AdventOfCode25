import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.chars2d)
ans1 = 0
ans2 = 0

h, w = len(data), len(data[0])

for y in range(h):
    for x in range(w):
        if data[y][x] == "@":
            count = [data[sy][sx]
                     for (sx, sy) in omni_moves_indicies(w, h, x, y)].count("@")

            if count < 4:
                ans1 += 1

while True:
    changed = False
    for y in range(h):
        for x in range(w):
            if data[y][x] == "@":
                count = [data[sy][sx]
                         for (sx, sy) in omni_moves_indicies(w, h, x, y)].count("@")

                if count < 4:
                    changed = True
                    data[y][x] = "."
                    ans2 += 1

    if not changed:
        break


print(ans1, ans2)
