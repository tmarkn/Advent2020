# get input
with open('Day10/input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

# organize numbers
numbers.sort()
# add ends 
# starts at 0
# ends with last + 3
numbers.insert(0, 0)
numbers.append(max(numbers) + 3)

# check differences between squential numbers
difference = [0, 0, 0]

# loop through, get their differences, append to array
for i in range(len(numbers) - 1):
    diff = numbers[i+1] - numbers[i]
    difference[diff-1] += 1

print(f'Number of 1s: {difference[0]}')
print(f'Number of 3s: {difference[2]}')
print(f'Their product is {difference[0] * difference[2]}')

# get number of possible arrangements
numb = {}
# start from bottom
for num in reversed(numbers):
    routes = 0
    # check if connected numbers are in dictionary
    for i in range(num+1, num+4):
        # add to current
        if i in numb:
            routes += numb[i]
    # no previous routes
    if routes == 0:
        routes = 1
    numb[num] = routes

# now we're here
print(f'Possible number of arrangements {numb[0]}')