def score_treeline(line):
    score = 0
    for l in line:
        score += 1
        if l >= current_tree_height:
            break

    return score


with open('input') as f:
    input = f.read().splitlines()

arr = [list(map(int, l)) for l in [list(x) for x in [i for i in input]]]

all = len(arr) * len(arr[0])
count = 0
highest_score = 0
for r in range(1, len(arr) - 1):
    for c in range(1, len(arr[0]) - 1):
        left = arr[r][:c]
        left.reverse()
        right = arr[r][c + 1:]
        down = [arr[r][c] for r in range(r + 1, len(arr))]
        up = [arr[r][c] for r in range(r - 1, -1, -1)]

        current_tree_height = arr[r][c]

        count += min([max(left), max(right), max(up),
                     max(down), current_tree_height]) == current_tree_height

        score = score_treeline(left) * score_treeline(right) * score_treeline(down) * score_treeline(up)
        highest_score = max(highest_score, score)

print('Part 1:', all - count)
print('Part 2:', highest_score)
