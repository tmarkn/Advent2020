# get input
with open('Day14/input.txt', 'r') as f:
    instructions = f.readlines()

# part 1
def applyBitMask(mask, value):
    # change to binary
    value = '{:036b}'.format(int(value))
    string = ''
    # go through string
    for i in range(36):
        # set normal value if X
        if mask[i] == 'X':
            string += value[i]
        # set mask value if 0 or 1
        else:
            string += mask[i]
    
    return int(string, 2)

# part 2
def applyBitMask2(mask, value):
    # change to binary
    value = '{:036b}'.format(int(value))
    string = ''
    # go through string
    for i in range(36):
        # set normal value if 0
        if mask[i] == '0':
            string += value[i]
        # set mask value if 1 or X
        else:
            string += mask[i]
    
    return string

# find all possible addresses from arr # recursive
def possibleAddresses(arr):
    # array of items to run through again
    tempArr = []
    returnArr = []
    # go through each item in arr
    for item in arr:
        # get the location of first X
        firstX = item.find('X')
        # did not find an X  # finished this address
        if firstX == -1:
            returnArr.append(item)
        # found an X
        else:
            # replace X with 0 and 1 then do another pass
            tempArr.append(item[:firstX] + '0' + item[firstX+1:])
            tempArr.append(item[:firstX] + '1' + item[firstX+1:])
    # do another pass then add to finished
    if len(tempArr):
        returnArr += possibleAddresses(tempArr)
    return returnArr

# part 1
memory = {}
# run through instructions
for instruct in instructions:
    # isolate values
    loc, value = instruct.strip().split(' = ')
    # change mask value
    if loc == 'mask':
        mask = value
    # apply mask value and set address equal to that value
    else:
        address = int(loc[loc.find('[')+1:loc.find(']')])
        memory[address] = applyBitMask(mask, value)

print(f'The sum of the remaining values in memory are {sum(memory.values())}')

# part 2
memory = {}
# run through instructions
for instruct in instructions:
    # isolate values
    loc, value = instruct.strip().split(' = ')
    # change mask value
    if loc == 'mask':
        mask = value
    # apply mask
    else:
        # apply mask on address
        address = int(loc[loc.find('[')+1:loc.find(']')])
        addresses = possibleAddresses([applyBitMask2(mask, address)])
        # set all addresses to value
        for address in addresses:
            memory[address] = int(value)
        
print(f'The sum of the remaining values in memory are {sum(memory.values())}')