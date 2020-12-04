# password object
class Password:
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

    # check if password is valid
    # the number of the specified letter is between the two values
    def isValid(self):
        numLetters = self.password.count(self.letter)
        if numLetters >= self.min and numLetters <= self.max:
            return True
        return False

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
    return pw

# get input
with open('Day2/input.txt', 'r') as f:
    passwords = [makePassword(x) for x in f.readlines()]

# check letters
numValidPasswords = sum(pw.isValid() for pw in passwords)
print(f'The number of valid passwords: {numValidPasswords}')