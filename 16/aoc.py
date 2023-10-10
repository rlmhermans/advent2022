from collections import defaultdict
from itertools import product

with open('input') as f:
    input = f.read().splitlines()

nodes = {}
valve_rooms = set()
for line in input:
    words = line.split(' ')
    name = words[1]
    flow = int(words[4][5:-1])
    if flow > 0:
        valve_rooms.add(name)
    paths = ''.join(words[9:]).split(',')
    nodes[name] = [flow, paths]

edges = defaultdict(defaultdict)

for origin in {'AA'} | valve_rooms:
    for target in valve_rooms - {origin}:
        visited = []
        q = [[origin, 0]]
        while len(q) != 0:
            node, steps = q.pop(0)
            visited.append(node)

            if node == target:
                edges[origin][node] = steps
                break

            else:
                for p in nodes[node][1]:
                    if p not in visited:
                        q.append([p, steps + 1])

MINUTES = 26
highest_per_valves = defaultdict(int)


def visit(current='AA', open=set(), time_spent=0, current_flow=0, total_flow=0):
    global highest_per_valves
    if current in valve_rooms:
        open.add(current)
        time_spent += 1
        total_flow += current_flow
        current_flow += nodes[current][0]

    highest_per_valves[frozenset(open)] = max(highest_per_valves[frozenset(
        open)], total_flow + current_flow * (MINUTES - time_spent))

    for n, s in edges[current].items():
        if n not in open and time_spent + s < MINUTES:
            visit(n, open.copy(), time_spent + s,
                  current_flow, total_flow + current_flow * s)


visit()

highest = 0
combinations = product(highest_per_valves.keys(), repeat=2)
for c1, c2 in combinations:
    if c1.isdisjoint(c2):
        flow = highest_per_valves[c1] + highest_per_valves[c2]
        highest = max(highest, flow)

print('Part 2:', highest)