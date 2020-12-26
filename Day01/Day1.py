# get input
with open('Day01/input.txt', 'r') as f:
    inp = [int(x) for x in f.readlines()]

# using two numbers
def twoNums(arr, num):
    # first number
    for x in range(len(arr)):
        # second number
        for y in range(x+1, len(arr)):
            # check for correct numbers and break
            if arr[x] + arr[y] == num:
                return arr[x], arr[y], arr[x] * arr[y]

# using three numbers
def threeNums(arr, num):
    # first number
    for x in range(len(arr)):
        # second number
        for y in range(x+1, len(arr)):
            # third number
            for z in range(x+2, len(arr)):
                # check for correct numbers and break
                if arr[x] + arr[y] + arr[z] == num:
                    return arr[x], arr[y], arr[z], arr[x] * arr[y] * arr[z]

print('The two numbers are {} and {}\n\tTheir product is {}'.format(*twoNums(inp, 2020)))
print('The three numbers are {}, {}, and {}\n\tTheir product is {}'.format(*threeNums(inp, 2020)))