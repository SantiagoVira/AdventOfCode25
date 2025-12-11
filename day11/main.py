import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.lines)
data = [l.split(": ") for l in data]
data = {k: vs.split(" ") for k, vs in data}
ans1 = 0
ans2 = 0


def dfs1(label):
    if label == "out":
        return 1

    return sum(dfs1(nxt) for nxt in data[label])


def dfs2(label, seen, calc):
    if label == "out":
        return int(seen == 0b11)
    elif label == "fft":
        seen |= 0b01
    elif label == "dac":
        seen |= 0b10

    if label in calc and calc[label][seen] > -1:
        return calc[label][seen]

    res = sum(dfs2(nxt, seen, calc) for nxt in data[label])
    calc[label][seen] = res
    return res


ans1 = dfs1("you")
calc = defaultdict(lambda: [-1, -1, -1, -1])
ans2 = dfs2("svr", 0b00, calc)

print(ans1, ans2)
