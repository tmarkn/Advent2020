# get input
with open('Day14/input.txt', 'r') as f:
    instructions = f.readlines()

# part 1
def applyBitMask(mask, value):
    value = '{:036b}'.format(int(value))
    string = ''
    for i in range(36):
        if mask[i] == 'X':
            string += value[i]
        else:
            string += mask[i]
    
    return int(string, 2)

# part 2
def applyBitMask2(mask, value):
    value = '{:036b}'.format(int(value))
    string = ''
    for i in range(36):
        if mask[i] == '0':
            string += value[i]
        else:
            string += mask[i]
    
    return string

# find all possible addresses from arr # recursive
# find first X and replace with both 0 and 1
# if another X is present, run through again program again until all X's are gone
def possibleAddresses(arr):
    # array of items to run through again
    tempArr = []
    returnArr = []
    for item in arr:
        firstX = item.find('X')
        if firstX == -1:
            returnArr.append(item)
        else:
            tempArr.append(item[:firstX] + '0' + item[firstX+1:])
            tempArr.append(item[:firstX] + '1' + item[firstX+1:])
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