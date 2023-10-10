with open('input') as f:
    input = f.read().splitlines()

solids = set()
lowest = 0
for l in input:
    points = l.split(' -> ')
    for i in range(len(points) - 1):
        frm = list(map(int, points[i].split(',')))
        to = list(map(int, points[i + 1].split(',')))
        lowest = max(lowest, frm[1], to[1])

        if frm[0] == to[0]:
            vert = [frm[1], to[1]]
            for v in range(min(vert), max(vert) + 1):
                solids.add((frm[0], v))
        else:
            hor = [frm[0], to[0]]
            for h in range(min(hor), max(hor) + 1):
                solids.add((h, frm[1]))

ROCKS = len(solids)

rock_pos = (500, 0)

while(not (500, 0) in solids):
    below = (rock_pos[0], rock_pos[1] + 1)
    left_below = (rock_pos[0] - 1, rock_pos[1] + 1)
    right_below = (rock_pos[0] + 1, rock_pos[1] + 1)

    if below[1] == lowest + 2:
        solids.add(rock_pos)
        rock_pos = (500, 0)

    elif below in solids:
        if left_below in solids:
            if right_below in solids:
                solids.add(rock_pos)
                rock_pos = (500, 0)
            else:
                rock_pos = right_below
        else:
            rock_pos = left_below
    else:
        rock_pos = below

print(len(solids) - ROCKS)
