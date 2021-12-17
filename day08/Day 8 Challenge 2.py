file = "input.txt"

input = [x.split(" | ") for x in open(file).read().splitlines()]

total = 0
for entry in input:
    patterns = entry[0].split()
    output_values = entry[1].split()
    mapping = dict.fromkeys(range(10))
    numbers = []
    mapping[1] = [char for char in next(x for x in patterns if len(x) == 2)]
    mapping[4] = [char for char in next(x for x in patterns if len(x) == 4)]
    mapping[7] = [char for char in next(x for x in patterns if len(x) == 3)]
    mapping[8] = [char for char in next(x for x in patterns if len(x) == 7)]

    while None in mapping.values():
        for pattern in patterns:
            characters = [char for char in pattern]
            if len(pattern) == 6:
                if all(x in characters for x in mapping[4]):
                    mapping[9] = characters
                elif all(x in characters for x in mapping[1]):
                    mapping[0] = characters
                else:
                    mapping[6] = characters
            if len(pattern) == 5:
                if mapping[6] is not None and all(x in mapping[6] for x in characters):
                    mapping[5] = characters
                elif mapping[9] is not None and all(x in mapping[9] for x in characters):
                    mapping[3] = characters
                elif mapping[6] is not None and mapping[9] is not None:
                    mapping[2] = characters

    for output in output_values:
        for key, value in mapping.items():
            if len(value) == len(output) and len(output) == len(set(value).intersection(output)):
                numbers.append(key)
                break

    total += int(''.join(map(str, numbers)))
print(total)