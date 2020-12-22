import itertools
import re

# check if the values fit within the any of the bounds
def followsRules(rules, num):
    rulesIn = set()
    for rule in rules:
        boundaries = rules[rule]
        for bounds in boundaries:
            if bounds[0] <= num <= bounds[1]:
                rulesIn.add(rule)
    return rulesIn

# reduce to one rule name per column
def arrReduce(arr):
    copy = arr[:]
    final = [None] * len(arr)
    todo = set()
    # do until no more items to remove
    while True:
        noMorePop = True
        # remove all that only have one label
        # must be of that label
        for i, x in enumerate(copy):
            if len(x) == 1:
                popped = x.pop()
                todo.add(popped)
                final[i] = popped
        # remove those labels from the rest of the columns
        for x in range(len(todo)):
            popped = todo.pop()
            for y in copy:
                try:
                    y.remove(popped)
                    noMorePop = False
                except KeyError:
                    pass
        # no more items # return
        if noMorePop:
            return final

# match boundaries
regex = re.compile(r'[0-9]+\-[0-9]+')

# get input
with open('Day16/input.txt', 'r') as f:
    notes = f.read()

# split into three different sections of notes
rules = {}
basedRules, basedTicket, basedNearbyTickets = notes.split('\n\n')

# rules
for rule in basedRules.split('\n'):
    # names
    ruleName = rule[:rule.find(':')]
    rules[ruleName] = []
    # boundaries
    for bounds in re.findall(regex, rule):
        boundaries = tuple(map(int, bounds.split('-')))
        rules[ruleName].append(boundaries)

# my ticket
bTicket = basedTicket.split('\n')[1]
myTicket = tuple(map(int, bTicket.split(',')))

# nearby tickets
bNearTickets = basedNearbyTickets.split('\n')[1:]
nearbyTickets = [tuple(map(int, ticket.split(','))) for ticket in bNearTickets]

# check for all invalid numbers
validTickets = []
total = 0
# check each ticket
for ticket in nearbyTickets:
    valid = True
    rulesIn = []
    # check each number
    for num in ticket:
        # check all rules followed
        rulesFollowed = followsRules(rules, num)
        # no rules followed
        if len(rulesFollowed) == 0:
            total += num
            valid = False
        # rules followed
        if valid:
            rulesIn.append(rulesFollowed)
    # at least one rule for each
    if valid:
        validTickets.append(rulesIn)
print(f'The ticket scanning error rate is {total}')

# transpose array to make iterating easier
TValidTickets = list(map(list, itertools.zip_longest(*validTickets, fillvalue=None)))
possibleRules = []
# find possible rule set per column
for i, TTicket in enumerate(TValidTickets):
    possRules = set()
    # check each rule
    for rule in rules:
        # check each value in column
        for possibleTicketRules in TTicket:
            if rule not in possibleTicketRules:
                break
        # rule possible in all values
        else: 
            possRules.add(rule)
    possibleRules.append(possRules)

# find possible combination of columns
ruleLabels = arrReduce(possibleRules)
# multiply each column with depature in name
product = 1
for i, label in enumerate(ruleLabels):
    if 'departure' in label:
        product *= myTicket[i]

print(f'The product of the columns that contain the word"departure" is {product}')