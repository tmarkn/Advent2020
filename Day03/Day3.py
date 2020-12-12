# get input
with open('Day3/input.txt', 'r') as f:
    map = [x[:-1] for x in f.readlines()]

# get dimesions
width = len(map[0])
height = len(map)

# use the slope on map and return number of trees
def traversePath(right, down):
    pos = 0
    trees = 0
    # skip 0th row
    for x in range(down, height, down):
        pos = (pos + right) % width
        # check if tree is hit
        if map[x][pos] == '#':
            trees += 1
    return trees

# get all five slopes
slopes = [
    traversePath(right=1, down=1),
    traversePath(right=3, down=1),  # part 1
    traversePath(right=5, down=1),
    traversePath(right=7, down=1),
    traversePath(right=1, down=2)
]
print(f'Your slopes are: {", ".join(str(x) for x in slopes)}')

# multiply slopes together
value = 1
for slope in slopes:
    value *= slope
print(f'The product of the slopes is: {value}')