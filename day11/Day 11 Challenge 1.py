file = "input.txt"

lines = [list(int(number) for number in x) for x in open(file).read().splitlines()]
grid = dict()
total_flashes = 0
for index_line, line in enumerate(lines):
    for index_number, number in enumerate(line):
        grid[(index_line, index_number)] = number

for step in range(0, 100):
    for x in grid:
        grid[x] += 1

    # find flashers
    flashers = [key for key in grid if grid[key] > 9]

    to_flash = flashers.copy()

    while len(to_flash) != 0:
        octopus = to_flash.pop()
        x = octopus[0]
        y = octopus[1]
        points = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                  (x - 1, y), (x + 1, y),
                  (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        for point in points:
            if point in grid:
                grid[point] += 1

        new_flashers = [key for key in grid if grid[key] > 9 and key not in flashers]
        to_flash += new_flashers
        flashers += new_flashers

    for x in [key for key in grid if grid[key] > 9]:
        grid[x] = 0

    total_flashes += len(flashers)


print(grid)
print(total_flashes)