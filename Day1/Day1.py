## get input
with open('Day1/input.txt', 'r') as f:
    inp = [int(x) for x in f.readlines()]

def twoNums(arr):
    ## first number
    for x in range(len(arr)):
        ## second number
        for y in range(x+1, len(arr)):
            ## check for correct numbers and break
            if arr[x] + arr[y] == 2020:
                return arr[x], arr[y], arr[x] * arr[y]

def threeNums(arr):
    ## first number
    for x in range(len(arr)):
        ## second number
        for y in range(x+1, len(arr)):
            ## third number
            for z in range(x+2, len(arr)):
                ## check for correct numbers and break
                if arr[x] + arr[y] + arr[z] == 2020:
                    return arr[x], arr[y], arr[z], arr[x] * arr[y] * arr[z]

print(twoNums(inp))
print(threeNums(inp))
