import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.lines)
ans1 = 0
ans2 = 0

for line in data:
    sections = line.split(" ")

    goal = 0b0
    for c in sections[0][-2:0:-1]:
        # Light vals, either "." or "#"
        goal <<= 1
        goal |= c == "#"
    jolts_goal = [int(x) for x in sections[-1][1:-1].split(",")]

    buttons = []
    for sec in sections[1:-1]:
        # All of format "(x1,x2,...,xn)"
        nums = [int(x) for x in sec[1:-1].split(",")]
        b = 0b0
        for n in nums:
            b |= (1 << n)

        buttons.append(b)

    q = deque([(0b0, 0)])
    seen = set()
    while q:
        lights, moves = q.popleft()
        if lights in seen:
            continue
        if lights == goal:
            ans1 += moves
            break

        seen.add(lights)
        for b in buttons:
            q.append((lights ^ b, moves + 1))

    '''
    [0 0 1 2 0]

    b1 b2 b3 {a,b,c,d,e}
    a = (a in b1) * p1 + (a in b2) * p2 + (a in b3) * p3
    b = (b in b1) * p1 + (b in b2) * p2 + (b in b3) * p3
    c = (c in b1) * p1 + (c in b2) * p2 + (c in b3) * p3
    d = (d in b1) * p1 + (d in b2) * p2 + (d in b3) * p3
    e = (e in b1) * p1 + (e in b2) * p2 + (e in b3) * p3
    '''


print(ans1, ans2)
