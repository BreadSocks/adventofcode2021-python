file = "input.txt"

ups = 0
downs = 0
no_change = 0
depths = [int(line) for line in open(file).read().splitlines()]
for index, depth in enumerate(depths):
    if index == 0:
        no_change += 1
    elif depth > depths[index - 1]:
        ups += 1
    elif depth < depths[index - 1]:
        downs += 1
    else:
        no_change += 1

print("Increases: ", str(ups), "\nDecreases: ", str(downs), "\nNo change: ", str(no_change))
