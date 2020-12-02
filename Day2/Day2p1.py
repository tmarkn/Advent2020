# password object
class Password:
    def __init__(self, min, max, letter, password, valid = False):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password
        self.valid = valid

# password constructor
def makePassword(string):
    # constructor format: 
    #   1-3 a: abcde

    # get correct parts
    parts = string.split()          # split via whitespace
    min, max = parts[0].split('-')  # min and max are first  # seperated by -
    letter = parts[1][:1]           # letter is next  # remove trailing colon
    password = parts[2]             # password is last

    # create password and check validity
    pw = Password(int(min), int(max), letter, password)
    if checkValidity(pw):
        pw.valid = True

    return pw

# check if password is valid
# the number of the specified letter is between the two values
def checkValidity(pw):
    numLetters = pw.password.count(pw.letter)
    if numLetters >= pw.min and numLetters <= pw.max:
        return True
    return False
    

# get input
with open('Day2/input.txt', 'r') as f:
    passwords = [makePassword(x) for x in f.readlines()]

# check letters
count = 0
for pw in passwords:
    if pw.valid == True:
        count += 1

print(f'Number of valid passords: {count}')