with open('input') as f:
    input = f.read().splitlines()

acc = 0
elves = []

for line in input:
    if line == "":
        elves.append(acc)
        acc = 0

    else: 
        acc += int(line)

elves.append(acc)

print(max(elves)) # Part 1

list.sort(elves)
print(sum(elves[-3:])) # Part 2