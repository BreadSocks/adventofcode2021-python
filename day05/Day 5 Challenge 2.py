file = "input.txt"

vents = [line.split(" -> ") for line in open(file).read().splitlines()]
grid = dict()
for vent in vents:
    start_x = int(vent[0].split(",")[0])
    start_y = int(vent[0].split(",")[1])
    end_x = int(vent[1].split(",")[0])
    end_y = int(vent[1].split(",")[1])
    if start_x != end_x and start_y != end_y:
        if start_x < end_x:
            x_multiplier = 1
        else:
            x_multiplier = -1

        if start_y < end_y:
            y_multiplier = 1
        else:
            y_multiplier = -1

        travel = abs(end_x - start_x)
        diag_x = start_x
        diag_y = start_y
        point = (diag_x, diag_y)
        if point in grid:
            grid[point] += 1
        else:
            grid[point] = 1
        for num in range(diag_x, diag_x + travel):
            diag_x = diag_x + x_multiplier
            diag_y = diag_y + y_multiplier
            point = (diag_x, diag_y)
            if point in grid:
                grid[point] += 1
            else:
                grid[point] = 1
    elif start_x == end_x:
        if start_y < end_y:
            ys = range(start_y, end_y + 1)
        else:
            ys = range(end_y, start_y + 1)
        for y in ys:
            point = (start_x, y)
            if point in grid:
                grid[point] += 1
            else:
                grid[point] = 1
    elif start_y == end_y:
        if start_x < end_x:
            xs = range(start_x, end_x + 1)
        else:
            xs = range(end_x, start_x + 1)
        for x in xs:
            point = (x, start_y)
            if point in grid:
                grid[point] += 1
            else:
                grid[point] = 1

print(grid)
answer = sum(map(lambda value: value >= 2, grid.values()))
print(answer)
