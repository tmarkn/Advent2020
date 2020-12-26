import math

def binaryPos(maxPos, string, lowerChar):
    min = 0
    max = maxPos

    for char in string:
        # lower half
        if char == lowerChar:
            max = max - ((max - min + 1) // 2)
        # higher half
        else:
            min = min + ((max - min + 1) // 2)
    return min

def seatPos(passSpecifier):
    # find position
    row = binaryPos(127, passSpecifier[:-3], 'F')
    column = binaryPos(7, passSpecifier[7:], 'L')

    # calculate id
    return row * 8 + column

# get input
with open('Day05/input.txt', 'r') as f:
    boardPasses = f.readlines()

# parse all boarding passes
passIDs = [seatPos(bPass) for bPass in boardPasses]

# highest seat id
print(f'The highest seat ID is {max(passIDs)}')

# missing seat id
missingSeat = sum(range(min(passIDs), max(passIDs) + 1)) - sum(passIDs)
print(f'Your seat ID is {missingSeat}')