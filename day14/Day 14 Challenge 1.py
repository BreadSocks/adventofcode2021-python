file = "input.txt"

lines = open(file).read().splitlines()
template = list(lines[0])
counts = dict()
for x in range(0, len(template) - 1):
    pair = "{}{}".format(template[x], template[x + 1])
    if pair in counts:
        counts[pair] += 1
    else:
        counts[pair] = 1

rules = dict()
for index in range(2, len(lines)):
    parts = lines[index].split(" -> ")
    rules[parts[0]] = parts[1]

print(rules)
print(counts)
for step in range(0, 10):
    new_counts = counts.copy()
    for pair, count in counts.items():
        for _ in range(0, count):
            new_counts[pair] -= 1
            substitution = rules[pair]
            new_pair1 = "{}{}".format(pair[0], substitution)
            new_pair2 = "{}{}".format(substitution, pair[1])
            if new_pair1 in new_counts:
                new_counts[new_pair1] += 1
            else:
                new_counts[new_pair1] = 1
            if new_pair2 in new_counts:
                new_counts[new_pair2] += 1
            else:
                new_counts[new_pair2] = 1
    counts = new_counts
    print(counts)
print(sum(counts.values()))
print(counts)

totals = dict()
for key in counts.keys():
    parts = list(key)
    if parts[0] not in totals:
        totals[parts[0]] = 0
    if parts[1] not in totals:
        totals[parts[1]] = 0

    if parts[0] == parts[1]:
        totals[parts[0]] += (counts[key] * 2)
    else:
        totals[parts[0]] += counts[key]
        totals[parts[1]] += counts[key]

for key in totals:
    value = totals[key]
    if value % 2 != 0:
        value += 1
    totals[key] = value / 2
print(max(totals.values()) - min(totals.values()))
