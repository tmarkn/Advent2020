# get input
with open('Day15/input.txt', 'r') as f:
    initNums = [int(x) for x in f.readline().split(',')]

# return the number said on that turn
def numberSaid(turnNum: int):
    # first n numbers said
    said = {k:v for v,k in enumerate(initNums, 1)}
    nextnum = 0
    turn = len(initNums) + 1
    # iterate until reach number of turns
    while turn != turnNum:
        # number was said before
        if nextnum in said:
            # get difference in turns
            diff = turn - said[nextnum]
            # mark down current turn
            said[nextnum] = turn
            # next number to be said is the difference between the turns
            nextnum = diff
        # number was not said before
        else:
            # mark down current turn
            said[nextnum] = turn
            # next number to be said is 0
            nextnum = 0
        # next turn
        turn += 1
    # reached select turn
    return(nextnum)

print(f'The 2020th number is {numberSaid(2020)}')
print(f'The 30000000th number is {numberSaid(30000000)}')