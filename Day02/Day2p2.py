# password object
class Password:
    def __init__(self, pos1, pos2, letter, password):
        self.pos1 = pos1
        self.pos2 = pos2
        self.letter = letter
        self.password = password

    # check if password is valid
    # one of the two positions must be the specified letter
    def isValid(self):
        valid = False
        if self.password[self.pos1-1] == self.letter:
            valid = not valid
        if self.password[self.pos2-1] == self.letter:
            valid = not valid
        return valid

# password constructor
def makePassword(string):
    # constructor format: 
    #   1-3 a: abcde

    # get correct parts
    parts = string.split()              # split via whitespace
    pos1, pos2 = parts[0].split('-')    # pos1 and pos2 are first  # seperated by -
    letter = parts[1][:1]               # letter is next  # remove trailing colon
    password = parts[2]                 # password is last

    # create password and check validity
    pw = Password(int(pos1), int(pos2), letter, password)
    return pw

# get input
with open('Day2/input.txt', 'r') as f:
    passwords = [makePassword(x) for x in f.readlines()]

# check letters
numValidPasswords = sum(pw.isValid() for pw in passwords)
print(f'The number of valid passwords: {numValidPasswords}')