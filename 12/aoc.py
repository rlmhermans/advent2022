with open('input') as f:
    input = [list(l) for l in f.read().splitlines()]

vectors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def valid(pos):
    return 0 <= pos[0] < len(input) and 0 <= pos[1] < len(input[0])

def get_neighbors(pos):
    neighbors = []
    for v in vectors:
        next = [pos[0] + v[0], pos[1] + v[1]]
        if valid(next): neighbors.append(next)

    return neighbors

def shortest(s):
    q = []
    q.append((s, 0))
    visited = [s]

    while len(q) != 0:
        current = q.pop(0)
        current_pos = current[0]
        current_height = input[current_pos[0]][current_pos[1]]
        if current_height == '{':
            return current[1]

        neighbors = get_neighbors(current_pos)
        for n in neighbors:
            if n not in visited:
                next_height = input[n[0]][n[1]]
                if ord(next_height) <= ord(current_height) + 1:
                    visited.append(n)
                    q.append((n, current[1] + 1))

lengths = []
for y in range(len(input)):
    lengths.append(shortest((y, 0)))

print(min(lengths))