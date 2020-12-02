# password object
class Password:
    def __init__(self, pos1, pos2, letter, password, valid = False):
        self.pos1 = pos1
        self.pos2 = pos2
        self.letter = letter
        self.password = password
        self.valid = valid

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
    if checkValidity(pw):
        pw.valid = True

    return pw

# check if password is valid
def checkValidity(pw):
    valid = False
    if pw.password[pw.pos1-1] == pw.letter:
        valid = not valid
    if pw.password[pw.pos2-1] == pw.letter:
        valid = not valid
    return valid

# get input
with open('Day2/input.txt', 'r') as f:
    passwords = [makePassword(x) for x in f.readlines()]

# check letters
count = 0
for pw in passwords:
    if pw.valid == True:
        count += 1

print(f'Number of valid passords: {count}')