file = "input.txt"

horizontal = 0
depth = 0
aim = 0
instructions = [line.split(" ") for line in open(file).read().splitlines()]
for instruction in instructions:
    command = instruction[0]
    value = int(instruction[1])
    if command == "forward":
        horizontal += value
        depth = depth + (aim * value)
    elif command == "up":
        aim -= value
    elif command == "down":
        aim += value

print("Distance: ", str(horizontal), "\nDepth: ", str(depth), "\nTotal: ", str(depth * horizontal))
