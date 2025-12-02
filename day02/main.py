import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input(
    "./input.txt", lambda s: [(int(x[:x.index("-")]), int(x[x.index("-") + 1:])) for x in s.split(",")])
ans1 = 0
ans2 = 0

for rng in data:
    s, e = rng

    for i in range(s, e + 1):
        st, le = str(i), len(str(i))
        if st[:le // 2] == st[le // 2:]:
            ans1 += i

        for j in range(1, le // 2 + 1):
            if le % j == 0 and st[:j] * (le // j) == st:
                ans2 += i
                break


print(ans1, ans2)
