# get input
with open('Day06/input.txt', 'r') as f:
    answerList = f.read().split('\n\n')

# part 1
yeses = 0
# each group
for groupAnswers in answerList:
    grpAnswers = set()
    # each person
    for answers in groupAnswers.split():
        # each letter
        for answer in answers:
            grpAnswers.add(answer)
    # add to yeses received
    yeses += len(grpAnswers)
print(f'The number of yeses is {yeses}')

# part 2
groupYeses = 0
# each group
for groupAnswers in answerList:
    memberCount = 0
    grpAnswers = {}
    # each person
    for answers in groupAnswers.split():
        # count members
        memberCount += 1
        # each letter
        for answer in answers:
            try:
                grpAnswers[answer] += 1
            except KeyError:
                grpAnswers[answer] = 1
    # add to group yeses if everyone answered yes
    groupYeses += sum(grpAnswers[answer] == memberCount for answer in grpAnswers)
print(f'The number of group yeses is {groupYeses}')