import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = [[int(x) for x in line.split(",")]
        for line in parse_input("./input.txt", Parse.lines)]
ans1 = 0
ans2 = 0

dists = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        junc1, junc2 = data[i], data[j]
        dists.append((math.dist(junc1, junc2), i, j))

dists.sort()

groups = list(range(len(data)))
idx = 0


def get_group(idx):
    group, group_idx = groups[idx], idx
    while group != group_idx:
        groups[group_idx] = groups[group]
        group_idx = group
        group = groups[group_idx]

    return group


for min_val, a, b in dists:
    if idx == 1000:
        # Already done 1000, part 1 done
        group_sizes = Counter()
        for gi in range(len(groups)):
            group_sizes[get_group(gi)] += 1

        top_three = group_sizes.most_common(3)
        ans1 = top_three[-3][1] * top_three[-2][1] * top_three[-1][1]

    a_group = get_group(a)
    b_group = get_group(b)

    if a_group != b_group:
        ans2 = data[a][0] * data[b][0]
    groups[b_group] = a_group
    idx += 1

print(ans1, ans2)
