with open('input') as f:
    input = f.read().splitlines()

# Part 1
total = 0
for i in input:
    half = int(len(i)/2)
    intersect = set(i[:half]).intersection(i[half:]).pop()
    total += ord(intersect)-38 if intersect.isupper() else ord(intersect)-96

print(total)

# Part 2
total = 0
for i in range(0, len(input), 3):
    intersect = set(input[i]).intersection(input[i+1]).intersection(input[i+2]).pop()
    total += ord(intersect)-38 if intersect.isupper() else ord(intersect)-96

print(total)