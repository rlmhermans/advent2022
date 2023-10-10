monkeys = {}
modulo = 1

class Monkey:
    def __init__(self, items, op, test, m1, m2):
        self.items = items
        self.op = op
        self.test = test
        self.m1 = m1
        self.m2 = m2
        self.items_seen = 0

    def turn(self):
        for i in self.items:
            self.items_seen += 1
            new = self.op(i)
            next = self.m1 if new % self.test == 0 else self.m2
            monkeys[next].items.append(new % modulo)

        self.items = []


def make_op(s):
    match s.split():
        case ['*', 'old']: return lambda x: x * x
        case ['*', v]: return lambda x: x * int(v)
        case ['+', v]: return lambda x: x + int(v)


with open('input') as f:
    input = [l.split('\n ') for l in f.read().split('\n\n')]


for i in input:
    items = [int(x) for x in i[1][17:].split(', ')]
    op = make_op(i[2].split("old ")[1])
    test = int(i[3].split("by ")[1])
    modulo *= test
    m1 = int(i[4].split("monkey ")[1])
    m2 = int(i[5].split("monkey ")[1])
    monkeys[int(i[0][7:-1])] = Monkey(items, op, test, m1, m2)


for r in range(10000):
    for x in range(len(monkeys)):
        monkeys[x].turn()

inspections = list(reversed(sorted([m.items_seen for m in monkeys.values()])))
print(inspections[0] * inspections[1])
