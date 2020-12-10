# get input
with open('Day9/input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

# check if the number is a sum of two of the numbers in the array
def checkValid(arr, number):
    # first number
    for i in range(len(arr) - 1):
        # number is bigger than number # skip
        if arr[i] > number:
            continue
        # second number
        for j in range(i + 1, len(arr)):
            # found two numbers
            if arr[i] + arr[j] == number:
                return True
    # never found number
    return False

# found contiguous set of numbers that sum to the the number
def findContiguousSum(arr, number):
    # find index of number
    index = arr.index(number)
    # find correct indexes
    for i in range(index):
        for j in range(i+2, index+1):
            total = sum(arr[i:j])
            if total == number:
                return i, j-1

limit = 25
valid = numbers [:limit]
# find invalid number
for i in numbers[limit:]:
    # found invalid
    if not checkValid(valid, i):
        invalidNum = i
        break
    # valid number # add to list and remove first (0th) number
    else:
        valid.pop(0)
        valid.append(i)

# part 1
print(f'Your invalid number is {invalidNum}')

# part 2
i, j = findContiguousSum(numbers, invalidNum)
print(f'The index bounds are {i} and {j} (inclusive)')
print(f'The numbers are {numbers[i]} and {numbers[j]}')
print(f'The sum of the numbers is {numbers[i] + numbers[j]}')