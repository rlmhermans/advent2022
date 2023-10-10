import re

with open('input') as f:
    start, instructions = f.read().split('\n\n')

start = start.splitlines()[:-1]
start.reverse()
pos = list(range(1, len(start[0]) + 1, 4))
stacks = {}

for i in range(len(pos)):
    stacks[i+1] = []

for l in start:
    for i in range(len(pos)):
        if l[pos[i]] != ' ':
            stacks[i+1].append(l[pos[i]])

for i in instructions.splitlines():
    amount, source, target = [int(n) for n in re.findall('\d+', i)]

    # Part 1
    # for _ in range(amount):
    #     crate = stacks[source].pop()
    #     stacks[target].append(crate)

    # Part 2
    crates = stacks[source][-amount:]
    stacks[source] = stacks[source][:-amount]
    stacks[target] += crates

for v in stacks.values():
    print(v[-1:])