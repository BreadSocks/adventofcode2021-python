file = "input.txt"

parts = open(file).read().replace("target area: ", "").split(", ")
x_parts = [int(x) for x in parts[0].replace("x=", "").split("..")]
y_parts = [int(y) for y in parts[1].replace("y=", "").split("..")]
min_x = x_parts[0]
max_x = x_parts[1]
min_y = y_parts[0]
max_y = y_parts[1]
x_range = range(min_x, max_x + 1)
y_range = range(min_y, max_y + 1)

print("x={}..{} y={}..{}".format(min_x, max_x, min_y, max_y))

y_values = []
velocities = dict()
upper_x = max(min_x, max_x)
lower_y = min(min_y, max_y)
count = 0

for x in range(0, upper_x + 1):
    # print("Currently: x={}", x)
    for y in range(-1000, 1000):
        probe_position = (0, 0)
        highest = -float('inf')
        velocity_x = x
        velocity_y = y
        smack = False
        while probe_position[0] < upper_x and probe_position[1] > lower_y and not smack:
            probe_position = (probe_position[0] + velocity_x, probe_position[1] + velocity_y)
            if velocity_x > 0:
                velocity_x -= 1
            elif velocity_x < 0:
                velocity_x += 1
            velocity_y -= 1
            highest = max(highest, probe_position[1])
            if probe_position[0] in x_range and probe_position[1] in y_range:
                smack = True

        if smack:
            y_values.append(highest)
            count += 1
            velocities[(x, y)] = highest

# print(y_values)
print(max(y_values))
# print(len(y_values))
print(y_values)
print(len(y_values))
print(velocities)
print(len(velocities.keys()))
print(count)
