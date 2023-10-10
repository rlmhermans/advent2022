# import re

with open('input') as f:
    input = f.read().splitlines()
    # print(sum([1 if not s1.isdisjoint(s2) else 0 for s1, s2 in [(set(range(a, b+1)), set(range(c, d+1))) for a, b, c, d in [map(int, n) for n in [re.findall('\d+', l) for l in f.read().splitlines()]]]]))


def makeRangeSet(s):
    rangeStart, rangeEnd = s.split('-')
    return set(range(int(rangeStart), int(rangeEnd)+1))


total = 0
totalOverlap = 0
for i in input:
    r1, r2 = i.split(',')
    rSet1 = makeRangeSet(r1)
    rSet2 = makeRangeSet(r2)

    #Part 1
    if rSet1.issubset(rSet2) or rSet2.issubset(rSet1):
        total += 1

    #Part 2
    if len(rSet1 & rSet2) is not 0:
        totalOverlap += 1

print(total)
print(totalOverlap)