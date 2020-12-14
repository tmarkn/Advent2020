import math

# get input
with open('Day13/input.txt', 'r') as f:
    specTime = int(f.readline())
    buses = f.readline().split(',')

validBuses = [int(bus) for bus in buses if bus != 'x']

# get times of each bus after the specified time
busTimes = []
for bus in validBuses:
    busTimes.append(math.ceil(specTime / bus) * bus)

# get lowest time
time = min(busTimes)
busID = validBuses[busTimes.index(min(busTimes))]
print(f'The first bus to arrive is bus {busID} at {time}')
print(f'The answer is {(time - specTime) * busID}')

# part 2
# Chinese Remainder Theorem
# get the difference in between buses
firstBusIndex = buses.index(str(validBuses[0]))
timeDifferences = []
for bus in validBuses:
    timeDiff = buses.index(str(bus)) - firstBusIndex
    timeDifferences.append(-timeDiff % bus)

# get total product of bus ids
totalProduct = 1
for x in validBuses:
    totalProduct *= x
# get the quotient of the total product and each bus id
indvProducts = []
for i in range(len(validBuses)):
    indvProducts.append(totalProduct // validBuses[i])
# get the multiplicands of each number
factors = []
for i in range(len(validBuses)):
    j = 1
    while (indvProducts[i] * j) % validBuses[i] != timeDifferences[i]:
        j+= 1
    factors.append(j)
# get the final number by adding the product of indvProducts and their multiplicands
final = 0
for i in range(len(validBuses)):
    final += factors[i] * indvProducts[i]
final %= totalProduct

print(f'The earliest time is {final}')