with open('input') as f:
    throws = [(o, s) for o, s in [l.split(' ') for l in f.read().splitlines()]]

scoring_table = {
    ('A', 'X'): 0+3,
    ('A', 'Y'): 3+1,
    ('A', 'Z'): 6+2,
    ('B', 'X'): 0+1,
    ('B', 'Y'): 3+2,
    ('B', 'Z'): 6+3,
    ('C', 'X'): 0+2,
    ('C', 'Y'): 3+3,
    ('C', 'Z'): 6+1
}

score = 0

for t in throws:
    score += scoring_table[t]

print(score)