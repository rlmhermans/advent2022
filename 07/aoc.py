class Node:
    def __init__(self, path, size, parent):
        self.path = path
        self.size = size
        self.parent = parent
        self.children = set()

    def getSize(self):
        size = self.size

        for c in self.children:
            size += c.getSize()

        return size


with open('input') as f:
    input = f.read().split('$')

nodes = {'/': Node('/', 0, '')} # Kleine shortcut
current_node = nodes['/']

for i in input[2:]:
    items = i.strip().split('\n')
    command = items[0].split(' ')

    match command[0]:
        case 'cd':
            current_node = current_node.parent if (command[1] == '..') else nodes[current_node.path + command[1]]
        case 'ls':
            for item in items[1:]:
                part = item.split(' ')
                size = 0 if (part[0] == 'dir') else int(part[0])
                path = current_node.path + part[1]
                new = Node(path, size, current_node)
                nodes[path] = new
                current_node.children.add(new)

MAX = 70000000
UPDATE = 30000000
remainder = UPDATE - (MAX - nodes['/'].getSize())

smallest = MAX
for n in nodes.values():
    if(n.size == 0):
        size = n.getSize()
        if(remainder <= size <= smallest): 
            smallest = size

print(smallest)