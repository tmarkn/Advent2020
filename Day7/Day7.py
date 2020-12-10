import re

# magic regex pattern remove excess words (bag)(contains)
bagsPattern = re.compile('\s*bags?[,.\s]*(?:contain)*\s*')

class TreeNode:
    def __init__(self, color):
        self.color = color
        self.parents = []
        self.children = []
    
    # part 1
    # count all bigger bags (once)
    def countAncestors(self):
        queue = self.parents
        counted = set()

        while len(queue):
            current = queue.pop(0)
            counted.add(current)
            queue += [x for x in current.parents if x not in counted]
        return len(counted)
    
    # part 2
    # count all smaller bags
    def rabbitHole(self, top = True):
        # don't count self
        if top:
            rabbits = 0
        else:
            rabbits = 1
        # count all
        for rabbit in self.children:
            rabbits += rabbit[0] * rabbit[1].rabbitHole(top=False)
        return rabbits

# get input
with open('Day7/input.txt', 'r') as f:
    rawRules = f.readlines()

colors = {}
rules = [bagsPattern.split(x)[:-1] for x in rawRules]

for rule in rules:
    if rule[0] not in colors:
        color = TreeNode(rule[0])
        colors[rule[0]] = color
    else:
        color = colors[rule[0]]
    for innerBag in rule[1:]:
        # end of tree branch
        if innerBag == 'no other':
            break

        # not end
        # split number and color
        spaceIndex = innerBag.find(' ')
        num = int(innerBag[:spaceIndex])
        smolBag = innerBag[spaceIndex+1:]

        # make new bag
        if smolBag not in colors:
            smolColor = TreeNode(smolBag)
            colors[smolBag] = smolColor
        # find bag
        else:
            smolColor = colors[smolBag]

        # add children andd parents
        smolColor.parents.append(color)
        color.children.append((num, smolColor))

# part 1
print(f'The number of bag colors that eventually contain at least one shiny gold bag is {colors["shiny gold"].countAncestors()}')
# part 2
print(f'The number of bags in your shiny gold bag is {colors["shiny gold"].rabbitHole()}') 