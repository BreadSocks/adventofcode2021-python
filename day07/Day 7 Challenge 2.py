from functools import reduce

file = "input.txt"

crabs = [int(x) for x in open(file).read().split(",")]
lowest = min(crabs)
highest = max(crabs)
total = float('inf')
chosen_position = 0

for option in range(lowest, highest + 1):
    this_total = sum([abs(x - option) + sum(range(abs(x - option))) for x in crabs])
    if this_total < total:
        total = this_total
        chosen_position = option
print(total)
