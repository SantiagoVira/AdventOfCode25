import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.lines)
ops = data[-1].split()
nums1 = [[int(n) for n in l.split()] for l in data[:-1]]
nums2 = data[:-1]

ans1 = 0
ans2 = 0


def op(op_str):
    return (lambda a, b: a + b) if op_str == "+" else (lambda a, b: a * b)


def op_start(op_str):
    return 0 if op_str == "+" else 1


for i in range(len(nums1[0])):
    ans1 += reduce(op(ops[i]), [row[i] for row in nums1], op_start(ops[i]))

op_count = 0
r_nums = []
for x in range(len(nums2[0])):
    num = "".join([nums2[y][x] for y in range(len(nums2))]).strip()

    if num:
        r_nums.append(int(num))
        continue

    ans2 += reduce(op(ops[op_count]), r_nums, op_start(ops[op_count]))
    op_count += 1
    r_nums = []

ans2 += reduce(op(ops[op_count]), r_nums, op_start(ops[op_count]))

print(ans1, ans2)
