from collections import Counter

file = "input.txt"

horizontal = 0
depth = 0
lines = [list(line) for line in open(file).read().splitlines()]
switched = list(zip(*lines))
print(lines)
print(switched)
most_common = []
least_common = []
for line in switched:
    results = Counter(line).most_common(2)
    most_common += results[0][0]
    least_common += results[1][0]

gamma_rate = int(''.join(map(str, most_common)), 2)
epsilon_rate = int(''.join(map(str, least_common)), 2)

print(gamma_rate * epsilon_rate)
# for instruction in instructions:
#     command = instruction[0]
#     value = int(instruction[1])
#     if command == "forward":
#         horizontal += value
#     elif command == "up":
#         depth -= value
#     elif command == "down":
#         depth += value
#
# print("Distance: ", str(horizontal), "\nDepth: ", str(depth), "\nTotal: ", str(depth * horizontal))
