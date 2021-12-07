file = "input.txt"

states = [int(x) for x in open(file).read().split(",")]
print("Initial state: " + str(states))
counter = 0
while counter < 80:
    new_states = states.copy()
    for index, value in enumerate(states):
        if value == 0:
            new_states[index] = 6
            new_states.append(8)
        else:
            new_states[index] -= 1
    counter += 1
    print("After {0} days: {1}".format(counter, str(new_states)))
    states = new_states

print(len(states))