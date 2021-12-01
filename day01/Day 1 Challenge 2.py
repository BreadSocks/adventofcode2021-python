file = "input.txt"

ups = 0
downs = 0
no_change = 0
results = []
depths = [int(line) for line in open(file).read().splitlines()]
for index in range(2, len(depths)):
    total = sum(depths[index - 2: index + 1])
    results.append(total)
    if len(results) == 1:
        no_change += 1
    else:
        previous = results[-2]
        if total > previous:
            ups += 1
        elif total < previous:
            downs += 1
        else:
            no_change += 1

print("Increases: ", str(ups), "\nDecreases: ", str(downs), "\nNo change: ", str(no_change))
print(results)