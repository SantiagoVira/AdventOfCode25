import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
ranges, ids = parse_input("./input.txt", Parse.two_lines)
ranges, ids = list(map(lambda l: tuple(map(int, l.split("-"))),
                   Parse.lines(ranges))), list(map(int, Parse.lines(ids)))
ans1 = 0
ans2 = 0

ranges.sort()

fresh_ranges = []

for id in ids:
    for s, e in ranges:
        if id >= s and id <= e:
            ans1 += 1
            break

for s, e in ranges:
    for i, (frs, fre) in enumerate(fresh_ranges):
        if e < frs:
            continue
        if s >= frs and s <= fre or e >= frs and e <= fre:
            fresh_ranges.pop(i)
            ans2 -= (fre - frs + 1)
            news, newe = min(s, frs), max(e, fre)
            fresh_ranges.insert(i, (news, newe))
            ans2 += newe - news + 1
            break
    else:
        fresh_ranges.append((s, e))
        ans2 += e - s + 1
        fresh_ranges.sort()

print(ans1, ans2)
