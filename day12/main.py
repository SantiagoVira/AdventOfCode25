import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.two_lines)

presents = [sec[sec.index("\n") + 1:].split("\n") for sec in data[:-1]]
presents = [[l.replace("#", "1").replace(".", "0")
             for l in p] for p in presents]

regions = Parse.lines(data[-1])
regions = [r.split(": ") for r in regions]
regions = [[tuple(map(int, size.split("x"))), list(
    map(int, counts.split(" ")))] for size, counts in regions]

ans1 = 0
ans2 = 0

num_cells = ["".join(p).count("1") for p in presents]

for (w, h), counts in regions:
    cells_used = sum(num_cells[i] * counts[i] for i in range(len(counts)))
    num_presents = sum(counts)
    if cells_used >= w * h:
        # Completely impossible
        ans2 += 1
        continue
    elif (w // 3) * (h // 3) >= num_presents:
        # Can fit by just lining up 3x3s
        ans2 += 1
        ans1 += 1

    # The hard part

assert ans2 == 1000
print(ans1, ans2)
print(len(regions))
