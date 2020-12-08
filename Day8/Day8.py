# get input
with open('Day8/input.txt', 'r') as f:
    instructions = [x.split() for x in f.readlines()]

# copy instructions # deep copy
newInstruct = [x[:] for x in instructions]
i = 0

# loop through, changing one instruction at a time, and run instructions
while i < len(newInstruct):
    accumulator = 0
    index = 0
    visited = set()

    # run instructions
    while True:
        # check if looping
        if index in visited:
            print(f'Looping:\n\tAccumulator = {accumulator}')
            break
        visited.add(index)
        # check for cleared instructions
        try:
            instr, value = newInstruct[index]
        except IndexError:
            # cleared
            if index == len(newInstruct):
                print(f'Finished by changing line {i}\n\tAccumulator = {accumulator}')
                exit()
            # index out of bounds
            else:
                print('Invalid Index')
                break
        
        # do instructions
        if instr == 'acc':
            accumulator += int(value)
            index += 1
        elif instr == 'jmp':
            index += int(value)
        else: #NOP
            index += 1
    
    # reset instruction
    newInstruct = [x[:] for x in instructions]
    # find next 'nop' or 'jmp'
    while newInstruct[i][0] == 'acc':
        i += 1
    # toggle 'jmp'/'nop'
    if newInstruct[i][0] == 'nop':
        newInstruct[i][0] = 'jmp'
    else:
        newInstruct[i][0] = 'nop'
    # go to next
    i += 1

# shouldn't get here
print('Something is wrong')