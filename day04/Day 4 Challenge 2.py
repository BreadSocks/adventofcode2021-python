from collections import Counter

file = "input.txt"

horizontal = 0
depth = 0
lines = [list(line) for line in open(file).read().splitlines()]
switched = list(zip(*lines))
print(lines)
print(switched)
most_common = []
least_common = []
# for line in switched:
#     results = Counter(line).most_common(2)
#     most_common += results[0][0]
#     least_common += results[1][0]

oxygen_generator_values = lines.copy()
line_index = 0
while len(oxygen_generator_values) > 1:
    flipped = list(zip(*oxygen_generator_values))
    results = Counter(flipped[line_index]).most_common(2)
    if results[0][1] == results[1][1]:
        most_common = '1'  #oxygen
    else:
        most_common = results[0][0]
    oxygen_generator_values = [x for x in oxygen_generator_values if x[line_index] == most_common]
    line_index += 1

co2_scrubber_values = lines.copy()
line_index = 0
while len(co2_scrubber_values) > 1:
    flipped = list(zip(*co2_scrubber_values))
    results = Counter(flipped[line_index]).most_common()
    if results[-1][1] == results[-2][1]:
        most_common = '0'  #co2
    else:
        most_common = results[-1][0]
    co2_scrubber_values = [x for x in co2_scrubber_values if x[line_index] == most_common]
    line_index += 1

oxygen_generator_rating = int(''.join(map(str, oxygen_generator_values[0])), 2)
co2_scrubber_rating = int(''.join(map(str, co2_scrubber_values[0])), 2)

print(oxygen_generator_rating)
print(co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)
