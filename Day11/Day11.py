pos = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

# get input
with open('Day11/input.txt', 'r') as f:
    inp = f.readlines()

# format seats
seats = []
for x in inp:
    seats.append([*x.strip()])

# part 1
def changeSeat(arr, x, y):
    adjacentWeirdos = 0
    # do all surrounding (x)
    for i in range(x-1, x+2):
        # edge
        if i < 0 or i >= len(arr):
            continue
        # do all surrounding (y)
        for j in range(y-1, y+2):
            # edge
            if j < 0 or j >= len(arr[0]):
                continue
            # same position
            if (x, y) == (i, j):
                continue
            # check for neighbors
            if arr[i][j] == '#':
                adjacentWeirdos += 1
    # occupied or not
    seat = arr[x][y]
    if adjacentWeirdos == 0:
        seat =  '#'
    if adjacentWeirdos >= 4:
        seat =  'L'
    if seat == arr[x][y]:
        return None
    return seat

# go in direction until hit seat or goes off edge
def checkDirection(arr, x, y, pos1, pos2):
    i = pos1
    j = pos2
    while True:
        i += x
        j += y
        # edge
        if i < 0 or i >= len(arr):
            return False
        if j < 0 or j >= len(arr[0]):
            return False
        # seat
        if arr[i][j] == '#':
            return True
        if arr[i][j] == 'L':
            return False

# part 2
def changeSeat2(arr, x, y):
    adjacentWeirdos = 0
    # check direction
    for xDir, yDir in pos:
        if checkDirection(arr, xDir, yDir, x, y):
            adjacentWeirdos += 1
    
    # occupied or not
    seat = arr[x][y]
    if adjacentWeirdos == 0:
        seat =  '#'
    if adjacentWeirdos >= 5:
        seat =  'L'
    if seat == arr[x][y]:
        return None
    return seat

# do pass on seats and update each pass until no changes are made
def processSeats(arr, version):
    seatmap = arr
    # do until no changes mode
    while True:
        temp = [x[:] for x in seatmap]
        updated = False
        # do pass
        for i in range(len(seatmap)):
            for j in range(len(seatmap[0])):
                # skip floor
                if temp[i][j] == '.':
                    continue
                # check which version to run
                if version == 1:
                    returned = changeSeat(seatmap, i, j)
                elif version == 2:
                    returned = changeSeat2(seatmap, i, j)
                # update seat
                if returned != None:
                    temp[i][j] = returned
                    updated = True
        # check if updated
        if updated == False:
            break
        # save current iteration
        seatmap = temp
    return seatmap

v1 = sum(x.count("#") for x in processSeats(seats, 1))
v2 = sum(x.count('#') for x in processSeats(seats, 2))
print(f'The number of seats occupied is {v1} for method 1')
print(f'The number of seats occupied is {v2} for method 2')