import math

file = "input.txt"

input = [[int(char) for char in x] for x in open(file).read().splitlines()]

grid = dict()
for y, line in enumerate(input):
    for x, number in enumerate(line):
        grid[(x, y)] = number


def basin(start_point, value, list):
    list.append((start_point, value))
    x = start_point[0]
    y = start_point[1]
    coords = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for coord in coords:
        if coord in grid and grid[coord] > value and grid[coord] != 9:
            basin(coord, grid[coord], list)
    return set(list)


basins = []
for key, value in grid.items():
    x = key[0]
    y = key[1]
    points = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    found = True
    for point in points:
        if point in grid and grid[point] <= value:
            found = False
            break
    if found:
        basins.append(basin(key, value, []))
print(basins)
print(math.prod(sorted([len(x) for x in basins])[-3:]))
