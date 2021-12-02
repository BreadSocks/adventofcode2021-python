file = "input.txt"

horizontal = 0
depth = 0
instructions = [line.split(" ") for line in open(file).read().splitlines()]
for instruction in instructions:
    command = instruction[0]
    value = int(instruction[1])
    if command == "forward":
        horizontal += value
    elif command == "up":
        depth -= value
    elif command == "down":
        depth += value

print("Distance: ", str(horizontal), "\nDepth: ", str(depth), "\nTotal: ", str(depth * horizontal))
