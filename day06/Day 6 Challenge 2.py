file = "input.txt"

initial_states = [int(x) for x in open(file).read().split(",")]
print("Initial state: " + str(initial_states))
states = dict.fromkeys(range(9), 0)
for state in initial_states:
    states[state] += 1
counter = 0
print(states)
while counter < 256:
    new_states = dict.fromkeys(range(9), 0)
    for key in states:
        if key == 0:
            new_states[8] = states[key]  # new one
            new_states[6] += states[key]
        else:
            new_states[key - 1] += states[key]
    counter += 1
    states = new_states
print(sum(states.values()))
