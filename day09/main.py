import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = [[int(x) for x in l.split(",")]
        for l in parse_input("./input.txt", Parse.lines)]
ans1 = 0
ans2 = 0

x_vals, y_vals = sorted([d[0] for d in data]), sorted([d[1] for d in data])
x_map = {x: i for i, x in enumerate(x_vals)}
y_map = {y: i for i, y in enumerate(y_vals)}
grid = [[False] * len(x_vals) for _ in range(len(y_vals))]

norms = [(x_map[x], y_map[y]) for x, y in data]

bottoms = [0] * len(grid[0])

for i in range(len(norms)):
    start, end = norms[i], norms[(i + 1) % len(norms)]
    minx, miny = min(start[0], end[0]), min(start[1], end[1])
    maxx, maxy = max(start[0], end[0]), max(start[1], end[1])
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            grid[y][x] = True
            bottoms[x] = max(bottoms[x], y)


cols = [False] * len(grid[0])
for y in range(1, len(grid) - 1):
    hashes, placing = False, False
    for x in range(len(grid[0])):
        if grid[y][x] and (not cols[x] or y == bottoms[x]):
            cols[x] = True
            hashes = False
            placing = False
            continue
        if not grid[y][x] and hashes:
            placing = not placing
        hashes = grid[y][x]
        if placing:
            grid[y][x] = True

max_cont_area = 0
for i in range(len(norms)):
    for j in range(i + 1, len(norms)):
        norm_i, norm_j = norms[i], norms[j]
        ix, iy = x_vals[norm_i[0]], y_vals[norm_i[1]]
        jx, jy = x_vals[norm_j[0]], y_vals[norm_j[1]]
        dx, dy = abs(ix - jx) + 1, abs(iy - jy) + 1

        area = dx * dy
        ans1 = max(ans1, area)
        if area > max_cont_area:
            minx, miny = min(norm_i[0], norm_j[0]), min(norm_i[1], norm_j[1])
            maxx, maxy = max(norm_i[0], norm_j[0]), max(norm_i[1], norm_j[1])
            valid = True
            for x in range(minx, maxx + 1):
                if not grid[miny][x] or not grid[maxy][x]:
                    break
            else:
                for y in range(miny + 1, maxy):
                    if not grid[y][minx] or not grid[y][maxx]:
                        break
                else:
                    # Valid for part 2
                    max_cont_area = area
                    ans2 = max(ans2, dx * dy)

print(ans1, ans2)
