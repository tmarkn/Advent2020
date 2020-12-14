# get input
with open('Day12/input.txt', 'r') as f:
    inp = f.readlines()

directions = [(x[0], int(x[1:])) for x in inp]

# part 1
def findDestination1(instructions):
    cardinal = ['N', 'E', 'S', 'W']
    north = east = 0
    facing = 1
    for dir in instructions:
        go, num = dir

        if go == 'F':
            go = cardinal[facing]
        if go == 'N':
            north += num
        elif go == 'E':
            east += num
        elif go == 'S':
            north -= num
        elif go == 'W':
            east -= num
        elif go == 'R':
            facing = (facing + (num // 90)) % 4
        elif go == 'L':
            facing = (facing - (num // 90)) % 4
    return north, east

# rotate clockwise
def rotateClockwise(degrees, north, east):
    # convert to < 360
    newDegrees = degrees % 360

    # return correct values
    if newDegrees == 0:
        return north, east
    elif newDegrees == 180:
        return -north, -east
    elif newDegrees == 90:
        return -east, north
    else: # degrees == 270
        return east, -north

# part 2
def findDestination2(instructions):
    # init
    shipNorth = shipEast = 0
    wpNorth = 1
    wpEast = 10
    # go through instructions
    for dir in instructions:
        go, num = dir

        # parse
        if go == 'F':
            # go in that ddirection num times
            shipNorth += wpNorth * num
            shipEast += wpEast * num
        elif go == 'N':
            # increase north waypoint
            wpNorth += num
        elif go == 'E':
            # increase east waypoint
            wpEast += num
        elif go == 'S':
            # decrease north waypoint # go more south
            wpNorth -= num
        elif go == 'W':
            # decrease east waypoint # go more east
            wpEast -= num
        elif go == 'R':
            # rotate clockwise
            wpNorth, wpEast = rotateClockwise(num, wpNorth, wpEast)
        else:
            # rotate counterclockwise (360 - num)
            wpNorth, wpEast = rotateClockwise(360 - num, wpNorth, wpEast)
    return shipNorth, shipEast

# run part 1
north, east = findDestination1(directions)
print(f'The ship is {north} units North and {east} units east')
print(f'The Manhattan distance is {abs(north) + abs(east)}')

# run part 2
north, east = findDestination2(directions)
print(f'The ship is {north} units North and {east} units east')
print(f'The Manhattan distance is {abs(north) + abs(east)}')