import statistics

file = "input.txt"

lines = [[char for char in x] for x in open(file).read().splitlines()]
mapping = {')': '(', ']': '[', '}': '{', '>': '<'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
part2_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
broken_chars = []
incomplete_scores = []
for line in lines:
    open_sets = []
    broken = False
    for char in line:
        if char in mapping.values():
            open_sets.append(char)
        elif open_sets[-1] == mapping[char]:
            open_sets.pop()
        else:
            broken_chars.append(char)  # screwed
            broken = True
            break

    if len(open_sets) > 0 and not broken:
        print("line is incomplete {}".format(open_sets))
        score = 0
        for start in open_sets.__reversed__():
            score *= 5
            score += part2_scores[start]
        incomplete_scores.append(score)


# part 1
print("Part 1: {}".format(sum([scores[x] for x in broken_chars])))

# part 2
incomplete_scores.sort()
print("Part 2: {}".format(statistics.median(incomplete_scores)))