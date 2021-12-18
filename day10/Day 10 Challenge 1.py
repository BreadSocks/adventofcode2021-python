file = "input.txt"

lines = [[char for char in x] for x in open(file).read().splitlines()]
mapping = {')': '(', ']': '[', '}': '{', '>': '<'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
broken_chars = []
for line in lines:
    open_sets = []
    for char in line:
        if char in mapping.values():
            open_sets.append(char)
        elif open_sets[-1] == mapping[char]:
            open_sets.pop()
        else:
            broken_chars.append(char)  # screwed
            break


print(sum([scores[x] for x in broken_chars]))
print(broken_chars)
    # counts = dict.fromkeys(["brackets", "squares", "braces", "chevrons"], 0)
    # for char in line:
    #     if char == '(':
    #         counts["brackets"] += 1
    #     elif char == '[':
    #         counts["squares"] += 1
    #     elif char == '{':
    #         counts["braces"] += 1
    #     elif char == '<':
    #         counts["chevrons"] += 1
    #     elif char == ')':
    #         counts["squares"] -= 1
    #     elif char == ']':
    #         counts["braces"] -= 1
    #     elif char == '}':
    #         counts["chevrons"] -= 1
    #     elif char == '>':
    #         counts["squares"] -= 1
    #
    #     if -1 in counts.values():
    #         print("line is corrupt {} {}".format(line, counts))
    #         break
