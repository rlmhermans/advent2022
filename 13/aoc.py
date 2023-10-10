from ast import literal_eval
from functools import cmp_to_key

def compare(left, right):
    smallest = min(len(left), len(right))
    for idx in range(smallest):
        result = 0
        if type(left[idx]) == list and type(right[idx]) == list:
            result = compare(left[idx], right[idx])

        elif type(left[idx]) == list and type(right[idx]) != list:
            result = compare(left[idx], [right[idx]])

        elif type(left[idx]) != list and type(right[idx]) == list:
            result = compare([left[idx]], right[idx])

        else: result = left[idx] - right[idx]

        if result != 0:
            return result

    return len(left) - len(right)


with open('input') as f:
    input = list(map(literal_eval, f.read().replace('\n\n', '\n').splitlines()))

markers = [[[2]], [[6]]]
input += markers

sorted_input = sorted(input, key=cmp_to_key(compare))

mult = 1
for m in markers:
    mult *= (sorted_input.index(m) + 1)

print(mult)