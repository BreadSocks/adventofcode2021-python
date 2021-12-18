file = "input.txt"

input = [[int(char) for char in x] for x in open(file).read().splitlines()]

grid = dict()
for y, line in enumerate(input):
    for x, number in enumerate(line):
        grid[(x, y)] = number

low_points = []
for key, value in grid.items():
    x = key[0]
    y = key[1]
    points = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    lowest = True
    for point in points:
        if point in grid and grid[point] <= value:
            lowest = False
            break
    if lowest:
        low_points.append(value + 1)
print(sum(low_points))