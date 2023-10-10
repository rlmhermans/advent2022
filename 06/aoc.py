with open('input') as f:
    input = f.read()

LENGTH = 14

for i in range(len(input)):
    s = set(input[i:i+LENGTH])
    if(len(s) == LENGTH):
        break

print(i+LENGTH)
