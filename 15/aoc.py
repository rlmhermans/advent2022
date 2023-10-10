MAX = 4000000
# MAX = 20
with open('input') as f:
    input = f.read().splitlines()


def range_for(p, d, r):
    left = d - abs(r - p[1])
    if left < 0:
        return
    x = p[0]
    return [max(0, x - left), min(x + left, MAX)]


def combined(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    combined_ranges = [sorted_ranges[0]]
    current = 0
    for r in sorted_ranges:
        _ , current_max = combined_ranges[current]
        r_min, r_max = r
        if r_min <= current_max and r_max > current_max:
            combined_ranges[current][1] = r_max
        
        elif r_min > current_max:
            current += 1
            combined_ranges.append(r)

    return combined_ranges


sensors = []
for i in input:
    p1, p2 = [list(map(int, y)) for y in [p.split(', y=')
                                          for p in i[12:].split(': closest beacon is at x=')]]
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    sensors.append([p1, dist])

for y in range(0, MAX + 1):
    ranges = []
    for s in sensors:
        found_range = range_for(s[0], s[1], y)
        if found_range != None:
            ranges.append(found_range)

    comb = combined(ranges)
    if len(comb) > 1:
        break

print('x:', comb[0][1] + 1, 'y:', y)
