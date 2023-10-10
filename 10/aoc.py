with open('input') as f:
    input = f.read().splitlines()

x = 1
cycles = [0]
for line in input:
    l = line.split()
    if l[0] == 'addx':
        y = int(l[1])
        cycles += [x, x + y]
        x += y
    elif l[0] == 'noop':
        cycles += [x]

sum = 0
for i in range(20, 221, 40):
    sum += i * cycles[i-1]

print('Part 1:', sum)

# Part 2
for j in range(6):
    for cycle in range(40):
        sprite_pos = cycles[cycle + 40 * j]
        p = '#' if cycle == sprite_pos - 1 or cycle == sprite_pos or cycle == sprite_pos + 1 else '.'
        print(p, end='')
    print()