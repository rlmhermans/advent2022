adjacent_deltas = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0), (0,  0), (1,  0),
    (-1,  1), (0,  1), (1,  1)
]


def adjacent(knotl, knotf):
    adjacent_positions = []
    for dx, dy in adjacent_deltas:
        adjacent_positions.append((knotl[0] + dx, knotl[1] + dy))

    return knotf in adjacent_positions


NR_OF_KNOTS = 10
with open('input') as f:
    input = f.read().splitlines()

headings = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
knots = [(0, 0) for _ in range(NR_OF_KNOTS)]
visited = {(0, 0)}

for line in input:
    d, steps = line.split(' ')
    dx, dy = headings[d]

    for _ in range(int(steps)):
        x, y = knots[0]
        knots[0] = (x + dx, y + dy)

        for k in range(len(knots) - 1):
            if not adjacent(knots[k], knots[k+1]):
                xl, yl = knots[k]
                xf, yf = knots[k+1]

                if   xl == xf and yl > yf : knots[k+1] = (xf,   yf+1)
                elif xl == xf and yl < yf : knots[k+1] = (xf,   yf-1)
                elif xl > xf  and yl == yf: knots[k+1] = (xf+1, yf)
                elif xl < xf  and yl == yf: knots[k+1] = (xf-1, yf)
                elif xl > xf  and yl > yf : knots[k+1] = (xf+1, yf+1)
                elif xl < xf  and yl > yf : knots[k+1] = (xf-1, yf+1)
                elif xl > xf  and yl < yf : knots[k+1] = (xf+1, yf-1)
                elif xl < xf  and yl < yf : knots[k+1] = (xf-1, yf-1)
            
            else: break

        visited.add(knots[-1])

print(len(visited))