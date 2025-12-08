import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.chars2d)
ans1 = 0
ans2 = 0

sy = 0
sx = data[0].index("S")

q = deque([(sx, sy, -1, -1)])
num_ways = {(-1, -1): 1}

while q:
    x, y, px, py = q.popleft()

    if (x, y) in num_ways:
        num_ways[(x, y)] += num_ways[(px, py)]
        continue
    if y + 1 >= len(data):
        ans2 += num_ways[(px, py)]
        continue
    num_ways[(x, y)] = num_ways[(px, py)]

    if data[y + 1][x] == "^":
        ans1 += 1
        if x - 1 >= 0:
            q.append((x - 1, y + 1, x, y))
        if x + 1 < len(data[0]):
            q.append((x + 1, y + 1, x, y))
    else:
        q.append((x, y + 1, x, y))

print(ans1, ans2)
