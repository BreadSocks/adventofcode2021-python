file = "input.txt"

input = [x.split(" | ") for x in open(file).read().splitlines()]

appearances = 0
for entry in input:
    patterns = entry[0].split()
    output_values = entry[1].split()
    for value in output_values:
        if len(value) == 2 or len(value) == 4 or len(value) == 3 or len(value) == 7:
            appearances += 1
print(input)
print(appearances)
